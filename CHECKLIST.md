# CHECKLIST.md — Daftar Tugas yang Bisa Dicentang

> **Cara pakai:** ganti `[ ]` menjadi `[x]` setelah selesai, lalu commit dengan pesan `docs(checklist): <bagian> selesai`. Setiap tugas punya kode (mis. `B2.3`) yang sama dengan diagram `docs/diagram_alur_kerja.png`.
> Item bertanda **(baseline)** sudah dikerjakan leader. Tugasmu adalah **memverifikasi**, **memahami**, dan bila perlu **memperbaikinya**.
> Rincian alasan teknis ada di `PANDUAN.md`, aturan di `CONSTRAINT.md`, dan teori di `MATERI.md`.

## Siapa memegang peran apa

Isi namamu di sini saat memilih peran (commit pertamamu!):

| Peran     | Nama           | NIM      | Fokus                                                      |
| --------- | -------------- | -------- | ---------------------------------------------------------- |
| Leader    | M. Faris Daffa | 18224025 | DTL C4.5, submisi final, review                            |
| Anggota A |                |          | Logistic Regression + bonus video/optimizer/cost-sensitive |
| Anggota B |                |          | KNN + data klasifikasi + notebook klasifikasi              |
| Anggota C |                |          | Naive Bayes + utilitas + laporan/README                    |
| Anggota D |                |          | Linear Regression + data regresi + notebook regresi        |

NIM anggota: 18224009 · 18224016 · 18224025 · 18224027 · 18224096. **NIM terkecil (18224009) yang membuat release & submit Edunex.**

---

## Bobot beban kerja (adil, berdasarkan kompleksitas)

Bobot kompleksitas: 1 poin ≈ setengah hari kerja. Total ≈ 49 poin, ≈ 10 poin per orang. **Setiap orang memegang tepat satu algoritma from scratch.** Leader memegang DTL karena paling kompleks.

- **Leader**: keputusan & submisi final Kaggle, review PR
  - Pemilik: M. Faris Daffa (18224025)
  - Algoritma: **DTL C4.5** (8)
  - Bonus: gambar pohon top-N (2)
  - Poin: 10
- **Anggota A**: –
  - Pemilik: *(pilih sendiri)*
  - Algoritma: **Logistic Regression** L1/L2/EN (4)
  - Bonus: video kontur (2), Momentum/Adam (1.5), cost-sensitive (2)
  - Poin: 9.5
- **Anggota B**: Data Understanding & Preparation **klasifikasi** (4), integrasi notebook klasifikasi (2)
  - Pemilik: *(pilih sendiri)*
  - Algoritma: **KNN** (3)
  - Bonus: –
  - Poin: 9
- **Anggota C**: utilitas `metrics.py`/`base.py`/tests (3), compile **laporan PDF + README** (3)
  - Pemilik: *(pilih sendiri)*
  - Algoritma: **Naive Bayes** (3)
  - Bonus: graf NB (1)
  - Poin: 10
- **Anggota D**: Data Understanding & Preparation **regresi** (4), integrasi notebook regresi (1.5)
  - Pemilik: *(pilih sendiri)*
  - Algoritma: **Linear Regression** (4)
  - Bonus: optimizer LinReg / lr decay (1.5)
  - Poin: 11

Anggota 18224009, 18224016, 18224027, dan 18224096 memilih peran A–D sendiri, lalu menulis namanya di `README.md` dan tabel peran di atas.

**Semua orang juga wajib:**
1. memahami dan bisa menjelaskan file kodenya;
2. menulis bab laporannya (penjelasan kelas/fungsi + potongan source code + perbandingan sklearn + insight);
3. mengerjakan minimal **1 eksperimen peningkatan** (`PANDUAN.md` §10.2) dan mencatat hasilnya;
4. commit di branch sendiri dan membuat PR.

---

## Timeline (mundur dari deadline Kamis 3 Des 2026 22.22 WIB)

- **0. Baseline & onboarding**: Baseline lengkap (✅ sudah). Semua anggota: setup environment, baca README/CONSTRAINT/CHECKLIST, pilih peran A–D, jalankan tests & notebook
  - Tanggal: 17–18 Nov
  - Siapa: semua
