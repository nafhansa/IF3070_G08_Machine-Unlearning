# Evaluation metrics and data splitting (perhitunganny pake NumPy)
import numpy as np


# Nilai acuan pada instruction/desc regresi.md.
RMSE_BASELINE = 6.9676


def confusion_matrix(y_true, y_pred):
    # Posisi matrix: [[TN, FP], [FN, TP]]. Label yang dipakai 0 dan 1.
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)
    tn = np.sum((y_true == 0) & (y_pred == 0))
    fp = np.sum((y_true == 0) & (y_pred == 1))
    fn = np.sum((y_true == 1) & (y_pred == 0))
    tp = np.sum((y_true == 1) & (y_pred == 1))
    return np.array([[tn, fp], [fn, tp]])


def accuracy(y_true, y_pred):
    return float(np.mean(np.asarray(y_true) == np.asarray(y_pred)))


def precision(y_true, y_pred):
    matrix = confusion_matrix(y_true, y_pred)
    tp, fp = matrix[1, 1], matrix[0, 1]
    if tp + fp == 0:
        return 0.0
    return float(tp / (tp + fp))


def recall(y_true, y_pred):
    matrix = confusion_matrix(y_true, y_pred)
    tp, fn = matrix[1, 1], matrix[1, 0]
    if tp + fn == 0:
        return 0.0
    return float(tp / (tp + fn))


def f1(y_true, y_pred):
    p = precision(y_true, y_pred)
    r = recall(y_true, y_pred)
    if p + r == 0:
        return 0.0
    return float(2 * p * r / (p + r))


def roc_auc(y_true, y_score):
    # AUC = peluang skor kelas 1 lebih tinggi daripada kelas 0.
    # Ranking dengan skor seri dihitung setengah (Mann-Whitney U.
    y_true = np.asarray(y_true)
    y_score = np.asarray(y_score, dtype=float)
    if len(y_true) != len(y_score):
        raise ValueError("Jumlah label dan skor harus sama")

    n_pos = int(np.sum(y_true == 1))
    n_neg = int(np.sum(y_true == 0))
    if n_pos == 0 or n_neg == 0:
        raise ValueError("AUC membutuhkan sampel kelas 0 dan 1")

    order = np.argsort(y_score, kind="mergesort")
    ranks = np.empty(len(y_score), dtype=float)
    i = 0
    while i < len(order):
        j = i
        while j + 1 < len(order) and y_score[order[j + 1]] == y_score[order[i]]:
            j += 1
        # Rank dimulai dari 1, sedangkan indeks array dimulai dari 0.
        average_rank = (i + j) / 2 + 1
        ranks[order[i:j + 1]] = average_rank
        i = j + 1

    sum_pos = np.sum(ranks[y_true == 1])
    auc = (sum_pos - n_pos * (n_pos + 1) / 2) / (n_pos * n_neg)
    return float(auc)


def log_loss(y_true, y_prob, eps=1e-15):
    y_true = np.asarray(y_true, dtype=float)
    y_prob = np.clip(np.asarray(y_prob, dtype=float), eps, 1 - eps)
    loss = y_true * np.log(y_prob) + (1 - y_true) * np.log(1 - y_prob)
    return float(-np.mean(loss))


def classification_report(y_true, y_prob, threshold=0.5):
    y_pred = (np.asarray(y_prob) >= threshold).astype(int)
    return {
        "roc_auc": roc_auc(y_true, y_prob),
        "accuracy": accuracy(y_true, y_pred),
        "precision": precision(y_true, y_pred),
        "recall": recall(y_true, y_pred),
        "f1": f1(y_true, y_pred),
        "log_loss": log_loss(y_true, y_prob),
    }


def mae(y_true, y_pred):
    error = np.asarray(y_true, dtype=float) - np.asarray(y_pred, dtype=float)
    return float(np.mean(np.abs(error)))


def mse(y_true, y_pred):
    error = np.asarray(y_true, dtype=float) - np.asarray(y_pred, dtype=float)
    return float(np.mean(error ** 2))


