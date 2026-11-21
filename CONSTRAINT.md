# CONSTRAINT.md — Aturan yang Wajib Dipatuhi

> **Untuk siapa:** semua anggota G08 dan AI assistant yang membantu mereka.
> **Sumber:** spek resmi (`instruction/spek.md` / `instruction/spek tubes ai 2.pdf`, versi 1.2 – 16/11/2026), halaman Kaggle (`instruction/desc klasifikasi.md`, `instruction/desc regresi.md`), dan template notebook asisten.
> **Cara pakai:** sebelum menulis kode atau mengubah sesuatu, cek tabel di bawah. Kalau ragu, **jangan dilanggar**; tanya leader atau ajukan pertanyaan di QnA Teams.

Setiap aturan diberi kode (mis. `M-03`) supaya mudah dirujuk di PR/diskusi. Tingkatannya:
* **WAJIB**: melanggar berarti nilai berkurang atau bonus hangus.
* **DILARANG**: melanggar berarti nilai berkurang, bahkan bisa nilai E.
* **BOLEH**: diizinkan, dengan syarat yang tertulis.

---

## 1. Integritas akademik (paling berat)

- **I-01**: **DILARANG** plagiarisme, meminta, atau memberi kode/laporan ke kelompok lain. Hukumannya **nilai E untuk seluruh anggota yang terlibat**.
  - Dasar: Spek: Aturan 4
- **I-02**: **DILARANG** beralasan "itu buatan LLM" untuk membela kesalahan atau kemiripan. *Alasan penggunaan LLM tidak dapat diterima.*
  - Dasar: Spek: Aturan 4
- **I-03**: **WAJIB** mengisi **Form Penggunaan Generative AI** (Halaman 19 Panduan AI ITB) **sejujur-jujurnya** sebagai lampiran laporan. Proyek ini memakai AI assistant untuk membuat baseline, dokumentasi, dan arahan, jadi **itu harus dideklarasikan**. Ketidakjujuran akan ditindaklanjuti sesuai hukum yang berlaku.
  - Dasar: Spek: Deliverables 3
- **I-04**: **WAJIB** setiap anggota **memahami** kode bagiannya sendiri dan bisa menjelaskannya (laporan berisi penjelasan fungsi/kelas + source code). Jangan menyalin tanpa paham.
  - Dasar: Spek: Deliverables 3
- **I-05**: **WAJIB** mencantumkan sumber dalam bentuk **komentar di kode** *dan* di bagian **Referensi laporan** bila memakai atau mengadaptasi metode dari Internet.
  - Dasar: Spek: Aturan 2
- **I-06**: Pertanyaan ke asisten **hanya** lewat komentar di unggahan Tugas Besar di Teams. Pertanyaan personal tidak dijawab.
  - Dasar: Spek: Aturan 3

---

## 2. Algoritma & library

- **M-01**: **WAJIB** implementasi **from scratch**: (a) **DTL** salah satu dari ID3/C4.5/CART, yang minimal menangani **numerik + kategorikal + null**. Kelompok memilih **C4.5**.
  - Dasar: Spek Cakupan 1
- **M-02**: **WAJIB** from scratch: **Logistic Regression** dengan **L1, L2, Elastic Net** *atau* **KNN**. Kelompok mengerjakan **keduanya**.
  - Dasar: Spek Cakupan 2
- **M-03**: **WAJIB** from scratch: **Naive Bayes**.
  - Dasar: Spek Cakupan 3
- **M-04**: **WAJIB** from scratch: **Linear Regression** untuk task regresi, dengan ketentuan: (a) pelatihan memakai **gradient descent (batch atau mini-batch)**, normal equation **hanya boleh sebagai pembanding**; (b) regularisasi **L2 dan L1**; (c) **standarisasi fitur numerik** sebelum training, dan **bias/intercept tidak diregularisasi**.
  - Dasar: Spek Cakupan 5a-c
- **M-05**: Implementasi from scratch **hanya boleh** memakai library untuk **perhitungan matematika**: NumPy (dan sejenisnya, mis. `math`, `scipy.special` untuk fungsi matematika). **DILARANG** memakai `sklearn` atau library ML lain di dalam `src/models/`.
  - Dasar: Spek Cakupan, paragraf terakhir
- **M-06**: Library lain yang ragu-ragu → **konfirmasi lewat QnA** sebelum dipakai.
  - Dasar: Spek