- **1. Pahami & jalankan**: Tiap orang memahami file kodenya dan bisa menjelaskannya. **C** memastikan utilitas stabil; **B** & **D** memastikan preprocessing stabil (fondasi orang lain)
  - Tanggal: 19–23 Nov
  - Siapa: semua
- **2. Eksplorasi & bonus**: Eksperimen peningkatan (`PANDUAN.md` §10.2) + finalisasi bonus + mulai draf bab laporan
  - Tanggal: 24–28 Nov
  - Siapa: semua
- **3. Integrasi & FREEZE**: Merge semua PR, run bersih, **leader submit final ke Kaggle (paling lambat 1 Des 23.59)**, catat MD5. Setelah freeze, **tidak ada perubahan kode** kecuali bugfix yang disetujui
  - Tanggal: 29 Nov – 1 Des
  - Siapa: B, D, Leader
- **4. Laporan & rilis**: C compile laporan PDF + README + form AI. Leader review akhir dan menjadikan repo **public**. **Anggota NIM terkecil (18224009)** membuat **release `v1.0`** dan submit link di Edunex **sebelum 3 Des 22.22** (target 3 Des 18.00)
  - Tanggal: 2–3 Des
  - Siapa: C, Leader, 18224009

Urutan dependensi (siapa butuh hasil siapa) ada di `docs/diagram_alur_kerja.png` dan `docs/diagram_pohon_tugas.png`. Ringkasnya:
* **C1 (utilitas)**, **B1 (prep klasifikasi)**, **D1 (prep regresi)** adalah **fondasi**. Selesaikan dulu, karena model lain bergantung padanya.
* B3 (notebook klasifikasi) menunggu A2, B2, C2, L2. D3 (notebook regresi) menunggu D2.
* L3 (submisi final) menunggu B3 & D3. C4 (laporan) menunggu L3 & semua draf bab.

---

## 0. Checklist global spek (dipantau leader)

### Wajib
- [x] DTL from scratch (C4.5): numerik + kategorikal + null **(baseline)**
- [x] Logistic Regression from scratch + L1, L2, Elastic Net **(baseline)**
- [x] KNN from scratch (opsional karena "pilih antara", tetap dikerjakan) **(baseline)**
- [x] Naive Bayes from scratch **(baseline)**
- [x] Perbandingan sklearn: DTL (ID3 entropy, C4.5 entropy + ccp_alpha, CART gini), LogReg, KNN, NB **(baseline)**
- [x] Linear Regression from scratch: GD batch/mini-batch, normal eq pembanding, L1, L2, standarisasi, bias tidak diregularisasi **(baseline)**
- [x] Bandingkan dengan LinearRegression/Ridge/Lasso: MAE, RMSE, R² + plot pred-vs-actual + residual **(baseline)**
- [x] Save & load model **(baseline)**
- [x] Tahapan: cleaning, transformation, feature selection, dimensionality reduction, modeling & validation **(baseline)**
- [x] Preprocessing train/test terpisah (fit di train saja) **(baseline)**
- [ ] Submisi Kaggle **Klasifikasi** minimal 1 (file siap di `output/submissions/`)
- [ ] Submisi Kaggle **Regresi** minimal 1 (file siap di `output/submissions/`)
- [x] Notebook reproducible (MD5 submisi identik saat dijalankan ulang) **(baseline, cek ulang saat freeze)**
- [ ] Repo GitHub `IF3070_G08_MachineUnlearning` dengan `src/`, `docs/`, `output/`, `README.md`
- [ ] Laporan PDF lengkap di `docs/`
- [ ] Repo **public** + release `v1.0` + link di Edunex (oleh 18224009) **sebelum 3 Des 2026 22.22 WIB**

### Bonus (maks. 20 poin)
- [ ] Kaggle rank top-10 (nama tim = nama kelompok)
- [x] Gambar pohon top-N **(baseline)**
- [x] Video kontur log-loss LogReg **(baseline)**
- [x] Graf Naive Bayes **(baseline)**
- [x] Optimizer di luar materi + referensi: Momentum, Adam, LR decay **(baseline)**, plus penjelasan di laporan
- [x] Cost-sensitive (FN = 2 × FP) di notebook **(baseline)**, plus analisis di laporan

