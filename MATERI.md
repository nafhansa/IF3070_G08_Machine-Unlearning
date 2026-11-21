# MATERI.md — Rangkuman Materi Kuliah untuk Tugas Besar 2

> **Untuk siapa:** anggota kelompok G08 (dan AI assistant mereka) yang ingin memahami atau mengubah kode tubes.
> **Isi:** gabungan **slide kuliah IF3070** (Materi 08–12) dan **transkrip video YouTube** (8 video modul Bu Masayu dan 9 video DTL Bu Ulfa) yang disusun **per topik**, bukan per file.
> **Aturan spek:** *"Utamakan implementasi yang mengacu pada salindia kuliah."* Jadi dokumen ini adalah **acuan utama**. Teknik di luar dokumen ini wajib diberi sumber (lihat `CONSTRAINT.md`).

Cara membaca rujukan:
* `[S08 hal.73]` = Slide Materi08 halaman PDF 73
* `[V-LR2]` = video Logistic Regression bagian 2
* `[V-DTL07]` = video DTL Bu Ulfa nomor 07

Daftar lengkap sumber ada di bagian paling bawah.

Rumus di slide asli banyak yang rusak karena OCR. Rumus di sini sudah **ditulis ulang dan dicek** terhadap contoh angka di slide, dan contoh angka itu juga diuji di `tests/test_models.py`.

**Penanda keaslian (hasil audit 18 Nov 2026):**
* Tanpa penanda = isi dari slide/video, sudah dicocokkan dengan sumbernya.
* **〔hitungan kami〕** = angka yang tidak tertulis di slide/video (mis. jawaban latihan), dihitung sendiri dan diverifikasi kode.
* **〔di luar slide〕** = pengetahuan tambahan yang tidak ada di materi kuliah. Boleh dipakai, tetapi wajib diberi referensi (`CONSTRAINT.md` I-05) dan **bukan** prioritas (spek: "utamakan salindia").

---

## Daftar Isi

