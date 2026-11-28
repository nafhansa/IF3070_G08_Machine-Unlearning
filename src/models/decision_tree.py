"""
Decision Tree Learning varian C4.5, from scratch (NumPy).

Acuan materi (Slide Materi10 DTL + video IF3270 Bu Ulfa):
- ID3 (hal. 14, video 03): top-down, greedy, pilih atribut terbaik untuk tiap simpul.
- Entropy & Information Gain (hal. 18-22, video 04):
      Entropy(S) = - sum_i p_i log2 p_i
      Gain(S, A) = Entropy(S) - sum_v |S_v|/|S| * Entropy(S_v)
- Gain Ratio (hal. 48-49, video 08):
      SplitInformation(S, A) = - sum_v |S_v|/|S| log2 |S_v|/|S|
      GainRatio = Gain / SplitInformation
  Heuristik dari slide: gain ratio hanya dipakai untuk atribut dengan gain >= rata-rata gain,
  untuk menghindari SplitInformation yang ~0.
- Atribut kontinu (hal. 42-43 & 50, video 06): urutkan nilai, kandidat threshold = titik tengah
  antara dua nilai bertetangga, pilih threshold dengan gain terbaik -> cabang biner (A <= c, A > c).
- Missing value (hal. 45, video 07), cara C4.5:
      * Gain hanya dihitung dari data yang nilainya diketahui, lalu dikali fraksi F = |known|/|S|.
      * Data yang nilainya hilang dikirim ke SEMUA cabang dengan bobot proporsional
        (contoh slide: 6/10 ke v1, 4/10 ke v2).
      * Saat klasifikasi, data dengan nilai hilang juga diteruskan ke semua cabang
        dan hasil probabilitas tiap cabang dijumlahkan berbobot.
- Overfitting & pruning (hal. 31-40, video 05):
      * pre-pruning: max_depth, min_samples_split, min_samples_leaf, min_gain
      * Reduced Error Pruning (hal. 36-37), greedy dengan validation set: prune_reduced_error()
      * Rule Post-Pruning, cara khas C4.5 (hal. 38-39): to_rules(), prune_rules(), predict_proba_rules()

Atribut kategorikal (nominal) dipecah multiway: satu cabang untuk setiap nilai (seperti ID3/C4.5).
Nilai kategori yang tidak pernah dilihat saat training diperlakukan seperti missing value.
"""
from __future__ import annotations

from collections import deque

import numpy as np

from .base import BaseModel

_EPS = 1e-12


class Node:
    """Satu simpul pohon. Simpul daun tidak memiliki children."""

    __slots__ = ("class_weights", "feature", "kind", "threshold", "categories", "children",
                 "branch_frac", "depth", "gain", "n_weight", "node_id")

    def __init__(self, class_weights, depth):
        self.class_weights = class_weights   # jumlah bobot tiap kelas pada simpul ini (data latih)
        self.feature = None                  # indeks fitur yang diuji
        self.kind = None                     # 'num' atau 'cat'
        self.threshold = None                # untuk fitur numerik: cabang kiri = x <= threshold
        self.categories = None               # untuk fitur kategorikal: kode kategori per cabang
        self.children = []                   # list Node
        self.branch_frac = None              # fraksi data (yang diketahui) per cabang -> untuk missing value
        self.depth = depth
        self.gain = 0.0
        self.n_weight = float(class_weights.sum())
        self.node_id = -1

    @property
    def is_leaf(self) -> bool:
        return len(self.children) == 0

    def make_leaf(self):
        self.children = []
        self.feature = self.kind = self.threshold = self.categories = self.branch_frac = None


def _impurity(counts: np.ndarray, kind: str) -> np.ndarray:
    """Entropy atau Gini untuk satu/banyak distribusi kelas (baris = distribusi)."""
    counts = np.atleast_2d(counts)
    total = counts.sum(1, keepdims=True)
    p = counts / np.maximum(total, _EPS)
    if kind == "gini":
        return 1.0 - (p ** 2).sum(1)
    with np.errstate(divide="ignore", invalid="ignore"):
        logp = np.where(p > 0, np.log2(np.where(p > 0, p, 1.0)), 0.0)
    return -(p * logp).sum(1)


