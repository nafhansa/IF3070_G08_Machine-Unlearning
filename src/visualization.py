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