- **M-07**: **BOLEH** memakai `sklearn` untuk **preprocessing** (template: *"Preparation steps may use sklearn"*), untuk **pembanding** (Cakupan 4 & 5d), dan untuk metrik. Kelompok memilih menulis preprocessing & metrik sendiri dengan NumPy demi reproducibility.
  - Dasar: Template, spek
- **M-08**: **WAJIB** membandingkan algoritma from scratch dengan scikit-learn. DTL memakai `DecisionTreeClassifier` dengan **ID3: `criterion='entropy'`; C4.5: `criterion='entropy'` + `ccp_alpha`; CART: `criterion='gini'`**.
  - Dasar: Spek Cakupan 4
- **M-09**: **WAJIB** membandingkan Linear Regression dengan `LinearRegression`, `Ridge`, `Lasso` sklearn memakai minimal **MAE, RMSE, R²**, **disertai visualisasi** (minimal *predicted vs actual* dan *residual plot*).
  - Dasar: Spek Cakupan 5d
- **M-10**: **WAJIB** model bisa **di-save dan di-load** (implementasi bebas; kita memakai `pickle` lewat `BaseModel.save/load`).
  - Dasar: Spek Cakupan 6
- **M-11**: Implementasi **utamakan mengacu pada salindia kuliah** (`MATERI.md`). Teknik di luar slide tetap boleh, tetapi ikuti I-05.
  - Dasar: Spek Aturan 2
- **M-13**: **Prinsip slide-first** (kesepakatan kelompok, turunan M-11): bila slide punya cara untuk suatu langkah, cara slide **diimplementasikan dan diukur lebih dulu**. Teknik luar hanya dipakai bila (a) diwajibkan spek, (b) diminta bonus, atau (c) **terbukti lebih baik di 5-fold CV**, dengan perbandingannya **ditampilkan di notebook** dan referensinya dicantumkan.
  - Dasar: Spek Aturan 2
- **M-12**: Model from scratch **disarankan** berbentuk kelas (`class KNN`, dst.) yang di-*import* ke notebook.
  - Dasar: Spek

---

## 3. Data & preprocessing

- **D-01**: **WAJIB** ada tahap: **Data Cleaning** (missing, duplikat, data tidak valid), **Data Transformation** (encoding, normalisasi/standarisasi, penanganan imbalance), **Feature Selection**, **Dimensionality Reduction** (bila perlu; boleh dicoba lalu ditolak dengan alasan), **Modeling & Validation** (train-test split / k-fold).
  - Dasar: Spek: Tahapan Pengolahan Data
- **D-02**: **DILARANG** menggabungkan train dan test saat preprocessing. Preprocessing **dilakukan terpisah**: `fit` di data latih → `transform` data lain.
  - Dasar: Spek: Tahapan, kalimat terakhir
- **D-03**: **WAJIB** split train/validation **sebelum** data preparation. Statistik apa pun (median, mean, std, kuantil, batas bin, model imputasi, bobot fitur) **hanya** dihitung dari split latih. Ini juga berlaku **di dalam setiap fold** CV.
  - Dasar: Template sec. 4 & 5
- **D-04**: `test.csv` **hanya** untuk submisi Kaggle, bukan untuk tuning.
  - Dasar: Template sec. 4
- **D-05**: **DILARANG** menghapus baris `test.csv` (duplikat/outlier). Submisi harus memuat **setiap id tepat sekali**.
  - Dasar: Kaggle
- **D-06**: Kolom `id` **dibaca sebagai teks** (`dtype={'id': str}`), karena sebagian id mirip angka.
  - Dasar: Kaggle, template
- **D-07**: Setiap keputusan preparation **WAJIB** punya blok **Insight** (alasan) di notebook dan dijelaskan di laporan (*"tahap cleaning dan preprocessing beserta alasannya"*).
  - Dasar: Template, spek Deliverables

---

## 4. Kaggle & reproducibility

- **K-01**: **WAJIB** minimal **1 submisi** di Kaggle **Klasifikasi** *dan* **Regresi**.
  - Dasar: Spek Cakupan 7
- **K-02**: Format submisi: CSV kolom `id,target`. Klasifikasi: `target` = **peluang phishing 0..1** (bukan label 0/1). Regresi: `target` = angka rating.
  - Dasar: Kaggle
- **K-03**: Metrik: Klasifikasi **ROC-AUC**; Regresi **RMSE** (baseline 6.9676). Public LB = 30% test, private LB = 70% test, jadi **pilih model berdasarkan CV, bukan public LB**.
  - Dasar: Kaggle