def rmse(y_true, y_pred):
    return float(np.sqrt(mse(y_true, y_pred)))


def r2(y_true, y_pred):
    y_true = np.asarray(y_true, dtype=float)
    y_pred = np.asarray(y_pred, dtype=float)
    ss_res = np.sum((y_true - y_pred) ** 2)
    ss_tot = np.sum((y_true - np.mean(y_true)) ** 2)
    if ss_tot == 0:
        # Jika target selalu sama, rumus biasa akan membagi dengan nol
        return 1.0 if ss_res == 0 else 0.0
    return float(1 - ss_res / ss_tot)


def regression_report(y_true, y_pred):
    return {"mae": mae(y_true, y_pred), "rmse": rmse(y_true, y_pred), "r2": r2(y_true, y_pred)}


# Rumus skor compiled dari instruction/desc regresi.md
def auc_norm(auc):
    return float(np.clip((auc - 0.5) / 0.5, 0, 1))


def rmse_norm(rmse_value, baseline=RMSE_BASELINE):
    return float(np.clip(1 - rmse_value / baseline, 0, 1))


def competition_score(auc, rmse_value):
    return 0.7 * auc_norm(auc) + 0.3 * rmse_norm(rmse_value)


def misclassification_cost(y_true, y_pred, cost_fn=2.0, cost_fp=1.0):
    matrix = confusion_matrix(y_true, y_pred)
    return float(cost_fn * matrix[1, 0] + cost_fp * matrix[0, 1])


def train_test_split(n_samples, test_size=0.2, seed=42, stratify=None):
    # Kembalikan indeks train dan validasi, bukan data yang sudah diolah.
    if n_samples < 2 or not 0 < test_size < 1:
        raise ValueError("Periksa jumlah sampel dan test_size")
    rng = np.random.default_rng(seed)
    if stratify is None:
        indices = rng.permutation(n_samples)
        n_val = int(round(n_samples * test_size))
        train_idx, val_idx = indices[n_val:], indices[:n_val]
    else:
        labels = np.asarray(stratify)
        if labels.ndim != 1 or len(labels) != n_samples:
            raise ValueError("stratify harus berisi satu label per sampel")
        train_parts, val_parts = [], []
        for cls in np.unique(labels):
            indices = rng.permutation(np.where(labels == cls)[0])
            n_val = int(round(len(indices) * test_size))
            train_parts.append(indices[n_val:])
            val_parts.append(indices[:n_val])
        train_idx = np.concatenate(train_parts)
        val_idx = np.concatenate(val_parts)
    if len(train_idx) == 0 or len(val_idx) == 0:
        raise ValueError("Train atau validasi kosong")
    return np.sort(train_idx), np.sort(val_idx)


def kfold_indices(n_samples, n_splits=5, seed=42):
    if not 2 <= n_splits <= n_samples:
        raise ValueError("n_splits harus antara 2 dan jumlah sampel")
    rng = np.random.default_rng(seed)
    folds = np.array_split(rng.permutation(n_samples), n_splits)
    result = []
    for k in range(n_splits):
        val_idx = folds[k]
        train_idx = np.concatenate(folds[:k] + folds[k + 1:])
        result.append((np.sort(train_idx), np.sort(val_idx)))
    return result


def stratified_kfold_indices(y, n_splits=5, seed=42):
    labels = np.asarray(y)
    if labels.ndim != 1 or not 2 <= n_splits <= len(labels):
        raise ValueError("Periksa bentuk y dan jumlah fold")
    rng = np.random.default_rng(seed)
    fold_of = np.empty(len(labels), dtype=int)
    for cls in np.unique(labels):
        indices = rng.permutation(np.where(labels == cls)[0])
        fold_of[indices] = np.arange(len(indices)) % n_splits
    result = []
    for k in range(n_splits):
        train_idx = np.where(fold_of != k)[0]
        val_idx = np.where(fold_of == k)[0]
        if len(val_idx) == 0:
            raise ValueError("Ada fold validasi kosong")
        result.append((train_idx, val_idx))
    return result