---

## Leader — M. Faris Daffa (DTL C4.5, submisi, review)

**Fase 0–1**
- [x] L0.1 Baseline kode, notebook, dokumen, diagram
- [ ] L0.2 Buat repo GitHub (private dulu), push baseline, undang 4 anggota sebagai collaborator
- [ ] L0.3 Daftarkan tim Kaggle bernama "Machine Unlearning" di kedua kompetisi
- [ ] L1.1 Baca ulang `src/models/decision_tree.py` dan pastikan bisa menjelaskan: `_eval_numeric`, `_eval_categorical`, `_best_split` (heuristik gain rata-rata), `_build` (bobot missing), `_route`, `prune_reduced_error` (greedy), `to_rules`, `prune_rules`, `predict_proba_rules`

**Fase 2**
- [ ] L2.1 Eksperimen E6: tuning `min_samples_leaf`, `laplace`, `criterion` dan catat di log eksperimen
- [ ] L2.2 Jelaskan di laporan: REP greedy vs rule post-pruning (tabel di notebook) dan kenapa AUC turun walau akurasi naik
- [ ] L2.3 Cek gambar pohon top-N (`output/figures/c45_tree_top15.png`) dan coba beberapa nilai `top_n`
- [ ] L2.4 Tulis bab laporan: DTL C4.5 + perbandingan sklearn + bonus pohon

**Fase 3–4**
- [ ] L3.1 Review & merge semua PR (cek Definition of Done di `PANDUAN.md` §11)
- [ ] L3.2 Run bersih (`bash tools/run_all.sh`), pilih model final berdasarkan CV
- [ ] L3.3 Submit kedua CSV ke Kaggle, pilih sebagai final, catat MD5 & skor di README (**freeze 1 Des**)
- [ ] L3.4 Uji clone bersih: MD5 identik
- [ ] L4.1 Tulis Kesimpulan & Saran, review laporan akhir
- [ ] L4.2 Jadikan repo **public**, ingatkan 18224009 membuat release `v1.0`

---

## Anggota A — Logistic Regression (+ bonus video, optimizer, cost-sensitive)

**Fase 0–1**
- [ ] A0.1 Setup environment (`PANDUAN.md` §7), `python tests/test_models.py` lulus
- [ ] A0.2 Baca `MATERI.md` §10 (Logistic Regression) dan §11 (Gradient Descent)
- [ ] A1.1 Pahami `src/models/logistic_regression.py`: sigmoid, `fit` (mini-batch, bias tidak diregularisasi), `_reg_strengths` (L1/L2/EN), `class_weight`
- [ ] A1.2 Pahami `src/models/optimizers.py` (gd, momentum, adam, lr_decay) dan bisa menjelaskan bedanya
- [ ] A1.3 Jalankan section 7 "Logistic Regression" di notebook klasifikasi, pahami tabel L1/L2/EN

**Fase 2**
- [ ] A2.1 Eksperimen E4/E5 (`PANDUAN.md` §10.2), catat CV di log eksperimen
- [ ] A2.2 Bonus video: cek `output/figures/logreg_contour.mp4`. Bila perlu perindah (judul, kecepatan, fitur lain)
- [ ] A2.3 Bonus optimizer: siapkan penjelasan cara kerja Momentum & Adam + referensi (Polyak 1964; Kingma & Ba 2015) + plot konvergensi
- [ ] A2.4 Bonus cost-sensitive: pahami turunan threshold 1/3 (MATERI §7.3) & hasil tabel biaya, tulis analisisnya

**Fase 3**
- [ ] A3.1 Draf bab laporan: LogReg (kelas + source code + L1/L2/EN + perbandingan sklearn), optimizer, cost-sensitive, video
- [ ] A3.2 PR ke `main`, lalu kirim draf ke Anggota C

---

## Anggota B — KNN + Data Understanding/Preparation klasifikasi + notebook klasifikasi

