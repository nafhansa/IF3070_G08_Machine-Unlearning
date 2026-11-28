from collections import deque
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def plot_naive_bayes_graph(
    nb,
    feature_names,
    top_k=20,
    path=None,
):
    if not hasattr(nb, "classes_"):
        raise ValueError("Model harus di-fit sebelum membuat graf")

    feature_names = list(feature_names)

    if len(feature_names) != nb.n_features_in_:
        raise ValueError("Jumlah nama fitur tidak sesuai dengan model")

    if not isinstance(top_k, (int, np.integer)) or top_k < 1:
        raise ValueError("top_k harus berupa integer positif")

    n_show = min(top_k, len(feature_names))
    names = feature_names[:n_show]

    fig, ax = plt.subplots(figsize=(12, 9))

    # Fitur diletakkan melingkar di sekitar node kelas.
    angles = np.linspace(
        0,
        2 * np.pi,
        n_show,
        endpoint=False,
    )

    for i, name in enumerate(names):
        x = 3 * np.cos(angles[i])
        y = 3 * np.sin(angles[i])

        ax.annotate(
            "",
            xy=(x, y),
            xytext=(0, 0),
            arrowprops={
                "arrowstyle": "->",
                "color": "gray",
                "shrinkA": 30,
                "shrinkB": 30,
            },
        )

        ax.text(
            x,
            y,
            str(name),
            ha="center",
            va="center",
            bbox={
                "boxstyle": "round,pad=0.5",
                "facecolor": "lightblue",
                "edgecolor": "gray",
            },
        )

    ax.text(
        0,
        0,
        "Kelas",
        ha="center",
        va="center",
        bbox={
            "boxstyle": "round,pad=0.7",
            "facecolor": "salmon",
            "edgecolor": "gray",
        },
    )

    title = "Struktur Naive Bayes"
    if n_show < len(feature_names):
        title += f" ({n_show} fitur pertama)"

    ax.set_title(title)
    ax.set_xlim(-4.5, 4.5)
    ax.set_ylim(-4, 4)
    ax.set_aspect("equal")
    ax.axis("off")
    fig.tight_layout()

    if path is not None:
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(path, dpi=200, bbox_inches="tight")

    return fig


# ---------------------------------------------------------------------- #
# Bonus DTL
# ---------------------------------------------------------------------- #
def plot_tree(tree, top_n: int = 15, path=None, figsize=(18, 9)):
    """
    Gambar pohon C4.5. Hanya `top_n` simpul pertama (urutan BFS dari akar) yang digambar;
    anak dari simpul ke-N ke atas diringkas menjadi "...". Warna daun: merah = phishing, hijau = legit.
    """
    root = tree.root_
    order, q = [], deque([root])
    while q and len(order) < top_n:
        n = q.popleft()
        order.append(n)
        q.extend(n.children)
    shown = {id(n) for n in order}
    # posisi: x berdasarkan urutan daun dalam subtree yang ditampilkan, y = -depth
    pos, counter = {}, [0]

    def layout(n):
        kids = [c for c in n.children if id(c) in shown]
        if not kids:
            pos[id(n)] = (counter[0], -n.depth)
            counter[0] += 1
        else:
            for c in kids:
                layout(c)
            xs = [pos[id(c)][0] for c in kids]
            pos[id(n)] = (np.mean(xs), -n.depth)

    layout(root)
    fig, ax = plt.subplots(figsize=figsize)
    for n in order:
        x, y = pos[id(n)]
        for b, c in enumerate(n.children):
            if id(c) in shown:
                cx, cy = pos[id(c)]
                ax.plot([x, cx], [y, cy], color="#999", lw=1, zorder=1)
                ax.text((x + cx) / 2, (y + cy) / 2, tree.branch_label(n, b).split(" ", 1)[1], fontsize=7,
                        ha="center", va="center", bbox=dict(fc="white", ec="none", alpha=0.8))
        p = tree._leaf_proba(n)
        if n.is_leaf or not any(id(c) in shown for c in n.children):
            label = f"{'phishing' if p.argmax() == 1 else 'legit'}\np={p.max():.2f}\nn={n.n_weight:.0f}"
            if not n.is_leaf:
                label = "...\n" + label
            color = "#f4a6a6" if p.argmax() == 1 else "#a6e3b0"
        else:
            label = f"{tree.feature_names_[n.feature]}\nn={n.n_weight:.0f}"
            color = "#cfe0fc"
        ax.text(x, y, label, ha="center", va="center", fontsize=8, zorder=2,
                bbox=dict(boxstyle="round,pad=0.4", fc=color, ec="#555"))
    ax.set_title(f"Pohon C4.5 (top-{top_n} simpul, kedalaman total {tree.get_depth()}, {tree.get_n_leaves()} daun)")
    ax.axis("off")
    fig.tight_layout()
    if path:
        fig.savefig(path, dpi=150)
    return fig