1. [Gambaran besar: Supervised Learning & tipe klasifikasi](#1-gambaran-besar)
2. [CRISP-DM: metodologi data science](#2-crisp-dm)
3. [Data Understanding](#3-data-understanding)
4. [Data Preparation](#4-data-preparation)
5. [Modeling & Evaluation (skenario eksperimen, metrik)](#5-modeling--evaluation)
6. [k-Nearest Neighbor (KNN)](#6-k-nearest-neighbor-knn)
7. [Bayes Decision Theory & Naive Bayes](#7-bayes-decision-theory--naive-bayes)
8. [Decision Tree Learning (ID3, C4.5)](#8-decision-tree-learning)
9. [Linear Regression](#9-linear-regression)
10. [Logistic Regression](#10-logistic-regression)
11. [Gradient Descent (batch vs stochastic)](#11-gradient-descent)
12. [Perceptron & ANN (tidak dipakai di tubes)](#12-perceptron--ann)
13. [Peta materi → kode tubes](#13-peta-materi--kode-tubes)
14. [Daftar sumber](#14-daftar-sumber)

---

## 1. Gambaran besar

### 1.1 Supervised learning
* Kita punya **data berlabel**: pasangan (x, y). x adalah vektor fitur berdimensi d, y adalah label.
* Tugas learning adalah mencari **hipotesis h ≈ f**, yaitu fungsi yang memetakan x → y, supaya bisa menebak y untuk data yang **belum pernah dilihat** (*unseen data*) `[S11 hal.13]`.
* **Klasifikasi**: y berupa kelas/kategori, misalnya phishing vs legit. **Regresi**: y berupa nilai kontinu, misalnya rating pemain `[S08 hal.20, 28]`.

### 1.2 Tipe tugas klasifikasi `[V-Classification]`
- **Jumlah kelas yang terdefinisi**: **binary** (2 kelas) vs **multi-class** (>2)
  - Contoh: fraud / bukan fraud; jenis ikan
- **Jumlah label per data**: **single-label** vs **multi-label**
  - Contoh: satu jenis ikan; disposisi keluhan ke beberapa dinas
- **Bentuk output**: **hard** (langsung kelas) vs **soft/fuzzy** (peluang tiap kelas, jumlahnya 1)
  - Contoh: "phishing" vs "P(phishing)=0.87"

* Binary classification pasti single-label. Multi-class yang multi-label cukup disebut *multi-label*.
* **Tubes ini:** klasifikasi phishing = **binary, single-label, soft** (Kaggle meminta peluang). Rating pemain = **regresi**.

---

## 2. CRISP-DM

`[S08 hal.6-24]` Membangun sistem AI berbasis data **bukan** sekadar "data + algoritma ML". Kita butuh metodologi iteratif. Ada metodologi teknis (KDD, SEMMA) dan metodologi bisnis (**CRISP-DM**, IBM, Microsoft TDSP). Di Indonesia dipakai SKKNI No. 299/2020 dengan 21 fungsi dasar, dari *menentukan objektif bisnis* sampai *membuat laporan akhir*.

Enam fase CRISP-DM:

- **1. **Business Understanding****: tentukan tujuan bisnis, nilai situasi (sumber daya, risiko, biaya), tentukan tujuan data science, buat rencana proyek
  - Output: tujuan & kriteria sukses bisnis, tujuan & kriteria sukses DS (metrik), project plan
- **2. **Data Understanding****: kumpulkan data awal → **deskripsikan** → **eksplorasi** → **verifikasi kualitas**
  - Output: laporan deskripsi, eksplorasi, kualitas data
- **3. **Data Preparation****: **select** → **clean** → **construct** → integrate → **format**
  - Output: dataset final + alasan inklusi/eksklusi, laporan cleaning, atribut turunan
- **4. **Modeling****: pilih algoritma, bagi data, tentukan langkah eksperimen, bangun model
  - Output: model
- **5. **Evaluation****: ukur performa vs target, pilih model terbaik, review proses
  - Output: model terbaik + catatan kekurangan
- **6. **Deployment****: pasang model ke aplikasi, monitor, maintain, dispose
  - Output: aplikasi AI yang beroperasi

Contoh *business goal* vs *data science goal* `[S08 hal.19]`: "meningkatkan penjualan katalog" (bisnis) vs "memprediksi jumlah barang yang dibeli pelanggan dari histori 3 tahun + demografi" (DS).

Tujuan task `[S08 hal.4]`: **descriptive** (apa yang terjadi), **diagnostic** (kenapa), **predictive** (apa yang akan terjadi, **tubes ini**), **prescriptive** (apa yang sebaiknya dilakukan).

Metrik per jenis task `[S08 hal.20]`: regresi memakai **RMSE, MAE**; klasifikasi memakai **recall, precision, F1**; klastering memakai silhouette, DBI.

> **Di tubes:** struktur notebook template mengikuti CRISP-DM. Section 3 = Data Understanding, 5–6 = Data Preparation, 7–8 = Modeling & Evaluation.

---

## 3. Data Understanding

`[S08 hal.25-57]` Tujuannya: memahami isi data, menguji kualitas, memastikan jumlah data cukup, dan menemukan insight awal.

### 3.1 Mendeskripsikan data `[S08 hal.38]`
* Sumber data, ukuran (jumlah instance & atribut), **tipe tiap atribut** dan rentang/himpunan nilainya, serta statistik deskriptif.

### 3.2 Tipe atribut (skala pengukuran)
Dari slide `[S08 hal.39-40]` dan video `[V-DTL01]`, `[S10 hal.2-7]`:

- **Kualitatif**: tidak ada urutan; boleh direpresentasikan angka tapi bukan kuantitas
  - Tipe: **Nominal**
  - Contoh: jenis kelamin, kode pos, NIM, posisi pemain
  - Statistik yang sah: modus
- **Kualitatif**: 2 nilai. *Simetrik* (sama penting, mis. gender) atau *asimetrik* (satu nilai lebih penting, mis. HIV positif)
  - Tipe: **Binary**
  - Contoh: `alamat_ip` 0/1
  - Statistik yang sah: modus, proporsi
- **Kualitatif**: ada urutan tapi jarak antar nilai tidak bermakna
  - Tipe: **Ordinal**
  - Contoh: ukuran minuman S/M/L, nilai A–E, skala Likert 1–5
  - Statistik yang sah: median, modus
- **Kuantitatif**: jarak bermakna, nol bukan "tidak ada"
  - Tipe: **Interval**
  - Contoh: suhu °C, tahun
  - Statistik yang sah: mean, median, variance
- **Kuantitatif**: nol berarti "tidak ada", rasio bermakna
  - Tipe: **Rasio**
  - Contoh: berat, panjang, lama pengalaman
  - Statistik yang sah: semua

* **Diskret vs kontinu** `[V-DTL01]`: diskret = himpunan nilai terbatas atau bisa dipetakan 1-1 ke bilangan asli. Selain itu kontinu.
* One-hot encoding mengubah nominal menjadi rangkaian biner: red = 100, green = 010, blue = 001 `[V-DTL01]`.

### 3.3 Statistik deskriptif `[S08 hal.45]`
| Jenis data     | Pemusatan           | Variabilitas                        | Sebaran             |
| -------------- | ------------------- | ----------------------------------- | ------------------- |
| Nominal        | modus               | –                                   | frekuensi, proporsi |
| Ordinal        | median, modus       | –                                   | frekuensi, proporsi |
| Interval/Rasio | mean, median, modus | variance, kuartil, persentil, range | frekuensi interval  |

### 3.4 Memeriksa kelengkapan & kualitas `[S08 hal.47-49]`
* **Kelengkapan:** apakah semua data/kolom yang perlu sudah ada, cukup jumlahnya, dan label berimbang?
* **Kualitas:** inkonsistensi (kode aneh, format tanggal), **missing values**, **duplikat**, **pencilan**, dan korelasi antaratribut serta atribut–label.
* **Data kotor** (noisy/inconsistent):
  * *class noise*: sampel kontradiktif atau salah label;
  * *attribute noise*: salah entri, pelanggaran konstrain, whitespace, beda satuan (cm vs m), beda level agregasi (harian vs mingguan).

### 3.5 Identifikasi pencilan (outlier)
* **Aturan IQR** `[S08 hal.50-51]`: IQR = Q3 − Q1. Low outlier < Q1 − 1.5·IQR, high outlier > Q3 + 1.5·IQR. Visualisasinya *box/whisker plot*. Contoh slide: Q1 = 19, Q3 = 24 → IQR = 5 → batas 11.5 dan 31.5.
* **Aturan 3 STD** `[S08 hal.52]`: x outlier bila x < x̄ − 3·STD atau x > x̄ + 3·STD, dengan STD = √(Σ(xᵢ − x̄)²/n).

### 3.6 Data tidak berimbang `[S08 hal.53]`
Contoh: kelas A = 1000 (majority), kelas B = 10 (minority). Model cenderung mengabaikan minority.

### 3.7 Grafik eksplorasi `[S08 hal.54-56]`
* Univariat: pie/bar chart (nominal, ordinal), histogram (interval, rasio).
* Bi/multivariat: box plot, scatter plot, heatmap (korelasi).

### 3.8 Laporan telaah data `[S08 hal.57]`
Berisi deskripsi data, kualitas, dan kuantitas. Laporan ini menjadi **dasar keputusan** di Data Preparation. Di notebook, ini adalah blok **Insight** di bawah tiap sel.

---

## 4. Data Preparation

`[S08 hal.58-88]` Tujuan: meningkatkan kualitas data dan memudahkan pemodelan. Urutan CRISP-DM adalah **Select → Clean → Construct → Integrate → Format**.

Proses lengkap menurut slide `[S08 hal.63]`:
1. **Pemilihan data**: record selection (sampling), feature selection
2. **Perbaikan data**: missing values, error, outlier, duplikasi
3. **Konstruksi data**: transformasi, encoding, dimensionality reduction
4. **Integrasi data**: join, append (concat/merge)

### 4.1 Select data
* Pilih data yang relevan dengan tujuan data science dan **catat alasan** inklusi/eksklusi `[S08 hal.60]`.
* **Sampling** `[S08 hal.64-66]`: probability sampling (acak berbasis peluang) vs non-probability (subjektif). Langkahnya: definisikan populasi → sampling frame → metode → ukuran sampel → kumpulkan.
* **Feature selection** `[S08 hal.67-71]`: mengurangi jumlah variabel masukan untuk menurunkan biaya komputasi dan kadang menaikkan performa.
  * *Unsupervised*: tanpa target. Contoh: jika dua fitur berkorelasi kuat, buang salah satu.
  * *Supervised*:
    * **Filter**: ukur hubungan tiap fitur dengan target memakai statistik atau *feature importance*, lalu pilih yang paling kuat.
    * **Wrapper** (RFE).
    * **Intrinsic** (pohon keputusan memilih fitur sendiri).

### 4.2 Clean data
**A. Missing values** `[S08 hal.73]`, enam cara:
1. hapus baris/kolom yang mengandung missing;
2. isi dengan **mean / median / modus**;
3. isi dengan nilai tetap;
4. interpolasi berdasarkan tren di sekitarnya;
5. forward/backward fill (nilai sebelum/sesudahnya);
6. **imputasi dengan prediksi**: latih model untuk menebak nilai hilang dari kolom lain.

Di DTL ada cara khusus untuk missing value, lihat [§8.6](#86-missing-attribute-values).

**B. Duplikasi** `[S08 hal.74]`: hapus, karena duplikat mendistorsi statistik, menambah overfitting, membuang waktu proses, dan membuat bias.

**C. Outliers** `[S08 hal.75]`: biasanya dihapus atau diimputasi seperti missing. **Catatan tubes:** pencilan yang *nyata* (bukan error) lebih baik dijinakkan dengan transformasi (log, kuantil) daripada dibuang.

**D. Kesalahan data** `[S08 hal.76]`: diperbaiki, dihapus, atau diimputasi.

### 4.3 Construct data
**Transformasi data** `[S08 hal.78-84]`, enam jenis:
1. **Data smoothing (binning)**: kelompokkan nilai kontinu ke dalam interval/bin.
   * Pro: berlaku untuk data kategorik dan numerik; model lebih robust dan mencegah overfitting.
   * Kontra: menambah komputasi, membuang informasi, kadang redundan.
   * Untuk kategori yang jarang (< 100 record pada data 100 ribu baris), gabungkan menjadi "Lain-lain".
2. **Attribute construction**: atribut baru dari atribut lama, misalnya `area = tinggi × lebar`.
3. **Data generalization**: naikkan ke hierarki konsep lebih tinggi (umur → anak/remaja/dewasa/tua; alamat → kota).
4. **Data aggregation**: ringkasan, misalnya penjualan triwulan → tahunan (`groupby`).
5. **Data discretization**: kontinu → diskret, misalnya berat < 65 ringan, 65–80 mid, > 80 berat; termasuk **pembulatan ke nilai terdekat**.
6. **Data normalization**: **min-max** x' = (x − x_min)/(x_max − x_min) ∈ [0, 1].

**Standardization** (z-score) z = (x − μ)/σ tidak tertulis eksplisit di slide 08, tetapi **diwajibkan spek** untuk Linear Regression. Statistik deskriptif μ dan σ ada di `[S11 hal.11]`.

**Encoding** `[S08 hal.85]`: sebagian algoritma hanya menerima angka, jadi pakai **ordinal encoding** (kategori → 0, 1, 2, … bila berurutan) atau **one-hot encoding** (satu kolom biner per kategori).

**Dimensionality reduction** `[S08 hal.86]`: kurangi dimensi tetapi **pertahankan semantik** data, misalnya **PCA**, t-SNE, UMAP. Beda dengan feature selection, yang menghapus atribut sehingga semantiknya berubah.

### 4.4 Integrate & format
* **Integrasi** `[S08 hal.88]`: concat (axis 0/1), merge/join (inner, left, right, outer). Tidak dibutuhkan di tubes karena tiap dataset hanya satu tabel.
* **Format** `[S08 hal.60]`: ubah ke bentuk yang dibaca tool tanpa mengubah makna, misalnya menjadi **matriks numerik**.

### 4.5 Aturan emas dari spek & template (bukan dari slide, tapi wajib)
* **Split dulu, baru preparation.** Data validasi harus benar-benar *unseen*.
* Semua statistik (median, mean/std, kuantil, model imputasi) **dihitung dari data latih saja**, lalu dipakai untuk mentransformasi validasi dan test.
* **Train dan test tidak boleh digabung** saat preprocessing.

---

## 5. Modeling & Evaluation

### 5.1 Skenario pemodelan `[S08 hal.89-94]`, `[S09 hal.13-14]`
* **Pilih algoritma** sesuai tugas: KNN, Naive Bayes, regresi, SVM, Decision Tree, Random Forest, deep learning. *"Tidak ada algoritma yang SELALU TERBAIK untuk setiap dataset! Coba beberapa algoritma!"*
* **Bagi data**: data latih (membangun model), data validasi (memilih hyperparameter), data uji (mengukur performa akhir).
* **Langkah eksperimen**: *Best Guess*, *One Factor at a Time*, atau *Grid Search*.
* **Hyperparameter** (mis. k dan jarak pada KNN) sangat bergantung pada persoalan, jadi harus dicoba dan dilihat mana yang terbaik **di validation set** agar tidak overfit `[S09 hal.13]`.
* Validasi: train-test split atau **k-fold cross validation** (disebut di spek).

### 5.2 Evaluasi `[S08 hal.95]`
* Evaluasi model: bandingkan performa capaian vs target, lalu pilih model terbaik.
* Evaluasi proses: review untuk mencari batasan atau kekurangan model.

### 5.3 Metrik
**Klasifikasi** (dari confusion matrix TP, TN, FP, FN):
* Accuracy = (TP+TN)/N
* Precision = TP/(TP+FP)
* Recall = TP/(TP+FN)
* F1 = 2·P·R/(P+R)
* **ROC-AUC** 〔di luar slide; metrik ini ditetapkan halaman Kaggle〕 = luas di bawah kurva TPR vs FPR untuk semua threshold. Artinya: **peluang sampel positif acak mendapat skor lebih tinggi dari sampel negatif acak**. AUC 0.5 = acak, 1 = sempurna. AUC tidak bergantung pada threshold.

**Regresi** `[S11 hal.14]`:
* MAE = (1/n)Σ|yᵢ − ŷᵢ|
* MSE = (1/n)Σ(yᵢ − ŷᵢ)²
* **RMSE** = √MSE (metrik Kaggle)
* R² = 1 − Σ(yᵢ − ŷᵢ)²/Σ(yᵢ − ȳ)²

Contoh di slide: regresi univariat MAE 22.50, MSE 840.97, R² 0.73; multivariat MAE 15.20, MSE 443.90, R² 0.87. Fitur yang lebih banyak dan relevan memberi error lebih kecil.

### 5.4 Overfitting (umum)
Hipotesis h **overfit** bila ada h' dengan error_train(h) < error_train(h') **tetapi** error_D(h) > error_D(h') pada seluruh distribusi data `[S10 hal.31]`, `[V-DTL05]`. Penyebabnya: noise atau data terlalu sedikit. Overfitting bisa menurunkan akurasi 10–25%.

---

## 6. k-Nearest Neighbor (KNN)

Sumber: `[S09 hal.3-14]`.

### 6.1 Konsep
* **Instance-based / lazy learner**: tidak membentuk hipotesis; training hanya **menyimpan seluruh data latih**.
* Prediksi untuk query: (1) hitung **jarak** query ke **semua** data latih, (2) ambil **k tetangga terdekat**, (3) kelas = **mayoritas** kelas k tetangga.

### 6.2 Contoh slide: Play Tennis
Query ⟨Sunny, Cool, High, True⟩ dengan jarak = jumlah atribut yang berbeda (atribut nominal). k = 1 → D2 (No); k = 2 → D1, D2 (No); k = 3 → D1, D2, D6 (No). Jadi **Play = No**.

### 6.3 Jarak
* **Atribut nominal** `[S09 hal.9]`: beda = 1, sama = 0, lalu dijumlahkan. Contoh latihan: data hobi/umur/pendidikan, k = 5.
* **Atribut numerik** `[S09 hal.10-12]`, keluarga **Minkowski**: D(a, b) = (Σⱼ |aⱼ − bⱼ|^p)^(1/p)
  * p = 1 → **Manhattan**: Σ|aⱼ − bⱼ|
  * p = 2 → **Euclidean**: √Σ(aⱼ − bⱼ)²
  * Contoh slide: titik baru (brightness 20, saturation 35) ke (40, 20, Red) → d = √(400+225) = **25**; ke (50, 50, Blue) → √(900+225) = **33.54**; ke (10, 25, Red) → **10** (terdekat).

### 6.4 Catatan `[S09 hal.8]`
- **Fungsi target yang kompleks bisa didekati dengan fungsi lokal yang lebih sederhana**: Biaya klasifikasi tinggi (hitung jarak ke semua data)
- **Tidak ada fase training**: Semua fitur ikut dihitung, padahal target bisa hanya bergantung pada **sedikit** fitur. Fitur tak relevan "mengacaukan" jarak

### 6.5 Hyperparameter `[S09 hal.13]`
* Jarak mana yang terbaik? Berapa k terbaik? **Coba semua** pada train dan validation set.
* *"Mitos: nilai k harus ganjil."* Lebih baik uji k sebagai hyperparameter.

### 6.6 Konsekuensi praktis (penting untuk tubes) 〔di luar slide, kecuali disebut〕
* Fitur **harus diskalakan** (normalisasi/standarisasi/kuantil), karena fitur berskala besar akan mendominasi jarak.
* KNN tidak bisa menerima NaN, jadi wajib imputasi dulu.
* Peluang soft = proporsi suara tetangga. Untuk AUC, *distance-weighted voting* (bobot 1/d) menghasilkan peluang yang lebih halus. Teknik ini di luar slide; sumbernya Cunningham & Delany 2020 (referensi [21] di spek).

---

## 7. Bayes Decision Theory & Naive Bayes

Sumber: `[V-Bayes1]`, `[V-Bayes2]`, `[S09 hal.15-22]`.

### 7.1 Rumus Bayes `[V-Bayes1]`
P(ωᵢ | x) = P(x | ωᵢ) · P(ωᵢ) / P(x)

dengan:
* P(ωᵢ | x) = **posterior**, yaitu peluang kelas ωᵢ setelah melihat fitur x;
* P(x | ωᵢ) = **likelihood / class-conditional probability**;
* P(ωᵢ) = **prior**, keyakinan awal peluang kelas (jumlah semua prior = 1);
* P(x) = **evidence / marginal**, faktor skala supaya total posterior = 1. Bisa **diabaikan** saat membandingkan kelas, karena sama untuk semua kelas.

### 7.2 Bayes decision rule (minimum error) `[V-Bayes1]`
Pilih ω₁ bila P(x|ω₁)P(ω₁) > P(x|ω₂)P(ω₂), selain itu pilih ω₂.

Contoh video: P(ω₁) = 2/3, P(ω₂) = 1/3, P(x=10|ω₁) = 0.08, P(x=10|ω₂) = 0.14 → 0.054 vs 0.046 → **ω₁**.

Contoh ikan (fitur lightness pada interval 5–5.5): P(salmon) = 74/N, P(x|salmon) = 4/74. Hasilnya posterior salmon 0.03 > sea bass 0.02, jadi **salmon**. Likelihood dihitung dari frekuensi: P(x|ωᵢ) = count(x, ωᵢ)/Nᵢ.

### 7.3 Minimum-risk Bayes decision rule `[V-Bayes2]` (dipakai untuk bonus cost-sensitive)
Setiap kesalahan bisa punya **biaya berbeda**. Contoh pengalengan ikan: pelanggan mau menerima salmon di kaleng sea bass, tetapi tidak sebaliknya.
* Definisikan **aksi** αᵢ dan **loss function** λ(αᵢ | ωⱼ) = biaya mengambil aksi αᵢ bila kelas sebenarnya ωⱼ.
* **Conditional risk**: R(αᵢ | x) = Σⱼ λ(αᵢ | ωⱼ) · P(ωⱼ | x)
* Aturannya: hitung risk semua aksi, lalu **pilih aksi dengan risk minimum**.
* Dua kelas (α₁ = pilih ω₁, α₂ = pilih ω₂, λᵢⱼ = λ(αᵢ|ωⱼ)): pilih ω₁ bila
  (λ₂₁ − λ₁₁) · P(x|ω₁)P(ω₁) > (λ₁₂ − λ₂₂) · P(x|ω₂)P(ω₂).
  Dalam bentuk **likelihood ratio**: P(x|ω₁)/P(x|ω₂) > [(λ₁₂ − λ₂₂)/(λ₂₁ − λ₁₁)] · [P(ω₂)/P(ω₁)] = **threshold** (tidak bergantung pada x).
* Contoh video: likelihood ratio 1.02 > threshold 0.77, jadi salmon.
* **Kasus khusus:** loss 0-1 dan prior sama → threshold = 1 → *maximum likelihood decision rule*.

**Penerapan di tubes (cost FN = 2 × FP):** misal ω₁ = phishing. Kesalahan "bilang legit padahal phishing" (FN) berbiaya 2, sedangkan FP berbiaya 1. Maka pilih phishing bila 2·P(phishing|x) > 1·P(legit|x), yaitu **P(phishing|x) > 1/3**. Threshold turun dari 0.5 menjadi 0.333.

### 7.4 Naive Bayes `[S09 hal.16-22]`
* Model probabilistik: hipotesisnya adalah tabel **P(vⱼ)** dan **P(aᵢ | vⱼ)**.
* **Asumsi naive:** atribut saling **independen** jika kelas diketahui, sehingga
  P(vⱼ | a₁…aₙ) ∝ P(vⱼ) · Πᵢ P(aᵢ | vⱼ)
* **Learning:** hitung frekuensi tiap nilai atribut per kelas dan frekuensi tiap kelas.
* **Klasifikasi:** kelas dengan nilai P(vⱼ)·Π P(aᵢ|vⱼ) **maksimum**.

**Contoh slide (Play Tennis, 9 yes / 5 no)**, query ⟨sunny, cool, high, true⟩:
* yes: 9/14 · 2/9 · 3/9 · 3/9 · 3/9 = **0.0053**
* no: 5/14 · 3/5 · 1/5 · 4/5 · 3/5 = **0.0206** → **No**

Tabel frekuensi: outlook sunny 2/3 (yes/no), overcast 4/0, rainy 3/2; temperature hot 2/2, mild 4/2, cool 3/1; humidity high 3/4, normal 6/1; windy false 6/2, true 3/3.

### 7.5 Hal praktis 〔di luar slide〕 (wajib dipahami)
* **Frekuensi nol:** (overcast | no) = 0 akan membuat seluruh perkalian bernilai 0. Solusinya **Laplace smoothing**: P(a=v|c) = (count + α)/(N_c + α·K), dengan K = jumlah nilai atribut.
* **Underflow:** perkalian puluhan peluang kecil bisa menjadi 0 di komputer. Hitung di **ruang log**: log P(vⱼ) + Σ log P(aᵢ|vⱼ).
* **Atribut kontinu:** pakai (a) **Gaussian NB**, P(a|c) = N(a; μ_c, σ²_c), atau (b) **diskretisasi** menjadi bin lalu hitung frekuensi seperti contoh slide.
* **Missing value:** cukup lewati atribut itu untuk baris tersebut (konsekuensi asumsi independen).
* Struktur NB sebagai **Bayesian network** (bonus graf NB): node kelas adalah satu-satunya *parent* dari setiap node fitur, tanpa garis antarfitur.

---

## 8. Decision Tree Learning

Sumber: `[S10]` dan video Bu Ulfa `[V-DTL01..09]`.

### 8.1 Apa, mengapa, kapan `[S10 hal.8-12]`, `[V-DTL02]`
* DTL adalah metode mengaproksimasi **fungsi target bernilai diskret**. Representasinya **pohon keputusan**, atau setara dengan himpunan **aturan IF-THEN**.
* Simpul internal menguji satu atribut, cabang adalah nilai atribut itu, dan daun adalah hasil klasifikasi.
* Pohon merepresentasikan **disjungsi dari konjungsi**, misalnya (outlook=sunny ∧ humidity=normal) ∨ (outlook=overcast) ∨ (outlook=rain ∧ wind=weak).
* Kenapa dipakai: populer, mudah dibaca, **robust terhadap data noisy**, bisa belajar ekspresi disjungtif. Sudah dipakai untuk diagnosis medis dan risiko kredit.
* Cocok bila data berbentuk pasangan atribut-nilai, target diskret, butuh disjungsi, data mungkin mengandung error, atau data mungkin punya **missing value**. Atribut kontinu ditangani dengan diskretisasi.

### 8.2 Algoritma ID3 `[S10 hal.13-15]`, `[V-DTL03]`
Diusulkan Quinlan (1986). Bekerja **top-down** dengan pencarian **greedy**:

```
ID3(S, atribut):
  1. A ← atribut "terbaik" (information gain terbesar)
  2. jadikan A atribut keputusan di simpul ini
  3. untuk setiap nilai v dari A: buat cabang, kelompokkan S_v
  4. untuk setiap cabang:
       jika semua contoh di S_v sekelas -> daun dengan kelas itu
       jika S_v kosong -> daun dengan kelas mayoritas induk (PLURALITY-VALUE)
       jika atribut habis -> daun kelas mayoritas
       selain itu -> ID3(S_v, atribut - {A})
```
Versi Russell & Norvig `[S10 hal.15]`: PLURALITY-VALUE memilih kelas terbanyak (seri dipecah acak). Pemilihan atribut bisa dengan information gain atau gain ratio. |A| = 2 menghasilkan binary tree; |A| ≥ 2 menghasilkan n-ary tree.

Contoh Play Tennis (14 data) `[V-DTL03]`:
* Root = **Outlook**. Overcast (4 data) semuanya Yes → daun Yes.
* Sunny (2 Yes, 3 No) → **Humidity**: High → No (D1, D2, D8); Normal → Yes (D9, D11).
* Rain (3 Yes, 2 No) → **Wind**: Strong → No; Weak → Yes.

Atribut terbaik idealnya memecah data menjadi kelompok yang **sekelas**. Contoh: "Patrons" lebih baik daripada "Type", karena nilai None/Some langsung menentukan kelas.

### 8.3 Entropy & Information Gain `[S10 hal.16-26]`, `[V-DTL04]`
**Entropy** = ukuran ketidakmurnian (impurity), yaitu jumlah bit minimum untuk mengkodekan kelas satu anggota acak dari S:

Entropy(S) = − Σᵢ₌₁ᶜ pᵢ · log₂ pᵢ   (pᵢ = proporsi kelas i; 0·log 0 dianggap 0)

* Homogen sempurna → 0; dua kelas seimbang → 1; c kelas → maksimum log₂ c.
* Contoh `[S10 hal.20]`: I(3/4, 1/4) = 0.81; I(2/6, 4/6) = 0.92.

**Information Gain** = ekspektasi pengurangan entropy setelah S dipecah berdasarkan A:

Gain(S, A) = Entropy(S) − Σ_{v ∈ Values(A)} (|S_v|/|S|) · Entropy(S_v)

Pilih A dengan Gain maksimum.

**Contoh Play Tennis** `[V-DTL04]`:
* Entropy(S) = −9/14 log₂ 9/14 − 5/14 log₂ 5/14 = **0.940**
* Gain(S, Outlook) = 0.940 − [5/14·E(2,3) + 4/14·E(4,0) + 5/14·E(3,2)] = **0.246** (terbesar → root). Video menyebutnya "0,2…"; nilai lengkap 0.2467 〔hitungan kami〕, diuji di `tests/`
* Gain(S, Humidity) = **0.151**
* Di cabang Sunny (5 data, E = 0.971): Gain(Humidity) = 0.971 → terpilih.

Latihan slide `[S10 hal.27]`: D = 100 data (c1 = 40, c2 = 30, c3 = 30), atr4 memecah menjadi a1 = 70 (40 c1, 30 c2), a2 = 30 (semua c3), a3 = 0. Slide hanya memberi soal. Jawabannya 〔hitungan kami〕: Entropy(D) = 1.571; Gain = 1.571 − 0.7·0.985 = **0.881**.

### 8.4 Overfitting & pruning `[S10 hal.31-40]`, `[V-DTL05]`
* Contoh: tambah D15 yang noise (Sunny, Hot, Normal, Strong → No). Pohon akan menambah cabang agar cocok dengan noise itu, sehingga akurasi pada data baru turun.
* Dua pendekatan:
  1. **Pre-pruning**: hentikan pertumbuhan lebih awal. Lebih langsung, tapi sulit menentukan kapan berhenti.
  2. **Post-pruning**: biarkan overfit lalu pangkas. Lebih sukses di praktik, tapi langkahnya lebih banyak.
* Menentukan ukuran pohon final `[S10 hal.35]`:
  1. pisahkan data: **2/3 training, 1/3 validation**;
  2. pakai semua data lalu uji statistik (mis. chi-square);
  3. **Minimum Description Length**: minimumkan panjang encoding(pohon) + encoding(data | pohon).
* **Reduced Error Pruning** `[S10 hal.36]`: setiap simpul keputusan adalah kandidat pangkas. Pangkas berarti ganti dengan daun berisi **kelas mayoritas** simpul itu. Ulangi sampai pemangkasan merugikan: evaluasi dampak tiap pangkasan pada **validation set**, lalu buang secara greedy simpul yang paling menaikkan akurasi validasi. Efektif bila data banyak.
* **Rule Post-Pruning (C4.5)** `[S10 hal.38-39]`, cocok untuk data terbatas:
  1. tumbuhkan pohon sampai fit (boleh overfit);
  2. ubah setiap jalur akar→daun menjadi **satu aturan**;
  3. **generalisasi** setiap aturan dengan menghapus prekondisi yang menaikkan estimasi akurasi;
  4. urutkan aturan berdasarkan estimasi akurasi dan pakai berurutan.
  * Contoh: "IF Outlook=Sunny ∧ Humidity=High THEN No" dipangkas menjadi "IF Outlook=Sunny THEN No" atau "IF Humidity=High THEN No".
  * Kenapa diubah ke aturan dulu? (1) setiap jalur dipangkas **independen**; (2) tidak ada beda antara atribut dekat akar dan dekat daun; (3) lebih mudah dibaca.
  * Pada C4.5, estimasi akurasi boleh dihitung pada **training set** (tidak perlu validation set terpisah).

### 8.5 Atribut kontinu `[S10 hal.42-43, 50]`, `[V-DTL06]`
* **Diskretisasi** menjadi atribut boolean A_c: TRUE bila A < c.
* Cara memilih threshold c:
  1. urutkan nilai atribut;
  2. cari pasangan bertetangga yang **kelasnya berbeda**;
  3. kandidat c = **titik tengah** pasangan tersebut;
  4. pilih kandidat dengan **gain terbesar**, dan bandingkan sekalian dengan atribut lain.
* Contoh: Temperature 40, 48, 60, 72, 80, 90 dengan kelas No, No, Yes, Yes, Yes, No. Kandidatnya **54** = (48+60)/2 dan **85** = (80+90)/2.
  * Gain(S, T54) = E(S) − [2/6·E(0,2) + 4/6·E(3,1)]
  * Gain(S, T85) = E(S) − [5/6·E(3,2) + 1/6·E(0,1)]
  * Slide dan video tidak menyebut pemenangnya. Bila dihitung, **54 lebih baik** 〔hitungan kami〕: Gain(T54) = 0.459 vs Gain(T85) = 0.191, diuji di `tests/`.
* Versi C4.5 di slide hal. 50: untuk setiap nilai p, partisi ≤ p dan > p, hitung **gain ratio**, lalu ambil yang maksimum.

### 8.6 Missing attribute values `[S10 hal.45-46]`, `[V-DTL07]`
Strategi:
1. isi dengan **nilai paling sering** pada simpul n;
2. isi dengan nilai paling sering **di antara contoh berkelas sama** pada simpul n;
3. **cara C4.5, beri peluang ke setiap nilai:**
   * Saat menghitung **Gain**, hanya data yang nilainya diketahui yang dipakai, lalu hasilnya dikalikan fraksinya:
     Gain(S, A) = F · (Entropy(S_known) − Σ_v |S_v|/|S_known| · Entropy(S_v)), dengan F = |S_known|/|S|.
     Contoh slide: 11 data, 1 hilang → F = **10/11**.
   * Saat **memecah**: data dengan nilai hilang dikirim ke **semua cabang dengan bobot pecahan** sesuai proporsi data yang diketahui. Contoh: 6 data v1 dan 4 data v2 → tambahkan **6/10** ke cabang v1 dan **4/10** ke cabang v2. Akibatnya jumlah data di cabang bisa bukan bilangan bulat.
   * Saat **klasifikasi**, cara yang sama berlaku: instance dengan nilai hilang dihitung di semua cabang dengan bobot proporsi, lalu kelas dengan total bobot terbesar dipilih.
4. **Missing sebagai nilai tersendiri ("?")**: hanya tepat bila hilangnya punya makna sendiri. Tidak tepat bila alasan hilangnya berbeda-beda. Contoh: gula darah hilang karena terlalu tinggi/rendah; IsPregnant hilang untuk pasien pria ("no") berbeda dengan untuk wanita 25 tahun ("unknown").

Latihan slide hal. 54: dataset Play/Don't Play dengan satu Outlook = "?". Hitung GainRatio(Outlook), bobot instance "?" di cabang sunny, threshold Humidity, dan daun tiap cabang.

### 8.7 Ukuran alternatif: Gain Ratio `[S10 hal.48-50]`, `[V-DTL08]`
* Masalah Gain: atribut dengan **banyak nilai** (mis. tanggal) selalu terpilih. Setiap nilainya hanya punya satu data sehingga entropy cabang = 0 dan gain maksimal, padahal tidak berguna untuk data baru.
* **SplitInformation**(S, A) = − Σᵢ (|Sᵢ|/|S|) · log₂(|Sᵢ|/|S|), yaitu entropy dari **pembagian** data (bukan dari kelas).
* **GainRatio**(S, A) = Gain(S, A) / SplitInformation(S, A). Atribut dengan banyak cabang punya SplitInfo besar, sehingga GainRatio mengecil.
* Contoh (video menunjukkan rumusnya, angka akhirnya 〔hitungan kami〕): atribut Date dengan 6 nilai unik → SplitInfo = −6·(1/6 log₂ 1/6) = 2.585. Atribut2 dengan v1 = 4, v2 = 2 → SplitInfo = −(4/6 log₂ 4/6 + 2/6 log₂ 2/6) = 0.918.
* **Bahaya:** bila hampir semua data punya nilai yang sama (|Sᵢ| ≈ |S|), SplitInfo ≈ 0 dan GainRatio tidak terdefinisi atau sangat besar. **Heuristik:** hitung GainRatio hanya untuk atribut yang **gain-nya di atas rata-rata**.
* **ID3 vs C4.5** `[S10 hal.50]`: C4.5 memakai gain ratio, bisa menangani atribut kontinu, menangani missing value, dan memakai rule post-pruning.

### 8.8 Atribut dengan biaya berbeda `[S10 hal.52-53]`, `[V-DTL09]`
Contoh medis: suhu dan nadi murah, biopsi mahal. Pakai atribut murah dulu, yang mahal hanya bila perlu:
* Tan & Schlimmer: Gain²(S, A) / Cost(A)
* Nunez: (2^Gain(S,A) − 1) / (Cost(A) + 1)^w, dengan w ∈ [0, 1] = bobot pentingnya biaya

(Tidak dipakai di tubes. Dicantumkan agar lengkap.)

### 8.9 Pemetaan ke spek & sklearn
Spek meminta salah satu dari **ID3, C4.5, CART** from scratch yang menangani **numerik, kategorikal, dan null**. Pembandingnya `DecisionTreeClassifier`:
* ID3: `criterion='entropy'`
* C4.5: `criterion='entropy'` + `ccp_alpha`
* CART: `criterion='gini'`

CART (Breiman et al. 1984) memakai **Gini impurity** 1 − Σ pᵢ² dan selalu memecah biner. CART tidak dibahas di slide, sumbernya referensi [23] di spek. **Kelompok kita memilih C4.5** karena paling lengkap dibahas di slide dan video.

---

## 9. Linear Regression

Sumber: `[S11 hal.3-15]`, `[V-LR1]` (review regresi), `[V-Perceptron2]` (gradient descent).

### 9.1 Model
* Contoh slide: agen properti menaksir harga rumah dari jumlah kamar.
* Y = **response / dependent variable**; x = **regressor / predictor / independent variable**.
* **Simple:** Y = β₀ + β₁x (β₀ = intercept, β₁ = slope). Contoh: harga = 100 + 50·4 = 300.
* **Multivariat:** h_θ(x) = θ₀ + θ₁x₁ + … + θₙxₙ = **θᵀx** (dengan x₀ = 1).
* Asumsi analisis regresi `[S11 hal.17]`, `[V-LR1]`: hubungan tidak deterministik; random error dengan E(error) = 0 dan varians konstan (**homoscedasticity**).

### 9.2 Least Square Estimator (LSE) `[S11 hal.10-15]`
* Fungsi objektif: **minimumkan SSE** = Σ (yᵢ − ŷᵢ)².
* Simple linear regression, solusi tertutup: **β₁ = σ_XY / σ²_X = cov(X, Y) / var(X)**, β₀ = ȳ − β₁x̄.
  * Contoh slide (CO₂ vs engine size): cov = 78.956, var = 2.0022 → β₁ = **39.435**, β₀ = **124.416**, sama dengan hasil sklearn.
  * Multivariat (ENGINESIZE, CYLINDERS, FUELCONSUMPTION): y = 64.98 + 11.37x₁ + 7.26x₂ + 9.58x₃.
* Definisi statistik `[S11 hal.11]`:
  * variance σ² = E[(X − μ)²]
  * covariance σ_XY = E[(X − μ_X)(Y − μ_Y)]
  * korelasi ρ = σ_XY / (σ_X σ_Y)
* **Ringkasan** `[S11 hal.15]`: cari θ* = argmin J(θ). Solusi analitik: selesaikan ∇J(θ) = 0. Bila tidak bisa, pakai metode numerik iteratif, dan yang paling sederhana adalah **gradient descent**.

### 9.3 Normal equation (bentuk matriks LSE) 〔bentuk matriks di luar slide; slide hanya memberi rumus cov/var untuk 1 fitur〕
Dengan X berisi kolom 1 untuk bias: **θ = (XᵀX)⁻¹ Xᵀy**. Ini hasil dari ∇J = 0 untuk J = ½‖y − Xθ‖². Spek: normal equation boleh dipakai **sebagai pembanding**, tetapi pelatihan utama **wajib gradient descent**.

### 9.4 Gradient descent untuk regresi linear
J(θ) = 1/(2n) Σᵢ (θᵀxᵢ − yᵢ)²  →  ∂J/∂θⱼ = (1/n) Σᵢ (θᵀxᵢ − yᵢ) · xᵢⱼ  →  θⱼ ← θⱼ − η · ∂J/∂θⱼ

Ini sama persis dengan aturan delta pada *unthresholded perceptron* (aktivasi linear) di `[V-Perceptron2]`. Detail batch vs stochastic ada di [§11](#11-gradient-descent).

### 9.5 Regularisasi 〔di luar slide, tetapi diwajibkan spek〕
Tujuannya mencegah bobot terlalu besar atau overfit:
* **L2 / Ridge:** J + (α/2)·‖w‖², gradien tambahan α·w
* **L1 / Lasso:** J + α·‖w‖₁, subgradien tambahan α·sign(w). Mendorong bobot menjadi 0 (seleksi fitur).
* **Bias θ₀ tidak ikut diregularisasi** (wajib menurut spek).
* **Standarisasi fitur sebelum training** (wajib menurut spek). Alasannya: penalti adil untuk setiap fitur, dan GD konvergen lebih cepat.

Referensi: Hoerl & Kennard (1970) untuk Ridge, Tibshirani (1996) untuk Lasso.

---

## 10. Logistic Regression

Sumber: `[S11 hal.16-31]`, `[V-LR1]`, `[V-LR2]` (Khodra/Masayu, referensi [15], [16] di spek).

### 10.1 Kenapa tidak linear regression untuk klasifikasi? `[S11 hal.18-21]`, `[V-LR1]`
* Kita *bisa* melakukan regresi ke label 0/1 lalu memakai threshold 0.5 (contoh dataset honors class, 200 siswa, fitur *write*). Ini disebut **linear discriminant function / linear classifier**: g(x) = wᵀx, decide ω₁ bila g(x) > 0, dan **g(x) = 0 adalah decision surface (hyperplane)**.
* Kelemahannya:
  * linear regression mengasumsikan target berdistribusi normal dengan varians konstan, padahal label biner tidak demikian;
  * LSE butuh asumsi tersebut;
  * output-nya bukan peluang.

### 10.2 Model logistic regression
* ŷ = bᵀx menyatakan **log-odds** peluang sukses: log(p/(1 − p)) = bᵀx. Odds = p/(1 − p).
* Peluang: **p = P(y=1 | x, b) = σ(bᵀx) = 1/(1 + e^(−bᵀx))**, yaitu fungsi logistik/sigmoid.
* Keputusan: kelas 1 bila p ≥ 0.5, selain itu kelas 0 (atau −1). Threshold boleh diubah, misalnya untuk cost-sensitive.
* Interpretasi `[S11 hal.23]`: koefisien 0.08 berarti kenaikan 1 unit *write* menambah **log-odds** sebesar 0.08.
* Ringkasan `[S11 hal.24]`: **linear model, binary classification, soft classification**. Untuk multikelas perlu penanganan khusus, misalnya softmax.
* Latihan `[S11 hal.25]`: linear ŷ = 0.07x − 4.85 vs logistic ŷ = 0.03x − 1.35 untuk write = 65, threshold p > 0.5.

### 10.3 Training: Maximum Likelihood + Stochastic Gradient Ascent `[S11 hal.26-31]`, `[V-LR2]`
* Cari b yang **memaksimumkan log conditional likelihood**:
  LCL = Σᵢ [yᵢ log pᵢ + (1 − yᵢ) log(1 − pᵢ)]
  Suku pertama untuk data berlabel 1, suku kedua untuk data berlabel 0.
* Turunannya: ∂LCL/∂bⱼ = Σᵢ (yᵢ − pᵢ) · xᵢⱼ, yaitu error × fitur.
* **Stochastic gradient ascent** (local search): untuk setiap contoh yang **dipilih acak** (tidak berurutan):
  **bⱼ ← bⱼ + η · (yᵢ − pᵢ) · xᵢⱼ**
  * Parameter: data D, jumlah iterasi T (= **epoch**, satu kali proses seluruh data), learning rate η (0 < η < 1).
  * Inisialisasi b = 0.

**Contoh slide** (η = 0.1, 1 epoch, D = {⟨[52, 41], 0⟩, ⟨[62, 58], 1⟩}):
1. Ambil ⟨[62, 58], 1⟩: p = σ(0) = 0.5 → b₀ = 0 + 0.1(1 − 0.5)·1 = **0.05**, b₁ = 0.1·0.5·62 = **3.1**, b₂ = **2.9**.
2. Ambil ⟨[52, 41], 0⟩: p = σ(0.05 + 3.1·52 + 2.9·41) = σ(280.15) ≈ 1 → b₀ = 0.05 − 0.1 = **−0.05**, b₁ = 3.1 − 5.2 = **−2.1**, b₂ = 2.9 − 4.1 = **−1.2**.
3. Prediksi `[S11 hal.30]`: x₁ → p = 1.53·10⁻⁶⁹ → 0 (benar); x₂ → p = 1.61·10⁻⁸⁷ → 0 (salah). **Akurasi training 50%**. Satu epoch belum cukup.

### 10.4 Bentuk setara yang dipakai di kode
Memaksimumkan LCL sama dengan **meminimumkan log-loss** J = −LCL/n. Gradien log-loss adalah (1/n) Σ (pᵢ − yᵢ)·xᵢ, kebalikan tanda dari slide. Update descent θ ← θ − η∇J **identik** dengan ascent di slide.

Regularisasi untuk spek 〔di luar slide〕: L1, L2, **Elastic Net** = α[ρ‖w‖₁ + (1 − ρ)/2 ‖w‖²]. Referensi: Zou & Hastie 2005.

---

## 11. Gradient Descent

Sumber: `[V-Perceptron2]`, `[S12 hal.10]`, `[S11 hal.15]`.

* GD mencari bobot dengan error minimum menggunakan **gradien permukaan error**. Bayangkan bidang semua kombinasi (w₀, w₁) (*hypothesis space*) dan di atasnya permukaan error. Kita bergerak ke arah **negatif gradien**.
* **Aturan:** Δw = −η · ∇E(w), dengan ∂E/∂wₖ = −Σ_d (y_d − o_d) x_{d,k} untuk E = ½ Σ_d (y_d − o_d)² dan aktivasi linear. Jadi **Δwₖ = η Σ_d (y_d − o_d) x_{d,k}**.

- **Kapan update**: **sekali per epoch**, setelah semua data diproses (Δw diakumulasi, prediksi dalam satu epoch memakai bobot yang sama)
  - **Stochastic (incremental) GD**: **setiap selesai satu instance**
- **Error**: kumulatif seluruh data
  - **Stochastic (incremental) GD**: per instance (dicatat kumulatif untuk terminasi)
- **Kelebihan**: arah turun yang "benar"
  - **Stochastic (incremental) GD**: lebih cepat, kadang lolos dari minimum lokal
- **Kekurangan**: **lambat**, butuh banyak iterasi; tidak ada jaminan minimum global bila ada banyak minimum lokal
  - **Stochastic (incremental) GD**: lintasannya bergoyang

* Terminasi: error < threshold (contoh video: η = 0.3, threshold 0.01, konvergen di epoch ke-10) atau jumlah epoch maksimum.
* **Mini-batch** = kompromi: update per kelompok kecil data. Spek mengizinkan *"batch atau mini-batch"*.
* **Learning rate** terlalu besar membuat error meledak (divergen); terlalu kecil membuat konvergensi lambat. 〔di luar slide〕 Untuk regresi linear, GD batch konvergen bila η < 2/λ_max(XᵀX/n) (Goodfellow et al. 2016, bab 4.3). Bukti numeriknya ada di notebook regresi.
* Inisialisasi bobot: 0 atau acak sangat kecil.
* Optimizer lanjutan **Momentum** dan **Adam** **tidak diajarkan di kelas**. Di tubes keduanya diklaim sebagai **bonus** dengan referensi (Polyak 1964; Kingma & Ba 2015).

---

## 12. Perceptron & ANN

Sumber: `[S12]`, `[V-Perceptron1]`, `[V-Perceptron2]`, `[V-ANN]`. **Tidak dipakai sebagai model tubes** (bukan bagian dari daftar model spek), tetapi konsep GD-nya relevan.

* **Perceptron:** y = sign(wᵀx) ∈ {−1, +1}, linear model untuk data *linearly separable*, membentuk hyperplane decision surface (garis di 2D, bidang di 3D).
* Mudah merepresentasikan fungsi **m-of-n**: AND (m = n), OR (m = 1). Contoh AND: w₁ = w₂ = 0.5, w₀ = −0.8.
* **Perceptron training rule:** wⱼ ← wⱼ + η(yᵢ − oᵢ)xᵢⱼ hanya bila salah prediksi. Dijamin konvergen bila data linearly separable dan η cukup kecil. Bila tidak separable, tidak pernah konvergen, sehingga dipakai **gradient descent** (unthresholded/linear unit = Adaline).
* **ANN / FFNN:** input layer → hidden layer(s) → output layer. Tiap neuron menghitung f(Σ w·x).
  * Aktivasi: sigmoid σ(z) = 1/(1 + e⁻ᶻ), ReLU max(0, z), linear.
  * **XOR** tidak bisa diselesaikan perceptron tunggal tetapi bisa dengan 1 hidden layer: h₁ = σ(−10 + 20x₁ + 20x₂), h₂ = σ(30 − 20x₁ − 20x₂), y = σ(−30 + 20h₁ + 20h₂).
  * *Forward propagation* menghitung output. *Backpropagation* = GD + chain rule untuk melatih bobot.

---

## 13. Peta materi → kode tubes

- **§4.2 imputasi median**: KNN & LogReg klasifikasi
  - File kode: `src/preprocessing.py::MedianImputer`
- **§4.2 imputasi dengan prediksi**: regresi: kiper_refleks dll.
  - File kode: `PlayerPreprocessor` (LinearRegression normal eq.)
- **§4.3 binning/diskretisasi**: LogReg & NB klasifikasi
  - File kode: `QuantileBinner`
- **§4.3 normalisasi min-max**: dicoba dulu untuk KNN (cara slide), kalah dari quantile
  - File kode: `MinMaxScaler`
- **〔di luar slide〕 quantile scaling**: KNN final (CV 0.977 → 0.988)
  - File kode: `QuantileScaler` (berbasis peringkat)
- **§4.3 standarisasi**: LogReg, LinReg
  - File kode: `StandardScaler`
- **§4.3 one-hot**: bin, fitur diskret, posisi, tipe badan
  - File kode: `one_hot()`
- **§4.3 attribute construction**
  - File kode: interaksi atribut × posisi; indikator missing/-1
- **§4.3 PCA**: dicoba, tidak dipakai (alasan di notebook)
  - File kode: notebook (SVD NumPy)
- **§4.1 filter feature selection**: bobot fitur dari AUC univariat
  - File kode: `KNNClassifier(feature_weighting='auc')`
- **§6 KNN**: Minkowski/Manhattan/Euclidean, voting mayoritas; 〔di luar slide〕 voting berbobot jarak
  - File kode: `src/models/knn.py`
- **§6 KNN multikelas**: penebak posisi cara slide; kalah dari softmax 〔di luar slide〕
  - File kode: `PlayerPreprocessor(position_model='knn')`
- **§7.4 Naive Bayes**: kategorikal (frekuensi + Laplace) + Gaussian, log-space
  - File kode: `src/models/naive_bayes.py`
- **§7.3 minimum-risk**: threshold 1/3
  - File kode: notebook klasifikasi, bonus cost-sensitive
- **§8 C4.5**: gain ratio + heuristik rata-rata, threshold, missing berbobot, **REP greedy** (hal. 36), **rule post-pruning** (hal. 38)
  - File kode: `src/models/decision_tree.py`
- **§9 Linear Regression**: GD batch/mini-batch, normal eq, L1, L2
  - File kode: `src/models/linear_regression.py`
- **§10 Logistic Regression**: SGA persis slide (`batch_size=1, optimizer='gd'`, diuji dengan contoh hal. 29); mini-batch, L1/L2/EN, class_weight
  - File kode: `src/models/logistic_regression.py`
- **§11 GD + bonus optimizer**: gd, momentum, adam, lr_decay
  - File kode: `src/models/optimizers.py`
- **§5.3 metrik**: AUC, F1, RMSE, R², k-fold
  - File kode: `src/metrics.py`

---

## 14. Daftar sumber

**Slide kuliah IF3070 2026/2027** (folder `instruction/materi_kelas/`):
* `[S08]` Materi08 *Introduction to Data Science*: CRISP-DM, Data Understanding, Data Preparation (99 hal.) → `materikelas08.md`
* `[S09]` Materi09 *KNN – Naive Bayes* (23 hal.) → `materikelas09.md`
* `[S10]` Materi10 *Decision Tree Learning* (55 hal.), N. U. Maulidevi → `materikelas10.md`
* `[S11]` Materi11 *Linear Regression & Logistic Regression* (33 hal.) → `materikelas11.md`
* `[S12]` Materi12 *Perceptron & ANN* (44 hal.) → `materikelas12.md`

**Video modul (Masayu L. Khodra)**, transkrip di `instruction/transkrip_video/<nama>.txt`:
* `[V-Classification]` Tipe task klasifikasi
* `[V-Bayes1]` Bayes Decision Rule
* `[V-Bayes2]` Minimum Risk Bayes Decision Rule
* `[V-LR1]` Logistic Regression: What & Why, https://www.youtube.com/watch?v=QAKZ_pymEzc (ref. [15] spek)
* `[V-LR2]` Logistic Regression: Stochastic Gradient Ascent, https://www.youtube.com/watch?v=O5NSNMQO1yU (ref. [16] spek)
* `[V-Perceptron1]` Perceptron
* `[V-Perceptron2]` Gradient Descent untuk Perceptron
* `[V-ANN]` Feed Forward Neural Network

**Video IF3270 DTL (Nur Ulfa Maulidevi)**, transkrip di `instruction/transkrip_dtl/` (ref. [6]–[14] spek):
* `[V-DTL01]` Attribute Types: https://www.youtube.com/watch?v=UkZjVkVqUrQ
* `[V-DTL02]` What, Why, and When: https://www.youtube.com/watch?v=zBUe2ma_14A
* `[V-DTL03]` Basic DTL Algorithm (ID3): https://www.youtube.com/watch?v=uSTgx9NiEHQ
* `[V-DTL04]` Information Gain: https://www.youtube.com/watch?v=aVE7xQJNuCA
* `[V-DTL05]` Overfitting: https://www.youtube.com/watch?v=hkxC117tEu4
* `[V-DTL06]` Continuous-valued Attribute: https://www.youtube.com/watch?v=7x-62Kqj04k
* `[V-DTL07]` Missing Attribute Values: https://www.youtube.com/watch?v=ZR7l0FYZLF8
* `[V-DTL08]` Alternative Measures: https://www.youtube.com/watch?v=4_Ueiuchxrk
* `[V-DTL09]` Attributes with Differing Costs: https://www.youtube.com/watch?v=GxH3xjtCFcY

**Referensi luar yang dipakai di kode** (wajib dicantumkan di laporan):
* P. Cunningham & S. J. Delany, *k-Nearest Neighbour Classifiers*, arXiv:2004.04523, 2020 (distance-weighted voting).
* J. R. Quinlan, *C4.5: Programs for Machine Learning*, Morgan Kaufmann, 1993 (pessimistic error pruning).
* H. Zou & T. Hastie, *Regularization and variable selection via the elastic net*, JRSS-B, 2005.
* B. T. Polyak, *Some methods of speeding up the convergence of iteration methods*, 1964 (momentum).
* D. P. Kingma & J. Ba, *Adam: A Method for Stochastic Optimization*, ICLR 2015, arXiv:1412.6980.
* C. M. Bishop, *Pattern Recognition and Machine Learning*, 2006, bab 4.3.4 (softmax regression).
* T. Mitchell, *Machine Learning*, McGraw-Hill, 1997 (bab 3 DTL, bab 4 GD, bab 6 Bayes).
* scikit-learn docs, *QuantileTransformer* (ide quantile scaling).

> **Catatan transkrip:** transkrip DTL berasal dari subtitle otomatis YouTube, sehingga ada salah eja ("game" = gain, "sea four point five" = C4.5). Isi di dokumen ini sudah dikoreksi dan dicocokkan dengan slide.