**Fase 0–1**
- [ ] B0.1 Setup environment, test lulus, notebook klasifikasi berjalan
- [ ] B0.2 Baca `MATERI.md` §3, §4, §6
- [ ] B1.1 Pahami `PhishingPreprocessor` di `src/preprocessing.py`: 4 mode (`tree`, `nb`, `knn`, `linear`), `MinMaxScaler` (slide) vs `QuantileScaler` (luar slide), `QuantileBinner`, indikator missing/−1; pahami tabel "langkah KNN dari murni slide → final"
- [ ] B1.2 Verifikasi section 3 & 5 notebook (Data Understanding & Preparation): angka dan insight masuk akal
- [ ] B1.3 Pastikan tidak ada data leakage (fit hanya di train) dan jelaskan alasannya di laporan

**Fase 2**
- [ ] B2.1 Pahami `src/models/knn.py`: jarak Manhattan/Euclidean/Minkowski, `kneighbors` per batch, bobot jarak, `feature_weighting='auc'`
- [ ] B2.2 Eksperimen E1/E2/E3 (tie-breaking, `weighting_power`, k, metrik) dan catat CV
- [ ] B2.3 Kirim kandidat perbaikan ke leader **dengan bukti CV** (jangan submit sendiri)

**Fase 3**
- [ ] B3.1 Pemilik notebook klasifikasi: integrasikan perubahan dari A, C, Leader; Restart & Run All
- [ ] B3.2 Perbarui blok **Insight** bila angka berubah
- [ ] B3.3 Draf bab laporan: Deskripsi persoalan (dataset phishing), cleaning & preprocessing + alasan, KNN + perbandingan sklearn

---

## Anggota C — Naive Bayes + utilitas + laporan/README

**Fase 0–1**
- [ ] C0.1 Setup environment, test lulus
- [ ] C0.2 Baca `MATERI.md` §5.3 (metrik) dan §7 (Bayes & Naive Bayes)
- [ ] C1.1 Pahami `src/metrics.py` (ROC-AUC via ranking, F1, RMSE, R², k-fold, skor kompetisi) dan `src/models/base.py` (save/load)
- [ ] C1.2 Pahami `tests/test_models.py`; tambah minimal 1 test baru (mis. NB dengan missing value)

**Fase 2**
- [ ] C2.1 Pahami `src/models/naive_bayes.py`: tabel frekuensi + Laplace, Gaussian, log-space, missing dilewati; cocokkan dengan contoh Play Tennis (0.0053 vs 0.0206)
- [ ] C2.2 Eksperimen E7 dan catat CV
- [ ] C2.3 Bonus graf NB: cek `output/figures/naive_bayes_graph.png`, jelaskan arti garis dan asumsi independensi

**Fase 3–4**
- [ ] C3.1 Siapkan Google Docs laporan dengan struktur `PANDUAN.md` §12, bagikan ke tim
- [ ] C3.2 Kumpulkan draf semua bab, rapikan format & referensi (gaya IEEE)
- [ ] C4.1 Ekspor laporan ke PDF, simpan di `docs/`, lalu commit
- [ ] C4.2 Lengkapi `README.md` (tabel pembagian tugas, riwayat submisi dari leader)
- [ ] C4.3 Koordinasikan **Form Penggunaan Generative AI**: kumpulkan dari semua anggota, isi jujur, lampirkan di PDF

---

## Anggota D — Linear Regression + Data Understanding/Preparation regresi + notebook regresi

**Fase 0–1**
- [ ] D0.1 Setup environment, test lulus, notebook regresi berjalan (±4 menit)
- [ ] D0.2 Baca `MATERI.md` §4, §9, §11
- [ ] D1.1 Pahami `PlayerPreprocessor`: pembulatan `level_liga`, log uang, imputasi regresi, penebak posisi KNN (slide) vs `SoftmaxClassifier` (soft), interaksi atribut × posisi, standarisasi
- [ ] D1.2 Verifikasi section 3 & 5 notebook regresi; jelaskan **kenapa interaksi posisi** menurunkan RMSE 1.28 → 0.42

