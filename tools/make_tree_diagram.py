"""
Buat docs/diagram_pohon_tugas.png: dekomposisi pekerjaan dari atas ke bawah (objective -> notebook -> langkah),
dengan warna unik per orang supaya setiap anggota cukup mencari warnanya sendiri.
Jalankan: python tools/make_tree_diagram.py
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import FancyBboxPatch, Patch  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "diagram_pohon_tugas.png"

# ---------------------------------------------------------------- warna per orang
PEOPLE = {
    "L": ("Leader · M. Faris Daffa", "C4.5, integrasi, submit", "#a9def9"),   # biru muda
    "A": ("Anggota A", "Logistic Regression", "#cdb4f6"),                       # ungu
    "B": ("Anggota B", "KNN + data klasifikasi", "#ffe17a"),                    # kuning
    "C": ("Anggota C", "Naive Bayes + utilitas + laporan", "#ffbf8a"),          # oranye
    "D": ("Anggota D", "Linear Regression + data regresi", "#a8e6b4"),          # hijau
    "S": ("Bersama", "semua anggota", "#ffb3d1"),                               # pink
}
STRUCT = "#e9ecef"   # node struktur (objective / cabang)

# ---------------------------------------------------------------- node: id -> (x, y, pemilik, teks)
X1 = [21, 34, 47, 60]            # kolom model notebook klasifikasi
X2 = [74, 87, 100]               # kolom notebook regresi
N1, N2, XF, XR = 40.5, 87, 7, 115
Y = {0: 0, 1: -12, 2: -25, 3: -35, 4: -45, 5: -57, 6: -68, 7: -80, 8: -91, 9: -102}

N = {
    "root": (61, Y[0], None, "TUBES 2 IF3070 SELESAI\nNotebook + Kaggle + laporan + rilis\n≤ Kamis 3 Des 2026, 22.22 WIB"),

    # ---- level 1
    "F": (XF, Y[1], None, "FONDASI\n(dipakai semua)"),
    "K": (N1, Y[1], None, "NOTEBOOK 1 · KLASIFIKASI\nDeteksi phishing · ROC-AUC\nsrc/tubes2_klasifikasi.ipynb"),
    "R": (N2, Y[1], None, "NOTEBOOK 2 · REGRESI\nRating pemain · RMSE\nsrc/tubes2_regresi.ipynb"),
    "P": (XR, Y[1], None, "LAPORAN & RILIS\ndocs/ + GitHub + Edunex"),

    # ---- fondasi
    "F1": (XF, Y[2], "S", "Setup .venv, jalankan test,\nbaca README / CONSTRAINT /\nCHECKLIST / PANDUAN"),
    "F2": (XF, Y[3], "C", "Utilitas: metrics.py,\nbase.py (save/load),\ntests/test_models.py"),

    # ---- notebook klasifikasi (alur dari atas ke bawah)
    "K1": (N1, Y[2], "B", "1. Data Understanding\n81 fitur · missing · nilai -1\n· pencilan · fitur terkuat"),
    "K2": (N1, Y[3], "B", "2. Split 80/20 stratified\n+ 5-fold CV (seed 42)"),
    "K3": (N1, Y[4], "B", "3. Preprocessing\nPhishingPreprocessor\n4 mode: tree/nb/knn/linear"),
    "KL": (X1[0], Y[5], "L", "4a. C4.5\ngain ratio · missing\nbobot pecahan"),
    "KA": (X1[1], Y[5], "A", "4b. Logistic Regression\nSGA · L1 / L2 /\nElastic Net"),
    "KB": (X1[2], Y[5], "B", "4c. KNN (model final)\nManhattan · bobot jarak\n· bobot fitur AUC"),
    "KC": (X1[3], Y[5], "C", "4d. Naive Bayes\nbinned 20 · Laplace\n· log-space"),
    "KL2": (X1[0], Y[6], "L", "Pruning REP + rule\n+ BONUS gambar\npohon top-N  [E6]"),
    "KA2": (X1[1], Y[6], "A", "BONUS video kontur,\nAdam, cost-sensitive\n+ interaksi [E4, E5]"),
    "KB2": (X1[2], Y[6], "B", "Tuning k, tie-break,\nindikator kosong\n[E1, E2, E3, E11]"),
    "KC2": (X1[3], Y[6], "C", "BONUS graf NB\n+ bin per fitur [E7]"),
    "K5": (N1, Y[7], "B", "5. Evaluasi: tabel 4 model\n+ banding sklearn\n+ confusion matrix"),
    "K6": (N1, Y[8], "L", "6. Pilih model (CV),\nsubmit Kaggle, cek MD5"),

    # ---- notebook regresi
    "R1": (N2, Y[2], "D", "1. Data Understanding\n48 fitur · efek per posisi\n· noise level_liga · missing"),
    "R2": (N2, Y[3], "D", "2. Split 80/20\n+ 5-fold CV (seed 42)"),
    "R3": (N2, Y[4], "D", "3. Preprocessing\nPlayerPreprocessor: log uang,\nimputasi, interaksi × posisi"),
    "RA": (X2[0], Y[5], "A", "Penebak posisi\n(softmax = LogReg\nmultikelas)  [E8]"),
    "RD": (X2[1], Y[5], "D", "Fitur uang tak-linear\n[E12, prioritas #1]\n+ bonus reputasi [E13]"),
    "RB": (X2[2], Y[5], "B", "Imputasi KNN vs\nregresi untuk\nkolom uang  [E16]"),
    "R4": (N2, Y[6], "D", "4. Linear Regression\nGD (Adam + lr decay)\n+ L1/L2 + BONUS optimizer"),
    "RL": (X2[0], Y[7], "L", "Diagnosa: C4.5 pada\nresidual → segmen\nyang sering salah [E15]"),
    "R5": (X2[1], Y[7], "D", "5. Evaluasi: MAE/RMSE/R²\n+ banding sklearn\n+ plot residual"),
    "RC": (X2[2], Y[7], "C", "Rincian error per\nsegmen otomatis\n+ uji pembulatan [E17]"),
    "R6": (N2, Y[8], "L", "6. Pilih model (CV),\nsubmit Kaggle, cek MD5"),

    # ---- laporan & rilis
    "P1": (XR, Y[6], "S", "Draf bab masing-masing\n(penjelasan kode +\neksperimen) ≤ 1 Des"),
    "P2": (XR, Y[7], "C", "Gabung laporan PDF\n+ README\n+ form Generative AI"),
    "P3": (XR, Y[8], "L", "Review akhir,\nrepo jadi PUBLIC"),
    "P4": (XR, Y[9], "S", "Release v1.0 + Edunex\noleh NIM terkecil\n(18224009)"),
}

# (induk, anak): garis siku dari bawah induk ke atas anak
EDGES = [
    ("root", "F"), ("root", "K"), ("root", "R"), ("root", "P"),
    ("F", "F1"), ("F1", "F2"),
    ("K", "K1"), ("K1", "K2"), ("K2", "K3"),
    ("K3", "KL"), ("K3", "KA"), ("K3", "KB"), ("K3", "KC"),
    ("KL", "KL2"), ("KA", "KA2"), ("KB", "KB2"), ("KC", "KC2"),
    ("KL2", "K5"), ("KA2", "K5"), ("KB2", "K5"), ("KC2", "K5"), ("K5", "K6"),
    ("R", "R1"), ("R1", "R2"), ("R2", "R3"),
    ("R3", "RA"), ("R3", "RD"), ("R3", "RB"),
    ("RA", "R4"), ("RD", "R4"), ("RB", "R4"),
    ("R4", "RL"), ("R4", "R5"), ("R4", "RC"),
    ("RL", "R6"), ("R5", "R6"), ("RC", "R6"),
    ("P", "P1"), ("P1", "P2"), ("P2", "P3"), ("P3", "P4"),
]

W, H = 11.6, 7.4
fig, ax = plt.subplots(figsize=(40, 39))
ax.set_xlim(-1, 123)
ax.set_ylim(-110, 13)
ax.axis("off")


def box(nid):
    x, y, who, text = N[nid]
    struct = who is None
    w = W + (5 if nid == "root" else 4 if struct else 0)
    fill = STRUCT if struct else PEOPLE[who][2]
    ax.add_patch(FancyBboxPatch((x - w / 2, y - H / 2), w, H, boxstyle="round,pad=0.25,rounding_size=0.9",
                                fc=fill, ec="#495057" if struct else "#6c757d", lw=2.4 if struct else 1.4, zorder=3))
    lines = text.split("\n")
    ax.text(x, y + (0.45 if not struct else 0), "\n".join(lines), ha="center", va="center", zorder=4,
            fontsize=17 if nid == "root" else 15 if struct else 13.2, linespacing=1.35,
            fontweight="bold" if struct else "normal")
    if not struct:   # label pemilik kecil di pojok bawah (agar tetap terbaca saat dicetak hitam-putih)
        ax.text(x, y - H / 2 + 0.75, PEOPLE[who][0], ha="center", va="center", fontsize=10.5,
                style="italic", color="#343a40", zorder=4)


def edge(a, b):
    xa, ya, *_ = N[a]
    xb, yb, *_ = N[b]
    y_top, y_bot = ya - H / 2 - 0.25, yb + H / 2 + 0.25
    ym = y_bot + 1.4 if abs(xa - xb) > 0.1 else (y_top + y_bot) / 2
    kw = dict(color="#6c757d", lw=2.0, zorder=1, solid_capstyle="round")
    ax.plot([xa, xa, xb, xb], [y_top, ym, ym, y_bot + 0.6], **kw)
    ax.annotate("", xy=(xb, y_bot), xytext=(xb, y_bot + 0.7),
                arrowprops=dict(arrowstyle="-|>", color="#6c757d", lw=2.0, mutation_scale=22), zorder=2)


for a, b in EDGES:
    edge(a, b)
for nid in N:
    box(nid)

# ---------------------------------------------------------------- judul + legenda
ax.text(61, 11.2, "Pohon Pekerjaan Tubes 2 · Kelompok G08 Machine Unlearning", ha="center", fontsize=28,
        fontweight="bold")
ax.text(61, 8.6, "Dibaca dari atas ke bawah. Cari warnamu sendiri; kode [E..] = ide eksplorasi di PANDUAN.md §10.2 "
                 "dan CHECKLIST.md Fase 4.", ha="center", fontsize=15, color="#495057")
handles = [Patch(fc=c, ec="#6c757d", label=f"{n} — {s}") for n, s, c in PEOPLE.values()]
handles.append(Patch(fc=STRUCT, ec="#495057", label="Struktur (objective / cabang)"))
ax.legend(handles=handles, loc="upper left", bbox_to_anchor=(0.005, 0.985), fontsize=14.5, frameon=True,
          title="Warna = pemilik tugas", title_fontsize=15.5, borderpad=1, labelspacing=0.8)

OUT.parent.mkdir(exist_ok=True)
fig.savefig(OUT, dpi=110, bbox_inches="tight", facecolor="white")
print("ditulis:", OUT)
