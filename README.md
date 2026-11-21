# IF3070_G08_MachineUnlearning

Tugas Besar 2 **IF3070 Dasar Inteligensi Artifisial** 2026/2027 · *Supervised Learning*

Repository ini berisi implementasi **from scratch** (NumPy) untuk dua sistem milik GOATBANGET™:

1. **Deteksi situs phishing** (klasifikasi, metrik ROC-AUC). Model: KNN, Decision Tree C4.5, Logistic Regression (L1/L2/Elastic Net), Naive Bayes.
2. **Prediksi rating pemain sepak bola** (regresi, metrik RMSE). Model: Linear Regression (gradient descent, L1/L2), dengan normal equation sebagai pembanding.

Setiap model dibandingkan dengan scikit-learn, bisa di-*save*/*load*, dan dipakai untuk submisi Kaggle.

## Hasil singkat (5-fold CV)

| Task        | Model submisi                                        | CV                 | Model pesaing                                             |
| ----------- | ---------------------------------------------------- | ------------------ | --------------------------------------------------------- |
| Klasifikasi | KNN (k=21, Manhattan, bobot jarak + bobot fitur AUC) | **ROC-AUC 0.9876** | LogReg Elastic Net 0.9871 · C4.5 0.97 · Naive Bayes 0.965 |
| Regresi     | Linear Regression GD-Adam + interaksi atribut×posisi | **RMSE 0.425**     | tanpa interaksi 1.28 · KNN Regressor 2.07                 |

Bonus yang sudah diimplementasikan:
* gambar pohon top-N
* video kontur log-loss
* graf Naive Bayes
* optimizer Momentum/Adam/LR-decay
* cost-sensitive classification (FN = 2×FP)

## Struktur

```
src/            source code
  models/         model from scratch: knn, decision_tree (C4.5), logistic_regression,
                  naive_bayes, linear_regression, optimizers, base (save/load)
  preprocessing.py, metrics.py, visualization.py
  tubes2_klasifikasi.ipynb, tubes2_regresi.ipynb   <- notebook utama (template asisten)
data/           dataset Kaggle (klasifikasi/, regresi/)
output/         hasil run: submissions/*.csv, models/*.pkl, figures/
docs/           laporan PDF + diagram alur kerja
tests/          uji kebenaran model (vs contoh slide & sklearn)
tools/          skrip bantu (run_all.sh, generator notebook, diagram)
instruction/    spek (md + pdf), deskripsi Kaggle, template notebook asisten,
                materi_kelas/ (slide 08-12), transkrip_video/, transkrip_dtl/
```

### Peta dokumen: mulai dari mana?

| Urutan | File | Isi | Wajib? |
| --- | --- | --- | --- |
| 1 | [README.md](README.md) | Gambaran singkat (ini) | Wajib |
| 2 | [CONSTRAINT.md](CONSTRAINT.md) | Aturan yang tidak boleh dilanggar | Wajib |
| 3 | [CHECKLIST.md](CHECKLIST.md) | Tugasmu, pembagian kerja, timeline, eksplorasi | Wajib |
| 4 | [PANDUAN.md](PANDUAN.md) | Arsitektur kode, keputusan desain, setup, Git, submisi, laporan | Rujukan |
| 5 | [MATERI.md](MATERI.md) | Ringkasan teori kuliah; baca bagian yang terkait tugasmu | Rujukan |

## Setup & menjalankan

Kebutuhan: **Python 3.12**.

```bash
python3.12 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt

python tests/test_models.py        # uji kebenaran model -> "Semua 14 test lulus."
bash tools/run_all.sh              # jalankan kedua notebook dari awal + cetak MD5 submisi (±7 menit)
```

Atau buka `src/tubes2_klasifikasi.ipynb` / `src/tubes2_regresi.ipynb` di Jupyter, lalu **Restart & Run All**. File submisi tersimpan di `output/submissions/`.

### Reproducibility
Seed tetap (42), KNN/C4.5 deterministik, dan Linear Regression final memakai full-batch GD. Menjalankan ulang notebook harus menghasilkan file submisi dengan MD5 berikut:

| File                                            | MD5                                |
| ----------------------------------------------- | ---------------------------------- |
| `output/submissions/submission_klasifikasi.csv` | `0d3f22aca92688997b3b6e3219e1e6eb` |
| `output/submissions/submission_regresi.csv`     | `508cf5adb222366bffd29a9af17ad3de` |

### Riwayat submisi Kaggle

| Tanggal             | Task        | File (MD5)  | CV          | Public LB | Final? |
| ------------------- | ----------- | ----------- | ----------- | --------- | ------ |
| *(isi saat submit)* | Klasifikasi | `0d3f22ac…` | AUC 0.9876  |           |        |
| *(isi saat submit)* | Regresi     | `508cf5ad…` | RMSE 0.4248 |           |        |

## Pembagian tugas

| Nama           | NIM      | Tugas                                                                                                        |
| -------------- | -------- | ------------------------------------------------------------------------------------------------------------ |
| M. Faris Daffa | 18224025 | Leader; DTL C4.5 from scratch + pruning; bonus visualisasi pohon; baseline & integrasi; submisi Kaggle final |
| *(isi)*        |          | Anggota A: Logistic Regression (L1/L2/Elastic Net); bonus video kontur, optimizer, cost-sensitive            |
| *(isi)*        |          | Anggota B: KNN; Data Understanding & Preparation klasifikasi; notebook klasifikasi                           |
| *(isi)*        |          | Anggota C: Naive Bayes; metrik & utilitas; bonus graf NB; laporan & README                                   |
| *(isi)*        |          | Anggota D: Linear Regression; Data Understanding & Preparation regresi; notebook regresi                     |

Anggota: 18224009, 18224016, 18224025, 18224027, 18224096. Rincian ada di [CHECKLIST.md](CHECKLIST.md).

## Referensi utama
Slide kuliah IF3070 (Materi 08–12), video IF3270 DTL (N. U. Maulidevi), video modul Logistic Regression/Bayes/Perceptron (M. L. Khodra). Referensi luar dicantumkan di komentar kode dan di [MATERI.md](MATERI.md) §14.