**Fase 2**
- [ ] D2.1 Pahami `src/models/linear_regression.py`: GD batch/mini-batch, normal equation, L1 (subgradien), L2, bias tidak diregularisasi
- [ ] D2.2 Pahami kenapa GD biasa divergen pada lr besar (λ_max) dan lambat pada 477 fitur, serta kenapa Adam + lr_decay dipakai
- [ ] D2.3 Eksperimen E8/E9/E10 (`PANDUAN.md` §10.2), catat CV
- [ ] D2.4 Bonus optimizer LinReg: plot konvergensi GD vs Momentum vs Adam + penjelasan

**Fase 3**
- [ ] D3.1 Pemilik notebook regresi: integrasikan perubahan, Restart & Run All
- [ ] D3.2 Perbarui blok **Insight** bila angka berubah
- [ ] D3.3 Draf bab laporan: deskripsi dataset rating, preprocessing + alasan, Linear Regression + perbandingan LinearRegression/Ridge/Lasso + plot

---

## Fase 4 — Eksplorasi menaikkan skor Kaggle (mulai 19 Nov)

Skor saat ini: klasifikasi AUC **0,98856**, regresi RMSE **0,41161** (public LB). Prioritas utama adalah **regresi**, karena di sana masih ada ruang untuk turun. Kode ide (E1, E12, dst.) mengacu ke tabel `PANDUAN.md` §10.2. Aturannya mengikuti `PANDUAN.md` §10.1: ukur dengan 5-fold CV, ubah satu hal per percobaan, dan catat di `docs/log_eksperimen.md` (termasuk yang gagal).

### 4.0 Diagnosa regresi (dikerjakan leader 18 Nov, bahan untuk semua)

- **Error terbesar ada di mana?**: Porsi kuadrat error: baris lengkap **54%**, baris dengan kolom kosong 35%, posisi kosong 11%
  - Artinya: Memperbaiki penebak posisi saja tidak cukup; batas maksimal yang bisa dicapai dengan cara itu ±0,40
- **Baris tanpa data kosong pun masih salah?**: Ya. RMSE baris lengkap 0,412; regresi per posisi pada data latihnya sendiri pun masih 0,38–0,45
  - Artinya: Atribut teknis secara linear sudah "habis"; sisa informasinya ada di kolom **lain**
- **Kolom apa yang masih menyimpan sinyal?**: Residual berkorelasi dengan `nilai_pasar`, `klausul_pelepasan`, `gaji`, `potensi`. Dalam grup usia + potensi yang sama, korelasi log nilai pasar dengan rating **0,94**
  - Artinya: Nilai pasar adalah fungsi **tak-linear** dari rating, usia, dan potensi, sehingga bisa "dibalik" untuk menebak rating
- **Sudah dicoba?**: Bin 20 kuantil + x², x³ + interaksi × usia/potensi untuk 3 kolom uang: CV **0,4248 → 0,4122**
  - Artinya: Ide paling menjanjikan sejauh ini (E12)
- **Segmen dengan error tinggi**: `reputasi_internasional` = 3 (RMSE 0,72) dan rating ≥ 80 (MAE 0,52)
  - Artinya: Ada efek "bonus reputasi" yang belum tertangkap (E13)
- **Pembulatan ke integer?**: Target memang selalu integer, tetapi pembulatan memperburuk (0,42 → 0,50)
  - Artinya: Baru masuk akal setelah RMSE < ±0,25 (E17)

### 4.1 Pembagian eksplorasi

**Leader — M. Faris Daffa (C4.5, integrasi)**
- [ ] L4.1 (E15) Latih **C4.5 regresi/klasifikasi pada residual** model regresi (misalnya target = |residual| > 0,6) untuk menemukan segmen mana yang paling sering salah. Ini **alat diagnosa**, bukan bagian submisi (bukan ensemble). Hasil berupa aturan IF-THEN dibagikan ke Anggota D.
- [ ] L4.2 (E6) Tuning `min_samples_leaf` / Laplace C4.5 klasifikasi; analisis aturan hasil rule post-pruning untuk laporan.
- [ ] L4.3 Review & merge PR eksperimen; hanya submit ke Kaggle jika CV membaik (maks. kuota harian, lihat `PANDUAN.md` §9.2).