- **K-04**: Skor bonus: `Skor = 0.7·AUC_norm + 0.3·RMSE_norm`, dengan `AUC_norm = clip((AUC−0.5)/0.5,0,1)` dan `RMSE_norm = clip(1−RMSE/6.9676,0,1)`. Bonus Kaggle: rank 1–3 = 5 poin, 4–5 = 3 poin, 6–10 = 1 poin.
  - Dasar: Kaggle, spek Bonus 1
- **K-05**: **WAJIB reproducible**: notebook yang dikumpulkan, bila dijalankan ulang oleh asisten, harus menghasilkan **nilai akhir yang sama** dengan submisi Kaggle. Bila tidak, **poin Bonus Kaggle dianulir dan poin Kaggle Submission = 0**. Konsekuensinya: seed tetap, tidak ada pengacakan tanpa seed, versi library dicatat di `requirements.txt`, dan cek **MD5** file submisi.
  - Dasar: Spek Cakupan, Bonus 1
- **K-06**: Untuk leaderboard: model yang boleh **hanya KNN, DTL, Logistic Regression, Naive Bayes from scratch, TANPA ensemble** (tidak boleh voting/averaging/stacking/boosting beberapa model).
  - Dasar: Spek Bonus 1
- **K-07**: ⚠ **Asumsi yang perlu dikonfirmasi di QnA:** daftar K-06 tidak menyebut Linear Regression, padahal spek mewajibkan submisi regresi (K-01) dan satu-satunya model regresi yang diwajibkan adalah Linear Regression from scratch (M-04). Daftar itu tampaknya sisa spek lama yang hanya punya klasifikasi. **Kelompok memakai Linear Regression from scratch** untuk submisi regresi. Cadangannya **KNNRegressor from scratch** (KNN ada di daftar resmi).
  - Dasar: Analisis spek
- **K-08**: Nama tim di leaderboard = **nama kelompok** (Machine Unlearning). Cukup 1 orang di tim Kaggle.
  - Dasar: Spek Bonus 1
- **K-09**: Model satu jenis dengan preprocessing kompleks (binning, pembobotan fitur, interaksi) **bukan ensemble**. Menggabungkan prediksi beberapa model **adalah** ensemble.
  - Dasar: Interpretasi K-06

---

## 5. Repository & pengumpulan

- **R-01**: Repo GitHub **akun pribadi**, nama **`IF3070_G08_MachineUnlearning`** (format `IF3070_GXX_NamaKelompok`). Boleh private selama pengerjaan, **WAJIB public** sebelum pengumpulan.
  - Dasar: Spek Deliverables 1
- **R-02**: Struktur wajib: `src/` (source code), `docs/` (laporan **.pdf**), `output/` (hasil run algoritma), `README.md` (deskripsi, cara setup & run, pembagian tugas).
  - Dasar: Spek Deliverables 3
- **R-03**: Laporan PDF memuat: **Cover**; **Deskripsi Persoalan** (pemahaman dataset); **Pembahasan** (penjelasan implementasi tiap algoritma + deskripsi fungsi/kelas + source code; tahap cleaning & preprocessing + alasannya; hasil & analisis perbandingan dengan pustaka memakai metrik yang sesuai + visualisasi); **Kesimpulan dan Saran**; **Pembagian tugas**; **Referensi**; **Lampiran Form Penggunaan Generative AI**.
  - Dasar: Spek Deliverables 3
- **R-04**: Commit & branching **mengikuti best practice**, disarankan **semantic commit** (`feat:`, `fix:`, `docs:`, `refactor:`, `test:`, `chore:`) agar kontribusi tiap anggota terlihat. Commit tidak dinilai langsung, tetapi menjadi bukti kontribusi.
  - Dasar: Spek Deliverables 2
- **R-05**: Pengumpulan: buat **release dengan tag `vX.Y`** (X = nomor milestone, Y = revisi mulai 0, mis. `v1.0`) **sebelum deadline**. Tautan release dikumpulkan lewat formulir **Edunex** oleh anggota dengan **NIM terkecil** (**18224009**).
  - Dasar: Spek Deliverables 4
- **R-06**: **Deadline: Kamis, 3 Desember 2026, 22.22 WIB.** Terlambat → pengurangan nilai.
  - Dasar: Spek
- **R-07**: **DILARANG** menaruh data pribadi (email, nomor HP) di repo, karena repo akan public. Cukup nama dan NIM.
  - Dasar: Kesepakatan kelompok

---

## 6. Bonus (maks. 20 poin, kerjakan **setelah** semua wajib selesai)

- **B-01**: Peringkat Kaggle
  - Poin: 1–5
  - Syarat utama: lihat K-04..K-06
  - Status baseline: submisi siap