def _split_info(weights: np.ndarray) -> float:
    """SplitInformation = -sum (w_b/W) log2 (w_b/W)."""
    w = weights[weights > 0]
    p = w / w.sum()
    return float(-(p * np.log2(p)).sum())


class C45DecisionTree(BaseModel):
    def __init__(self, criterion: str = "gain_ratio", impurity: str = "entropy", max_depth: int | None = None,
                 min_samples_split: float = 2, min_samples_leaf: float = 1, min_gain: float = 1e-7,
                 laplace: float = 0.0, categorical_features="auto", max_categories: int = 0,
                 use_average_gain_heuristic: bool = True):
        """
        Parameter
        ---------
        criterion          : 'gain_ratio' (C4.5) atau 'gain' (ID3, information gain murni)
        impurity           : 'entropy' (sesuai slide) atau 'gini'
        max_depth          : kedalaman maksimum (None = tanpa batas)
        min_samples_split  : bobot data minimum agar simpul boleh dipecah
        min_samples_leaf   : bobot data minimum pada setiap cabang hasil split
        min_gain           : gain minimum agar split dilakukan
        laplace            : smoothing Laplace untuk probabilitas daun (0 = proporsi apa adanya)
        categorical_features : 'auto' (kolom non-numerik = kategorikal) atau list indeks kolom
        max_categories     : pada mode 'auto', kolom numerik dengan nilai unik <= ini juga
                             diperlakukan kategorikal (0 = nonaktif)
        use_average_gain_heuristic : terapkan heuristik slide (gain ratio hanya untuk gain >= rata-rata)
        """
        self.criterion = criterion
        self.impurity = impurity
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.min_samples_leaf = min_samples_leaf
        self.min_gain = min_gain
        self.laplace = laplace
        self.categorical_features = categorical_features
        self.max_categories = max_categories
        self.use_average_gain_heuristic = use_average_gain_heuristic

    # ================================================================== #
    # Encoding input: kolom numerik -> float (NaN = hilang),
    # kolom kategorikal -> kode integer (-1 = hilang / tidak dikenal)
    # ================================================================== #
    def _encode(self, X, fitting: bool):
        if hasattr(X, "columns"):
            cols = [X[c].to_numpy() for c in X.columns]
            names = [str(c) for c in X.columns]
        else:
            X = np.asarray(X)
            cols = [X[:, j] for j in range(X.shape[1])]
            names = [f"x{j}" for j in range(X.shape[1])]
        if fitting:
            self.feature_names_ = names
            self.is_categorical_ = []
            for j, col in enumerate(cols):
                if isinstance(self.categorical_features, (list, tuple, set)):
                    is_cat = j in self.categorical_features or names[j] in self.categorical_features
                elif col.dtype.kind not in "fiub":
                    is_cat = True
                elif self.max_categories > 0:
                    v = col.astype(float)
                    is_cat = len(np.unique(v[~np.isnan(v)])) <= self.max_categories
                else:
                    is_cat = False
                self.is_categorical_.append(is_cat)
            self.category_maps_ = [None] * len(cols)
        encoded = np.empty((len(cols[0]), len(cols)), dtype=float)
        for j, col in enumerate(cols):
            if self.is_categorical_[j]:
                keys = np.array([None if (v is None or (isinstance(v, float) and np.isnan(v))) else str(v) for v in col],
                                dtype=object)
                if fitting:
                    uniq = sorted({k for k in keys if k is not None})
                    self.category_maps_[j] = {k: i for i, k in enumerate(uniq)}
                cmap = self.category_maps_[j]
                encoded[:, j] = [cmap.get(k, -1) if k is not None else -1 for k in keys]
            else:
                encoded[:, j] = col.astype(float)
        return encoded

    # ================================================================== #
    # Training
    # ================================================================== #
    def fit(self, X, y, sample_weight=None):
        Xe = self._encode(X, fitting=True)
        y = np.asarray(y)
        self.classes_, y_idx = np.unique(y, return_inverse=True)
        self.n_classes_ = len(self.classes_)
        w = np.ones(len(y)) if sample_weight is None else np.asarray(sample_weight, dtype=float)
        self.n_features_ = Xe.shape[1]
        self.feature_importances_ = np.zeros(self.n_features_)
        self._X, self._y = Xe, y_idx
        self.root_ = self._build(np.arange(len(y)), w, depth=0)
        del self._X, self._y
        total = self.feature_importances_.sum()
        if total > 0:
            self.feature_importances_ /= total
        self._assign_ids()
        return self

    def _class_weights(self, idx, w):
        return np.bincount(self._y[idx], weights=w, minlength=self.n_classes_).astype(float)

    def _build(self, idx, w, depth):
        cw = self._class_weights(idx, w)
        node = Node(cw, depth)
        total = cw.sum()
        if (np.count_nonzero(cw > _EPS) <= 1 or total < self.min_samples_split
                or (self.max_depth is not None and depth >= self.max_depth)):
            return node
        best = self._best_split(idx, w, cw)
        if best is None:
            return node
        node.feature, node.kind, node.gain = best["feature"], best["kind"], best["gain"]
        node.threshold, node.categories = best.get("threshold"), best.get("categories")
        self.feature_importances_[node.feature] += best["gain"] * total
        # --- partisi data ke cabang -----------------------------------
        x = self._X[idx, node.feature]
        missing = np.isnan(x) if node.kind == "num" else (x < 0)
        branch_of = np.full(len(idx), -1)
        if node.kind == "num":
            branch_of[~missing] = (x[~missing] > node.threshold).astype(int)
            n_branch = 2
        else:
            code_to_branch = {c: b for b, c in enumerate(node.categories)}
            branch_of[~missing] = [code_to_branch.get(int(c), -1) for c in x[~missing]]
            n_branch = len(node.categories)
        known_w = np.array([w[branch_of == b].sum() for b in range(n_branch)])
        node.branch_frac = known_w / known_w.sum()
        miss_idx = idx[branch_of == -1]
        miss_w = w[branch_of == -1]
        for b in range(n_branch):
            sel = branch_of == b
            # data yang nilainya hilang ikut ke setiap cabang dengan bobot proporsional (C4.5)
            child_idx = np.concatenate([idx[sel], miss_idx])
            child_w = np.concatenate([w[sel], miss_w * node.branch_frac[b]])
            keep = child_w > 1e-9
            node.children.append(self._build(child_idx[keep], child_w[keep], depth + 1))
        return node

    def _best_split(self, idx, w, cw_parent):
        total_w = w.sum()
        candidates = []
        for f in range(self.n_features_):
            x = self._X[idx, f]
            if self.is_categorical_[f]:
                res = self._eval_categorical(x, idx, w, total_w)
            else:
                res = self._eval_numeric(x, idx, w, total_w)
            if res is not None:
                res["feature"] = f
                candidates.append(res)
        if not candidates:
            return None
        gains = np.array([c["gain"] for c in candidates])
        if self.criterion == "gain":
            best = candidates[int(np.argmax(gains))]
        else:
            # Heuristik slide: hanya atribut dengan gain >= rata-rata yang dibandingkan gain ratio-nya
            pool = [c for c in candidates if c["gain"] >= gains.mean() - 1e-12] if self.use_average_gain_heuristic else candidates
            ratios = np.array([c["gain"] / c["split_info"] if c["split_info"] > _EPS else 0.0 for c in pool])
            best = pool[int(np.argmax(ratios))]
        if best["gain"] <= self.min_gain:
            return None
        return best

    def _eval_numeric(self, x, idx, w, total_w):
        known = ~np.isnan(x)
        if known.sum() < 2:
            return None
        xk, yk, wk = x[known], self._y[idx][known], w[known]
        order = np.argsort(xk, kind="mergesort")
        xk, yk, wk = xk[order], yk[order], wk[order]
        W_known = wk.sum()
        F = W_known / total_w                                   # fraksi data yang diketahui
        onehot = np.zeros((len(yk), self.n_classes_))
        onehot[np.arange(len(yk)), yk] = wk
        left = np.cumsum(onehot, axis=0)[:-1]                   # distribusi kelas cabang kiri utk tiap posisi
        total_counts = onehot.sum(0)
        right = total_counts[None, :] - left
        valid = xk[1:] > xk[:-1]                                # hanya di antara dua nilai berbeda
        wl, wr = left.sum(1), right.sum(1)
        valid &= (wl >= self.min_samples_leaf) & (wr >= self.min_samples_leaf)
        if not valid.any():
            return None
        H = _impurity(total_counts, self.impurity)[0]
        child_H = (wl * _impurity(left, self.impurity) + wr * _impurity(right, self.impurity)) / W_known
        gain_all = F * (H - child_H)
        gain_all[~valid] = -np.inf
        pos = int(np.argmax(gain_all))
        gain = float(gain_all[pos])
        if gain <= 0:
            return None
        miss_w = total_w - W_known
        split_info = _split_info(np.array([wl[pos], wr[pos], miss_w]))
        threshold = (xk[pos] + xk[pos + 1]) / 2.0               # titik tengah (slide: (48+60)/2 = 54)
        return {"kind": "num", "gain": gain, "split_info": split_info, "threshold": float(threshold)}

    def _eval_categorical(self, x, idx, w, total_w):
        known = x >= 0
        if known.sum() < 2:
            return None
        codes = x[known].astype(int)
        yk, wk = self._y[idx][known], w[known]
        cats = np.unique(codes)
        if len(cats) < 2:
            return None
        table = np.zeros((len(cats), self.n_classes_))
        pos = np.searchsorted(cats, codes)
        np.add.at(table, (pos, yk), wk)
        branch_w = table.sum(1)
        if (branch_w >= self.min_samples_leaf).sum() < 2:
            return None
        W_known = wk.sum()
        F = W_known / total_w
        H = _impurity(table.sum(0), self.impurity)[0]
        child_H = (branch_w * _impurity(table, self.impurity)).sum() / W_known
        gain = float(F * (H - child_H))
        if gain <= 0:
            return None
        split_info = _split_info(np.append(branch_w, total_w - W_known))
        return {"kind": "cat", "gain": gain, "split_info": split_info, "categories": [int(c) for c in cats]}

    # ================================================================== #
    # Prediksi
    # ================================================================== #
    def _leaf_proba(self, node):
        cw = node.class_weights + self.laplace
        return cw / max(cw.sum(), _EPS)

    def _route(self, node, Xe, rows, weights, out):
        """Teruskan baris ke bawah pohon. Baris dengan nilai hilang dibagi ke semua cabang."""
        if node.is_leaf:
            out[rows] += weights[:, None] * self._leaf_proba(node)[None, :]
            return
        x = Xe[rows, node.feature]
        if node.kind == "num":
            missing = np.isnan(x)
            branch = np.where(missing, -1, (x > node.threshold).astype(int))
        else:
            code_to_branch = {c: b for b, c in enumerate(node.categories)}
            branch = np.array([code_to_branch.get(int(c), -1) if c >= 0 else -1 for c in x], dtype=int)
        for b, child in enumerate(node.children):
            sel = branch == b
            miss = branch == -1
            r = np.concatenate([rows[sel], rows[miss]])
            ww = np.concatenate([weights[sel], weights[miss] * node.branch_frac[b]])
            if len(r):
                self._route(child, Xe, r, ww, out)

    def predict_proba(self, X) -> np.ndarray:
        Xe = self._encode(X, fitting=False)
        out = np.zeros((Xe.shape[0], self.n_classes_))
        self._route(self.root_, Xe, np.arange(Xe.shape[0]), np.ones(Xe.shape[0]), out)
        return out / out.sum(1, keepdims=True)

    def predict(self, X) -> np.ndarray:
        return self.classes_[np.argmax(self.predict_proba(X), axis=1)]

    # ================================================================== #
    # Pruning
    # ================================================================== #
    def _validation_counts(self, Xe, y_idx):
        """Bobot kelas data validasi yang sampai di setiap simpul (missing dibagi proporsional)."""
        counts = {}

        def collect(node, rows, weights):
            counts[id(node)] = (np.bincount(y_idx[rows], weights=weights, minlength=self.n_classes_)
                                if len(rows) else np.zeros(self.n_classes_))
            if node.is_leaf:
                return
            x = Xe[rows, node.feature]
            if node.kind == "num":
                branch = np.where(np.isnan(x), -1, (x > node.threshold).astype(int))
            else:
                m = {c: b for b, c in enumerate(node.categories)}
                branch = np.array([m.get(int(c), -1) if c >= 0 else -1 for c in x], dtype=int)
            for b, child in enumerate(node.children):
                sel, miss = branch == b, branch == -1
                collect(child, np.concatenate([rows[sel], rows[miss]]),
                        np.concatenate([weights[sel], weights[miss] * node.branch_frac[b]]))

        collect(self.root_, np.arange(len(y_idx)), np.ones(len(y_idx)))
        return counts

    def prune_reduced_error(self, X_val, y_val):
        """
        Reduced Error Pruning PERSIS seperti slide Materi10 hal. 36 (Mitchell 1997, bab 3.7.1):
          - setiap simpul keputusan adalah kandidat; memangkas = mengganti subtree dengan daun berisi
            kelas mayoritas (data latih) simpul tersebut;
          - "Do until further pruning is harmful":
              1. evaluasi dampak memangkas SETIAP simpul pada error validation set,
              2. pangkas secara greedy SATU simpul yang paling memperbaiki akurasi validasi
                 (pemangkasan yang tidak mengubah error juga diterima -> pohon lebih sederhana),
              3. ulangi; berhenti bila semua kandidat justru menaikkan error.
        """
        Xe = self._encode(X_val, fitting=False)
        y_idx = np.searchsorted(self.classes_, np.asarray(y_val))
        counts = self._validation_counts(Xe, y_idx)

        def leaf_err(node):
            c = counts[id(node)]
            return c.sum() - c[np.argmax(node.class_weights)]

        def subtree_err(node):
            return leaf_err(node) if node.is_leaf else sum(subtree_err(c) for c in node.children)

        self.pruning_history_ = []
        while True:
            internal, q = [], deque([self.root_])
            while q:
                n = q.popleft()
                if not n.is_leaf:
                    internal.append(n)
                    q.extend(n.children)
            if not internal:
                break
            gains = [subtree_err(n) - leaf_err(n) for n in internal]   # >0 berarti error validasi turun
            best = int(np.argmax(gains))
            if gains[best] < -1e-12:
                break
            internal[best].make_leaf()
            self.pruning_history_.append(subtree_err(self.root_))
        self._assign_ids()
        return self

    # ------------------------------------------------------------------ #
    # Rule Post-Pruning (slide Materi10 hal. 38-39, video DTL-05)
    # ------------------------------------------------------------------ #
    def to_rules(self):
        """Ubah pohon menjadi himpunan aturan IF-THEN: satu aturan untuk setiap jalur akar -> daun."""
        rules = []

        def walk(node, conds):
            if node.is_leaf:
                rules.append({"conds": list(conds), "leaf": node})
                return
            for b, child in enumerate(node.children):
                if node.kind == "num":
                    cond = (node.feature, "<=" if b == 0 else ">", node.threshold)
                else:
                    cond = (node.feature, "==", node.categories[b])
                walk(child, conds + [cond])

        walk(self.root_, [])
        return rules

    @staticmethod
    def _cond_mask(Xe, cond):
        f, op, v = cond
        x = Xe[:, f]
        if op == "<=":
            return x <= v          # NaN -> False (nilai hilang tidak memenuhi syarat)
        if op == ">":
            return x > v
        return x == v

    def prune_rules(self, X_val, y_val):
        """
        Rule Post-Pruning (C4.5) sesuai slide hal. 38:
          1. pohon sudah ditumbuhkan sampai fit (boleh overfit)            -> fit()
          2. ubah setiap jalur akar->daun menjadi satu aturan                -> to_rules()
          3. generalisasi setiap aturan: hapus prekondisi yang MENAIKKAN estimasi akurasinya
             (greedy, satu per satu, sampai tidak ada yang menaikkan)
          4. urutkan aturan berdasarkan estimasi akurasi; saat klasifikasi aturan dipakai berurutan
        Estimasi akurasi dihitung pada validation set (slide hal. 39: "over validation set / training set")
        memakai koreksi Laplace (benar + 1) / (tercakup + 2) supaya aturan yang hanya mencakup sedikit data
        tidak mendapat akurasi 100% semu. Data yang tidak cocok dengan aturan mana pun mendapat kelas
        mayoritas data latih (PLURALITY-VALUE, slide hal. 15).
        """
        Xe = self._encode(X_val, fitting=False)
        y_idx = np.searchsorted(self.classes_, np.asarray(y_val))
        rules = self.to_rules()
        masks_cache = {}

        def mask_of(conds):
            m = np.ones(len(y_idx), dtype=bool)
            for c in conds:
                if c not in masks_cache:
                    masks_cache[c] = self._cond_mask(Xe, c)
                m &= masks_cache[c]
            return m

        def estimate(conds, cls):
            m = mask_of(conds)
            return (np.sum(y_idx[m] == cls) + 1.0) / (m.sum() + 2.0)

        pruned = []
        for r in rules:
            cls = int(np.argmax(r["leaf"].class_weights))
            conds = list(r["conds"])
            acc = estimate(conds, cls)
            improved = True
            while improved and conds:
                improved = False
                trials = [(estimate(conds[:i] + conds[i + 1:], cls), i) for i in range(len(conds))]
                best_acc, best_i = max(trials)
                if best_acc > acc + 1e-12:
                    conds.pop(best_i)
                    acc, improved = best_acc, True
            m = mask_of(conds)
            dist = np.bincount(y_idx[m], minlength=self.n_classes_).astype(float)
            pruned.append({"conds": conds, "class": cls, "accuracy": float(acc), "coverage": int(m.sum()),
                           "proba": (dist + 1.0) / (dist.sum() + self.n_classes_)})
        pruned.sort(key=lambda r: (-r["accuracy"], -r["coverage"]))
        prior = self.root_.class_weights / self.root_.class_weights.sum()
        self.rules_ = pruned
        self.default_proba_ = prior
        return self

    def predict_proba_rules(self, X) -> np.ndarray:
        """Klasifikasi dengan aturan terurut: aturan pertama yang cocok menentukan peluang kelas."""
        Xe = self._encode(X, fitting=False)
        out = np.tile(self.default_proba_, (len(Xe), 1))
        done = np.zeros(len(Xe), dtype=bool)
        for r in self.rules_:
            m = ~done
            for c in r["conds"]:
                m &= self._cond_mask(Xe, c)
            out[m] = r["proba"]
            done |= m
        return out

    def rule_text(self, rule) -> str:
        parts = []
        for f, op, v in rule["conds"]:
            name = self.feature_names_[f]
            if op == "==":
                inv = {i: k for k, i in self.category_maps_[f].items()}
                parts.append(f"{name} = {inv[v]}")
            else:
                parts.append(f"{name} {op} {v:.4g}")
        return ("IF " + " AND ".join(parts) if parts else "IF (selalu)") + \
            f" THEN {self.classes_[rule['class']]}  [akurasi {rule['accuracy']:.3f}, cakupan {rule['coverage']}]"

    # ================================================================== #
    # Utilitas: statistik pohon, export aturan, traversal untuk visualisasi
    # ================================================================== #
    def _assign_ids(self):
        q, i = deque([self.root_]), 0
        while q:
            n = q.popleft()
            n.node_id = i
            i += 1
            q.extend(n.children)

    def get_depth(self) -> int:
        def d(n):
            return n.depth if n.is_leaf else max(d(c) for c in n.children)
        return d(self.root_)

    def get_n_leaves(self) -> int:
        def c(n):
            return 1 if n.is_leaf else sum(c(ch) for ch in n.children)
        return c(self.root_)

    def branch_label(self, node, b) -> str:
        name = self.feature_names_[node.feature]
        if node.kind == "num":
            return f"{name} <= {node.threshold:.4g}" if b == 0 else f"{name} > {node.threshold:.4g}"
        inv = {v: k for k, v in self.category_maps_[node.feature].items()}
        return f"{name} = {inv[node.categories[b]]}"

    def export_text(self, max_depth: int = 3) -> str:
        """Representasi pohon sebagai aturan IF-THEN bertingkat (slide hal. 9-10)."""
        lines = []

        def walk(node, indent):
            if node.is_leaf or node.depth >= max_depth:
                p = self._leaf_proba(node)
                lines.append("  " * indent + f"-> kelas {self.classes_[np.argmax(p)]} "
                             f"(p={p.max():.3f}, bobot={node.n_weight:.1f})")
                return
            for b, child in enumerate(node.children):
                lines.append("  " * indent + "IF " + self.branch_label(node, b))
                walk(child, indent + 1)

        walk(self.root_, 0)
        return "\n".join(lines)