**Anggota A — Logistic Regression (+ softmax penebak posisi)**
- [ ] A4.1 (E8) Perbaiki **penebak posisi** (`SoftmaxClassifier` = logistic regression multikelas, jadi masih wilayahmu): tambah fitur `tinggi_cm`, `berat_kg`, `kaki_lemah`, `kaki_dominan`, `tipe_badan`; tuning `alpha`, `epochs`. Ukur akurasi posisi **dan** RMSE akhir. Target: akurasi > 0,70, RMSE baris posisi-kosong < 0,65.
- [ ] A4.2 (E4) Klasifikasi: fitur interaksi LogReg (`indeks_google × usia_domain`, `jumlah_hyperlink × peringkat_halaman`), jumlah bin 5/10/20, α Elastic Net.
- [ ] A4.3 (E5) Proximal L1 (ISTA) sebagai bonus optimizer.

**Anggota B — KNN**
- [ ] B4.1 (E1) Klasifikasi: *tie-breaking* skor KNN yang seri di 0 / 1 (misalnya + ε × jarak ke tetangga phishing terdekat). Ini peluang terbesar di klasifikasi karena AUC sensitif terhadap skor seri.
- [ ] B4.2 (E2, E3) Tuning `weighting_power`, k, Minkowski p = 1,5; bobot fitur dari information gain (hubungkan dengan C4.5 leader).
- [ ] B4.3 (E11) Klasifikasi: tambah indikator "nilai kosong" dan "WHOIS −1" sebagai fitur KNN.
- [ ] B4.4 (E16) Regresi: bandingkan **imputasi KNN** (cara slide) dengan imputasi regresi untuk `nilai_pasar` / `klausul_pelepasan`. Ini kolom yang paling penting setelah E12, jadi imputasi yang lebih akurat langsung berdampak.

**Anggota C — Naive Bayes + metrik + laporan**
- [ ] C4.1 (E7) Klasifikasi: jumlah bin per fitur, alpha, buang fitur yang saling berkorelasi.
- [ ] C4.2 (E17) Buat fungsi di `src/metrics.py` untuk **rincian error regresi per segmen** (posisi, kolom kosong, reputasi, rentang rating) sehingga tabel 4.0 bisa dibuat ulang otomatis setiap eksperimen. Uji juga strategi pembulatan setiap kali RMSE turun.
- [ ] C4.3 Rangkum semua eksperimen Fase 4 (yang berhasil & gagal) untuk bab laporan.

**Anggota D — Linear Regression (pemilik pipeline regresi)**
- [ ] D4.1 (E12) **Prioritas #1.** Pindahkan fitur uang tak-linear ke `PlayerPreprocessor` sebagai parameter (misalnya `money_features=True`): one-hot 20 bin kuantil + x², x³ + interaksi × `usia`, `usia²`, `potensi` untuk `nilai_pasar`, `gaji`, `klausul_pelepasan`, ditambah indikator kosong. Batas bin di-fit dari train saja. Verifikasi CV ≈ 0,412, lalu latih ulang dengan GD-Adam (cek konvergen vs normal equation).
- [ ] D4.2 (E13) Bonus reputasi: interaksi `reputasi_internasional` × posisi, tetapi **gabungkan dulu** level 3–5 menjadi satu (level 5 hanya 22 pemain). Percobaan tanpa penggabungan membuat skala meledak (RMSE 12).
- [ ] D4.3 (E9, E10) Interaksi atribut × `tipe_badan`; imputasi atribut kiper khusus kiper.
- [ ] D4.4 Setelah fitur bertambah, tuning ulang α L2 kecil (1e-5 s.d. 1e-3), karena model mungkin mulai overfit.
- [ ] D4.5 Pakai aturan dari L4.1 untuk menentukan fitur berikutnya.

---

## Penutupan (semua)

- [ ] Setiap anggota punya minimal 3 commit semantik di branch sendiri
- [ ] Setiap anggota bisa menjelaskan kode bagiannya tanpa membuka AI
- [ ] Semua bab laporan masuk ke Anggota C paling lambat **1 Des**
- [ ] Form Generative AI tiap anggota sudah diisi jujur
- [ ] Release `v1.0` dibuat dan link sudah dikumpulkan di Edunex (18224009)