- **B-02**: Gambar pohon DTL + parameter **top-N** percabangan
  - Poin: 2
  - Syarat utama: format bebas
  - Status baseline: `V.plot_tree(tree, top_n=...)`
- **B-03**: **Video** kontur log-loss + lintasan (θ₀, θ₁) LogReg selama training
  - Poin: 2
  - Syarat utama: harus video
  - Status baseline: `V.make_logreg_contour_video` → mp4
- **B-04**: Gambar **graf** NB: hubungan fitur dan variabel kelas
  - Poin: 2
  - Status baseline: `V.plot_naive_bayes_graph`
- **B-05**: Algoritma **optimasi model selain yang diajarkan** (untuk LogReg/KNN, NB, perbandingan, LinReg)
  - Poin: 2 per algoritma, maks. 6
  - Syarat utama: **wajib referensi**, tanpa referensi dianulir; jelaskan cara kerjanya
  - Status baseline: Momentum, Adam, LR decay (`optimizers.py`)
- **B-06**: **Cost-sensitive classification** (biaya FN = 2 × FP): jelaskan threshold, class weight, atau pendekatan lain; bandingkan biaya & metrik; ada di notebook **dan** laporan
  - Poin: 3
  - Status baseline: notebook klasifikasi sec. 11
- **B-07**: "Plis baca lorenya :) 🙏 [100 obrigado]"
  - Poin: ?
  - Syarat utama: tidak jelas (lelucon asisten); abaikan kecuali ada klarifikasi QnA
  - Status baseline: –

---

## 7. Apa yang ada di materi kelas vs di luar materi

Gunakan tabel ini untuk menentukan perlu-tidaknya **referensi** (I-05) dan apakah bisa diklaim bonus (B-05).

- **KNN, jarak Minkowski/Manhattan/Euclidean, tuning k**: ✅
  - Rujukan: Slide 09
- **Voting berbobot jarak (1/d)**: ❌ (perlu referensi)
  - Rujukan: Cunningham & Delany 2020 = ref. [21] spek
- **Pembobotan fitur KNN via AUC univariat**: ✅ konsep filter feature selection (Slide 08 hal.71); bentuk bobotnya rancangan kelompok
  - Rujukan: jelaskan di laporan
- **Naive Bayes frekuensi**: ✅
  - Rujukan: Slide 09
- **Laplace smoothing, Gaussian NB, log-space**: ❌
  - Rujukan: Mitchell 1997 bab 6; dokumentasi sklearn
- **Minimum-risk Bayes (threshold cost-sensitive)**: ✅
  - Rujukan: Video Bayes 2
- **ID3, entropy, gain, gain ratio, threshold kontinu, missing berbobot, REP, rule post-pruning**: ✅
  - Rujukan: Slide 10, video DTL
- **Reduced Error Pruning (greedy) & Rule Post-Pruning**: ✅ (dipakai)
  - Rujukan: Slide 10 hal. 36-39, video DTL-05
- **Gini / CART**: ❌
  - Rujukan: ref. [23] spek
- **Linear regression LSE, gradient descent batch/stochastic**: ✅
  - Rujukan: Slide 11, video Perceptron 2
- **Normal equation bentuk matriks**: ⚠ (LSE analitik ada)
  - Rujukan: buku statistika
- **Regularisasi L1/L2/Elastic Net**: ❌ (diminta spek)
  - Rujukan: Zou & Hastie 2005; Tibshirani 1996
- **Logistic regression MLE + SGA**: ✅
  - Rujukan: Slide 11, video LR 1–2
- **Softmax (multikelas) untuk menebak posisi**: ❌; KNN dari slide dicoba dulu (RMSE 0.4376 vs softmax 0.4248)
  - Rujukan: Bishop 2006 4.3.4
- **Momentum, Adam, LR decay**: ❌ → **bonus B-05**
  - Rujukan: Polyak 1964; Kingma & Ba 2015
- **Binning, diskretisasi, normalisasi, one-hot, PCA, imputasi prediksi, IQR outlier**: ✅
  - Rujukan: Slide 08
- **Quantile transform (berbasis peringkat)**: ❌; min-max dari slide dicoba dulu (KNN AUC 0.977 vs quantile 0.988)
  - Rujukan: dokumentasi sklearn QuantileTransformer
- **Standarisasi z-score**: ⚠ (diwajibkan spek)
  - Rujukan: –
- **Ensemble (bagging, boosting, voting)**: ❌ dan **dilarang** untuk Kaggle
  - Rujukan: K-06
