"""
Buat docs/diagram_alur_kerja.png: diagram keterhubungan pekerjaan antaranggota.
Jalankan: python tools/make_diagram.py
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]

LANES = ["Leader\n(M. Faris Daffa)", "Anggota A", "Anggota B", "Anggota C", "Anggota D"]
LANE_SUB = ["DTL C4.5", "Logistic Regression", "KNN + data klasifikasi", "Naive Bayes + utilitas + laporan",
            "Linear Regression + data regresi"]
PHASES = [("Fase 0\n17-18 Nov", "Baseline & onboarding"), ("Fase 1\n19-23 Nov", "Pahami & jalankan"),
          ("Fase 2\n24-28 Nov", "Eksplorasi & bonus"), ("Fase 3\n29 Nov-1 Des", "Integrasi & freeze"),
          ("Fase 4\n2-3 Des", "Laporan & rilis")]
COLORS = {0: "#fde2e4", 1: "#e2ece9", 2: "#dfe7fd", 3: "#fff1e6", 4: "#e8e8f8"}

# (id, lane, fase, teks)
TASKS = [
    ("L0", 0, 0, "Baseline lengkap\n(kode, notebook, docs)\n✔ SUDAH → dibagikan\nke semua anggota"),
    ("S0", 1, 0, "Setup env + baca\nREADME/CONSTRAINT/\nCHECKLIST"),
    ("S1", 2, 0, "Setup env + baca\nREADME/CONSTRAINT/\nCHECKLIST"),
    ("S2", 3, 0, "Setup env + baca\nREADME/CONSTRAINT/\nCHECKLIST"),
    ("S3", 4, 0, "Setup env + baca\nREADME/CONSTRAINT/\nCHECKLIST"),

    ("U", 3, 1, "C1 utilitas: metrics.py,\nbase.py (save/load), tests\n→ dipakai SEMUA model"),
    ("PK", 2, 1, "B1 Data Underst. &\nPreparation klasifikasi\n(preprocessing.py)"),
    ("PR", 4, 1, "D1 Data Underst. &\nPreparation regresi\n(PlayerPreprocessor)"),
    ("M1", 0, 1, "L1 pahami & rapikan\nC4.5 (decision_tree.py)"),
    ("M2", 1, 1, "A1 pahami LogReg\nL1/L2/EN"),

    ("M3", 2, 2, "B2 KNN: tuning k,\nbobot fitur, tie-break"),
    ("M4", 3, 2, "C2 Naive Bayes +\nbonus graf NB"),
    ("M5", 4, 2, "D2 LinReg GD + L1/L2\n+ bonus optimizer"),
    ("B1", 0, 2, "L2 tuning C4.5 +\nbonus gambar top-N"),
    ("B2", 1, 2, "A2 bonus video kontur\n+ Adam + cost-sensitive"),

    ("NK", 2, 3, "B3 integrasi notebook\nklasifikasi"),
    ("NR", 4, 3, "D3 integrasi notebook\nregresi"),
    ("SUB", 0, 3, "L3 pilih model final,\nsubmit Kaggle, cek MD5\n(FREEZE 1 Des)"),
    ("DR1", 1, 3, "A3 draf bab LogReg\n+ cost-sensitive"),
    ("DR2", 3, 3, "C3 kumpulkan draf\nsemua bab laporan"),

    ("LAP", 3, 4, "C4 laporan PDF +\nREADME + form AI"),
    ("REL", 0, 4, "L4 review akhir, repo PUBLIC\n→ NIM terkecil (18224009):\nrelease v1.0 + Edunex\n≤ 3 Des 22.22"),
]
DEPS = [("U", "M3"), ("U", "M4"), ("U", "M5"), ("U", "B1"), ("U", "B2"),
        ("PK", "M3"), ("PK", "M4"), ("PK", "B1"), ("PK", "B2"), ("PR", "M5"),
        ("M1", "B1"), ("M2", "B2"),
        ("M3", "NK"), ("M4", "NK"), ("B1", "NK"), ("B2", "NK"), ("M5", "NR"),
        ("NK", "SUB"), ("NR", "SUB"), ("B2", "DR1"), ("DR1", "DR2"),
        ("SUB", "LAP"), ("DR2", "LAP"), ("LAP", "REL")]

W, H = 3.0, 1.3           # ukuran kotak
DX, DY = 5.4, 2.4         # jarak antar fase / lane (lorong antar kolom = DX - W = 2.4)
fig, ax = plt.subplots(figsize=(30, 15.5))
x0, y0 = 4.6, 0.0
ARROW_COLORS = ["#c0392b", "#16a085", "#2c6fbb", "#d35400", "#7d3c98"]   # warna panah = lane asal

pos = {tid: (x0 + phase * DX, y0 - lane * DY) for tid, lane, phase, _ in TASKS}
lane_of = {tid: lane for tid, lane, _, _ in TASKS}
phase_of = {tid: phase for tid, _, phase, _ in TASKS}

# swimlane
for i, (name, sub) in enumerate(zip(LANES, LANE_SUB)):
    y = y0 - i * DY
    ax.add_patch(plt.Rectangle((-0.3, y - DY / 2), x0 + 5 * DX - 0.3, DY, color=COLORS[i], alpha=0.55, zorder=0))
    ax.text(0.1, y + 0.2, name, fontsize=12.5, fontweight="bold", va="center")
    ax.text(0.1, y - 0.45, sub, fontsize=9.5, style="italic", va="center", color="#333")
for j, (ph, desc) in enumerate(PHASES):
    x = x0 + j * DX
    ax.text(x, y0 + 1.75, ph, ha="center", fontsize=12.5, fontweight="bold")
    ax.text(x, y0 + 1.2, desc, ha="center", fontsize=10, color="#444")
    ax.axvline(x - DX / 2, color="#bbb", lw=0.8, ls=":", zorder=0)

# ---- titik keluar/masuk: panah yang keluar/masuk sisi yang sama disebar agar tidak menumpuk
def spread(n, k):
    return 0.0 if n == 1 else (H * 0.7) * (0.5 - k / (n - 1))

out_edges = {t: sorted([d for d in DEPS if d[0] == t], key=lambda d: lane_of[d[1]]) for t in pos}
in_edges = {t: sorted([d for d in DEPS if d[1] == t], key=lambda d: lane_of[d[0]]) for t in pos}

same_col = [d for d in DEPS if phase_of[d[0]] == phase_of[d[1]]]

# ---- jalur lorong: setiap panah lintas-lane di satu lorong mendapat posisi x sendiri
gutters = {}
for d in DEPS:
    if phase_of[d[1]] > phase_of[d[0]] and lane_of[d[0]] != lane_of[d[1]]:
        gutters.setdefault(phase_of[d[0]], []).append(d)
gx = {}
for ph, ds in gutters.items():
    ds.sort(key=lambda d: (lane_of[d[1]] - lane_of[d[0]] > 0, lane_of[d[0]], lane_of[d[1]]))
    n_same = sum(1 for d in same_col if phase_of[d[0]] == ph)
    left, right = x0 + ph * DX + W / 2 + 0.35 + 0.28 * n_same, x0 + (ph + 1) * DX - W / 2 - 0.35
    for k, d in enumerate(ds):
        gx[d] = left + (right - left) * (k + 0.5) / len(ds)

from matplotlib.path import Path  # noqa: E402
for d in DEPS:
    a_, b_ = d
    (xa, ya), (xb, yb) = pos[a_], pos[b_]
    color = ARROW_COLORS[lane_of[a_]]
    if phase_of[b_] == phase_of[a_]:                        # satu kolom
        lo, hi = sorted([lane_of[a_], lane_of[b_]])
        blocked = any(phase_of[t] == phase_of[a_] and lo < lane_of[t] < hi for t in pos)
        if not blocked:                                     # jalur kosong: lurus vertikal
            up = yb > ya
            pts = [(xa, ya + (H / 2 if up else -H / 2)), (xb, yb - (H / 2 if up else -H / 2))]
        else:                                               # ada kotak di tengah: lewat lorong kanan
            k = same_col.index(d)
            g = xa + W / 2 + 0.3 + 0.28 * k
            sy = ya + spread(len(out_edges[a_]), out_edges[a_].index(d))
            ty = yb + spread(len(in_edges[b_]), in_edges[b_].index(d))
            if len(in_edges[b_]) == 1 and out_edges[b_]:       # sisi kanan juga dipakai panah keluar
                ty = yb + 0.3 * H
            pts = [(xa + W / 2, sy), (g, sy), (g, ty), (xb + W / 2, ty)]
    else:
        sy = ya + spread(len(out_edges[a_]), out_edges[a_].index(d))
        ty = yb + spread(len(in_edges[b_]), in_edges[b_].index(d))
        sx, tx = xa + W / 2, xb - W / 2
        if abs(sy - ty) < 1e-9:
            pts = [(sx, sy), (tx, ty)]
        else:                                               # siku: kanan -> lorong -> kanan
            g = gx.get(d, (sx + tx) / 2)
            pts = [(sx, sy), (g, sy), (g, ty), (tx, ty)]
    path = Path(pts, [Path.MOVETO] + [Path.LINETO] * (len(pts) - 1))
    ax.add_patch(FancyArrowPatch(path=path, arrowstyle="-|>", mutation_scale=15, lw=1.6, color=color,
                                 zorder=1, alpha=0.9, joinstyle="round", capstyle="round"))

for tid, lane, phase, text in TASKS:
    x, y = pos[tid]
    special = tid in ("L0", "SUB", "REL")
    ax.add_patch(FancyBboxPatch((x - W / 2, y - H / 2), W, H, boxstyle="round,pad=0.05,rounding_size=0.15",
                                fc="#ffffff" if not special else "#ffe08a", ec="#333", lw=1.4 if special else 1, zorder=2))
    ax.text(x, y, text, ha="center", va="center", fontsize=9.5, zorder=3)

ax.text(x0 + 2 * DX, y0 - 5 * DY + 0.45,
        "Panah A → B = B membutuhkan hasil/kode A. Kerjakan kotak paling kiri dulu. Kotak kuning = titik kritis "
        "(baseline, freeze submisi, rilis).\nUtilitas (C1) & preprocessing (B1, D1) adalah fondasi: model lain baru "
        "boleh diubah setelah keduanya stabil. Warna panah = lane asal. Lihat PANDUAN.md & CHECKLIST.md untuk detail.",
        ha="center", fontsize=10.5, color="#222")
ax.set_xlim(-0.4, x0 + 4 * DX + DX / 2 + 0.2)
ax.set_ylim(y0 - 5 * DY - 0.1, y0 + 2.3)
ax.axis("off")
ax.set_title("Alur & Dependensi Pekerjaan — Tubes 2 IF3070 G08 Machine Unlearning (deadline Kamis 3 Des 2026 22.22 WIB)",
             fontsize=15, fontweight="bold", pad=10)
out = ROOT / "docs" / "diagram_alur_kerja.png"
fig.savefig(out, dpi=110, bbox_inches="tight")
print("ditulis:", out)
