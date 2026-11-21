# Tugas Besar 2: Supervised Learning

IF3070 Dasar Inteligensi Artifisial 2026/2027

Dosen Pengampu: Dr. Nur Ulfa Maulidevi, S.T, M.Sc.  
Ir. Windy Gambetta, M.B.A

Dipersiapkan oleh Tim Asisten Laboratorium Inteligensi Artifisial 2023

Versi: 1.2 - 16/11/2026

Sistem pengerjaan: Take Home Berkelompok  
Deadline pengumpulan: **Kamis, 3 Desember 2026 22.22 WIB**

> **Catatan sinkronisasi (G08, 17 Nov 2026).** File ini adalah salinan teks dari `spek tubes ai 2.pdf` (16 halaman, versi 1.2). Sudah dicek halaman demi halaman terhadap PDF, dan isinya identik. Perbedaan yang perlu diketahui:
> 1. Halaman **Log Perubahan Dokumen**, **Timeline**, dan **Salam dari Asisten** tercantum di Daftar Isi, tetapi **tidak ada** di PDF yang kita simpan.
> 2. PDF berisi **hyperlink** yang hilang saat dikonversi: sheet kelompok, link Kaggle Klasifikasi & Regresi, template notebook ("tautan ini"), panduan semantic commit, Panduan AI ITB, dan slide kuliah di Referensi. Buka PDF atau Teams untuk link-nya.
> 3. Penekanan (teks **tebal**/merah) di PDF sudah dikembalikan di file ini.
> 4. Info Kaggle yang tidak ada di spek (metrik ROC-AUC/RMSE, rumus skor, format submisi) ada di `desc klasifikasi.md` dan `desc regresi.md` (folder yang sama). Ringkasan semua aturan ada di `../CONSTRAINT.md`.

## Daftar Isi

Log Perubahan Dokumen 2  
Daftar Isi 3  
Tujuan 4  
Aturan 5  
Deliverables 6  
Timeline 7  
Deskripsi 8  
Spesifikasi 10  
Deskripsi Dataset 10  
Tahapan Pengolahan Data 10  
Cakupan 12  
Bonus 14  
Referensi 16  
Salam dari Asisten 19

## Tujuan

Tugas Besar II pada kuliah IF3070 Dasar Intelegensi Artifisial bertujuan agar peserta kuliah mendapatkan wawasan tentang bagaimana cara mengimplementasikan dan mengevaluasi algoritma-algoritma supervised learning untuk menyelesaikan permasalahan berupa studi kasus yang relevan terhadap industri.

Pada tugas ini peserta akan merancang, mengimplementasikan beberapa varian algoritma supervised learning, melakukan eksperimen, dan menganalisis hasilnya.

## Aturan

Terdapat beberapa hal yang perlu diperhatikan dalam pengerjaan tugas ini:

1. Tugas besar dilaksanakan **secara berkelompok**. Pembagian kelompok ditentukan sendiri oleh mahasiswa dengan mengisi sheet kelompok berikut ini dengan 1 kelompok terdiri dari **5 mahasiswa** yang dapat berasal dari lintas kelas. Batas waktu pengisian kelompok adalah Senin, 16 November 2026 pukul 22.22 WIB. Silakan lihat instruksi lebih lanjut di sheets kelompok di atas.

2. **Utamakan implementasi yang mengacu pada salindia kuliah.** Apabila menggunakan atau mengadaptasi metode dari sumber di Internet, **sumber tersebut wajib dicantumkan** dalam bentuk komentar pada program serta referensinya pada laporan.

3. Jika terdapat hal yang kurang dipahami, peserta dapat mengajukan pertanyaan kepada asisten melalui **komentar pada Unggahan Tugas Besar di Teams**. Pertanyaan yang diajukan secara personal kepada asisten tidak akan dijawab untuk menghindari perbedaan informasi yang diterima.

4. Dilarang melakukan plagiarisme, meminta atau memberikan kode dan/atau laporan kepada kelompok lain, dan alasan penggunaan LLM tidak dapat diterima. Pelanggaran terhadap aturan ini akan mengakibatkan **pemberian nilai E** kepada seluruh anggota kelompok yang terlibat.

## Deliverables

Berikut deliverables dalam pengerjaan tugas ini:

1. Untuk tugas ini, setiap kelompok diwajibkan menggunakan version control system Git dengan membuat repository pada GitHub (akun pribadi). Format penamaan repository adalah **IF3070_GXX_NamaKelompok**, dengan XX merupakan nomor kelompok yang terdapat pada sheet kelompok. Repository dapat bersifat private selama masa pengerjaan dan **wajib diubah menjadi public** sebelum pengumpulan agar dapat diakses oleh asisten.

2. Meskipun commit dan development tidak dinilai secara langsung, setiap kelompok diharapkan melakukan commit dan branching yang mengikuti best practice. Disarankan menggunakan semantic commit agar kontribusi tiap anggota dapat terlihat dengan jelas.

3. Repository harus memiliki struktur sebagai berikut:

   - Folder src, digunakan untuk menyimpan source code.
   - Folder docs, digunakan untuk menyimpan laporan dalam bentuk .pdf yang terdiri atas komponen berikut:
     - Cover
     - Deskripsi Persoalan yang berisi pemahaman terhadap dataset
     - Pembahasan yang berisi penjelasan implementasi setiap algoritma (berisi deskripsi fungsi/kelas beserta source code), tahap cleaning dan preprocessing beserta alasannya, serta hasil dan analisis perbandingan dengan pustaka menggunakan metrics yang sesuai (disertai visualisasi)
     - Kesimpulan dan Saran
     - Pembagian tugas tiap anggota kelompok
     - Referensi
     - Lampiran Form Penggunaan Generative AI yang diisi dengan sejujur-jujurnya (Halaman 19 pada Panduan AI ITB). Apabila terdapat indikasi kecurangan atau ketidakjujuran, maka akan **ditindaklanjuti sesuai hukum yang berlaku**.
   - Folder output, digunakan untuk menyimpan hasil run algoritma.
   - README.md, yang berisi deskripsi singkat repository, cara setup dan run program, dan pembagian tugas tiap anggota kelompok.

4. Pengumpulan dilakukan dengan membuat release dengan tag **vX.Y** pada repository sebelum deadline, dengan **X adalah nomor milestone dan Y adalah angka revisi** yang dimulai dari 0 untuk versi awal. Tautan release dikumpulkan melalui formulir pada Edunex oleh anggota dengan NIM terkecil. Pengumpulan yang melewati deadline akan dikenakan **pengurangan nilai**.

## Deskripsi

B.O.A.T  
Ballon D’Or of All Time  
WINNER  
Saya sangat suka Decision Trees karena distribution invariancenya  
1. Cristiano Ronaldo 2008  
2. Lionel Messi 2012  
3. Cristiano Ronaldo 2017  
4. Lionel Messi 2023  
5. Cristiano Ronaldo 2016  
Cristiano RONALDO  
Asisten Lab AI 23  
Aku sayang LAB AI

Gambar 1. Cristiano Ronaldo, GOAT/BOAT (Sumber: @FabrizioRomano)

### Prologue

Q: ええ、なんで急にサッカーとフィッシングの話になったの？  
A: 世界を救うのにジャンルなんて関係ないからね。

Di tengah meningkatnya popularitas sepak bola dan maraknya aktivitas perjudian online, masyarakat semakin sering dihadapkan pada berbagai situs yang menawarkan prediksi pertandingan dengan iming-iming keuntungan besar. Sayangnya, tidak sedikit dari situs tersebut yang justru menjadi sarana penipuan, pencurian data pribadi, hingga praktik perjudian online ilegal.

Melihat fenomena tersebut, sebuah organisasi independen bernama GOATBANGET™ (Greatest Of All Time: Better Education in Technology) hadir dengan misi mulia: mengedukasi masyarakat mengenai sepak bola berbasis data sekaligus memberantas ancaman digital yang merugikan pengguna internet.

Namun, misi tersebut tidak berjalan semulus tendangan bebas Cristiano Ronaldo. Sejumlah situs phishing mulai bermunculan dengan menyamar sebagai platform analisis sepak bola, sementara situs-situs perjudian ilegal semakin lihai memanfaatkan berbagai celah untuk menjaring korban.

Merasa perlu mengambil tindakan, CEO GOATBANGET™ akhirnya meminta bantuan Lab AI ¹ (eMudhra² + CRO) STEI ITB untuk mengembangkan dua sistem cerdas: sistem phishing detection yang mampu mengidentifikasi situs berbahaya berdasarkan karakteristik URL dan fitur lainnya, serta sistem football match prediction yang dapat memperkirakan hasil pertandingan berdasarkan statistik, performa tim, dan data historis. Sistem prediksi ini diharapkan dapat menjadi sarana edukasi analisis sepak bola berbasis data, bukan untuk mendukung aktivitas perjudian.

Karena Lab AI 23 sedang sibuk mengamankan multiverse dari ancaman VAR yang korup dan harus bekerja dalam bayang-bayang, tugas mulia ini akhirnya diserahkan kepada para member akademi La Fabrica (kalian).

Oleh karena itu, bantulah GOATBANGET™ dan para asisten Lab AI dalam membangun kedua sistem tersebut. Bersama-sama, kita wujudkan ekosistem sepak bola digital yang lebih aman, cerdas, dan bebas dari ancaman penipuan maupun perjudian ilegal.

Ingat, tidak semua prediksi bisa menjadi kenyataan, tetapi setiap ancaman digital bisa kita pelajari dan antisipasi.

Protect the internet, respect the game, and never trust a suspicious URL!

## Spesifikasi

Pembelajaran mesin merupakan salah satu cabang dari kecerdasan buatan yang memungkinkan sistem untuk belajar dari data dan membuat prediksi atau keputusan tanpa diprogram secara eksplisit.

### Deskripsi Dataset

Dataset yang digunakan terdiri dari dua bagian. Bagian pertama berisi data klasifikasi situs phishing, dengan fitur yang menggambarkan struktur URL, teks, dan konten halaman. Bagian kedua berisi data regresi rating pemain sepak bola, dengan fitur profil, atribut teknis, dan atribut kiper. Keduanya memuat fitur numerik dan kategorikal sehingga Anda perlu memahami konteks setiap fitur dan menyesuaikan tipe serta nilainya sebelum data diproses. Deskripsi fitur dan target dataset dapat dilihat di Kaggle Klasifikasi dan Regresi.

### Tahapan Pengolahan Data

Untuk menghasilkan prediksi yang berkualitas, Anda diharuskan untuk melakukan beberapa tahap berikut:

- Data Cleaning  
  Tahap ini bertujuan untuk membersihkan dataset dari nilai yang hilang (missing values), data duplikat, atau data yang tidak valid sehingga dataset siap digunakan untuk analisis.

- Data Transformation  
  Transformasi data melibatkan langkah-langkah seperti encoding variabel kategori, normalisasi atau standarisasi fitur numerik, serta penanganan ketidakseimbangan data (imbalanced data) untuk memastikan data berada dalam format yang sesuai dengan algoritma pembelajaran mesin.

- Feature Selection  
  Pemilihan fitur yang relevan bertujuan untuk mengurangi kompleksitas model, menghindari overfitting, serta meningkatkan kinerja model. Langkah ini melibatkan identifikasi fitur yang memiliki pengaruh signifikan terhadap variabel target.

- Dimensionality Reduction  
  Jika dataset memiliki jumlah fitur yang besar, reduksi dimensi dapat digunakan untuk mengurangi dimensi tanpa kehilangan informasi penting. Teknik seperti Principal Component Analysis (PCA) sering digunakan pada tahap ini.

- Modeling dan Validation  
  Pada tahap ini, algoritma pembelajaran mesin seperti KNN, DTL, Logistic Regression, Naive Bayes, dan Linear Regression diterapkan pada dataset. Anda akan melatih model pembelajaran mesin yang akan mengklasifikasi fitur ‘Target’ berdasarkan fitur-fitur lain yang telah diberikan. Model yang telah dibuat divalidasi menggunakan metode seperti train-test split atau k-fold cross-validation untuk memastikan kinerja yang optimal.

Tahap preprocessing dilakukan secara terpisah pada training data dan test data. Kedua data tersebut tidak boleh digabungkan.

## Cakupan

Pada tugas ini, Anda diminta untuk mengimplementasikan algoritma pembelajaran mesin yang telah kalian pelajari di kuliah, yaitu KNN, DTL, Logistic Regression, dan Bayesian Network (Naive Bayes) pada dataset yang sudah dijelaskan. Berikut merupakan hal-hal yang perlu dilakukan oleh setiap kelompok:

1. Implementasikan Decision Tree Learning (DTL) from scratch. Algoritma seminimal mungkin harus dapat menangani tipe data numerik dan categorical serta dapat menangani null values. Pilih salah satu algoritma DTL berikut.

   a. Iterative Dichotomiser 3 (ID3)  
   b. C4.5  
   c. Classification and Regression Tree (CART)

2. Pilih antara:

   a. Implementasikan Logistic Regression from scratch. Buat juga regularisasi berikut:  
   i. L1 regularization  
   ii. L2 regularization  
   iii. Elastic Net

   b. Implementasikan KNN from scratch.

3. Implementasikan Naive Bayes from scratch.

4. Implementasikan algoritma poin 1–3 menggunakan scikit-learn. Bandingkan hasil dari algoritma from scratch dan algoritma scikit-learn. Untuk DTL, gunakan DecisionTreeClassifier dengan parameter berikut:

   a. ID3: criterion=’entropy’  
   b. C4.5: criterion=’entropy’ dan tambahkan ccp_alpha  
   c. CART: criterion=’gini’

5. Implementasikan Linear Regression from scratch untuk task regresi dengan ketentuan berikut.

   a. Pelatihan menggunakan gradient descent (batch atau mini-batch). Normal equation boleh ditambahkan sebagai pembanding.

   b. Buat juga regularisasi berikut:  
   i. L2 regularization  
   ii. L1 regularization

   c. Lakukan standarisasi fitur numerik sebelum pelatihan. Bias/intercept tidak ikut diregularisasi.

   d. Bandingkan hasilnya dengan LinearRegression, Ridge, dan Lasso dari scikit-learn menggunakan metrics regresi yang sesuai, minimal MAE, RMSE, dan R², disertai visualisasi (misalnya predicted vs actual dan residual plot).

6. Model harus bisa di-save dan di-load. Implementasinya dibebaskan.

7. Kaggle Submission pada Kaggle Klasifikasi dan Regresi minimal 1 submission.

Untuk poin 2–5, algoritma optimasi model selain yang diajarkan di kelas akan dihitung sebagai bonus.

Implementasi KNN, DTL, Logistic Regression, Naive Bayes, dan Linear Regression from scratch dapat dibuat dalam bentuk kelas (class KNN, dst.) yang nantinya akan di-import ke notebook pengerjaan. Templat notebook pengerjaan dapat diakses pada tautan ini. Untuk implementasi from scratch, library yang boleh digunakan adalah untuk perhitungan matematika saja, seperti NumPy dan sejenisnya.

**Konfirmasi library yang boleh digunakan dapat dilakukan melalui QnA.**

Notebook yang dikumpulkan harus reproducible, yaitu menghasilkan nilai akhir yang sama dengan submisi Kaggle ketika dijalankan ulang oleh asisten. Apabila tidak reproducible, poin Bonus Kaggle dianulir dan poin Kaggle Submission bernilai 0.

## Bonus

Hanya kerjakan spesifikasi ini jika Anda sudah menyelesaikan seluruh spesifikasi wajib. Bonus yang dihitung maksimum 20 poin. Berikut merupakan beberapa spesifikasi bonus yang dapat Anda kerjakan:

1. Bonus Kaggle (1–5 poin)

   Nilai diberikan berdasarkan peringkat leaderboard **Kaggle (70% Classification dan 30% Regression)**. Dalam leaderboard, gunakan nama kelompok. Identifikasi dilakukan berdasarkan nama kelompok, jadi cukup 1 orang saja yang berada dalam tim Kaggle. Hasil prediksi di Kaggle harus reproducible sehingga notebook yang dikumpulkan harus bisa menghasilkan nilai akhir yang sama dengan submisi Kaggle. **Model yang boleh digunakan hanya KNN, DTL, Logistic Regression, dan Naive Bayes yang diimplementasikan from scratch (tanpa ensemble).**

   > *Catatan G08:* daftar ini tidak menyebut Linear Regression, padahal submisi regresi wajib dan model regresi yang diwajibkan adalah Linear Regression from scratch. Kita memakai Linear Regression from scratch untuk regresi; sebaiknya dikonfirmasi di QnA. Lihat `CONSTRAINT.md` K-07. Poin diberikan sebagai berikut:

   a. Rank 1–3: 5 poin  
   b. Rank 4–5: 3 poin  
   c. Rank 6–10: 1 poin

2. DTL (2 poin)

   Hasilkan gambar percabangan tree (format berkas dibebaskan). Tambahkan parameter untuk mengatur top-N percabangan yang ditampilkan dalam gambar.

3. Logistic Regression (2 poin)

   Hasilkan video yang menampilkan garis kontur fungsi loss (log-loss) dan lintasan parameter (θ₀, θ₁) selama training.

4. Naive Bayes (2 poin)

   Hasilkan gambar graf yang menampilkan hubungan antarfitur dan variabel kelas.

5. Algoritma poin 2–4 (2 poin per algoritma, maksimum 6 poin)

   Implementasikan algoritma untuk mengoptimasi model (selain algoritma yang telah diajarkan di kelas). Jelaskan bagaimana algoritma tersebut dapat mengoptimasi model. Sertakan juga referensi/sumbernya **(tanpa referensi, poin bonus ini dianulir)**.

6. Cost-sensitive classification (3 poin)

   Tidak semua kesalahan prediksi bernilai sama. Pada klasifikasi phishing ini, False Negative (phishing lolos) lebih mahal daripada False Positive (alarm palsu), karena kredensial pengguna bisa dicuri. Asumsikan biaya False Negative dua kali biaya False Positive.

   Bagaimana penanganan Anda berubah? Jelaskan pilihan ambang keputusan, pembobotan kelas, atau pendekatan lain, lalu bandingkan dampaknya terhadap biaya keseluruhan dan metrik evaluasi. Tambahkan bagian ini di notebook dan cantumkan analisisnya di laporan Anda.

7. Plis baca lorenya :) 🙏 [100 obrigado]

## Referensi

[1] N. U. Maulidevi, "Introduction to Learning and Supervised Learning," IF3170 Inteligensi Artifisial, Edunex ITB, 2026. [Online]. Available: Slide Introduction to Learning. [Accessed: Nov. 2, 2026].

[2] F. Z. Ruskanda, "CRISP-DM dan Data Understanding," IF3170 Inteligensi Artifisial, Edunex ITB, 2026. [Online]. Available: Slide CRISP-DM dan Data Understanding. [Accessed: Nov. 2, 2026].

[3] E. Ferdian, "Data Preparation," IF3170 Inteligensi Artifisial, Edunex ITB, 2026. [Online]. Available: Slide Data Preparation. [Accessed: Nov. 2, 2026].

[4] E. Ferdian, "KNN," IF3170 Inteligensi Artifisial, Edunex ITB, 2026. [Online]. Available: Slide KNN. [Accessed: Nov. 2, 2026].

[5] N. U. Maulidevi, "Bayes Net," IF3170 Inteligensi Artifisial, Edunex ITB, 2024. [Online]. Available: Slide Bayes Net. [Accessed: Nov. 2, 2026].

[6] N. U. Maulidevi, "IF3270 DTL-01: Attribute Types," YouTube, 2021. [Video]. Available: https://www.youtube.com/watch?v=UkZjVkVqUrQ. [Accessed: Nov. 2, 2026].

[7] N. U. Maulidevi, "IF3270 DTL-02: What, Why, and When," YouTube, 2021. [Video]. Available: https://www.youtube.com/watch?v=zBUe2ma_14A. [Accessed: Nov. 2, 2026].

[8] N. U. Maulidevi, "IF3270 DTL-03: Basic DTL Algorithm (ID3)," YouTube, 2021. [Video]. Available: https://www.youtube.com/watch?v=uSTgx9NiEHQ. [Accessed: Nov. 2, 2026].

[9] N. U. Maulidevi, "IF3270 DTL-04: Information Gain," YouTube, 2021. [Video]. Available: https://www.youtube.com/watch?v=aVE7xQJNuCA. [Accessed: Nov. 2, 2026].

[10] N. U. Maulidevi, "IF3270 Issues in DTL-01: Overfitting," YouTube, 2021. [Video]. Available: https://www.youtube.com/watch?v=hkxC117tEu4. [Accessed: Nov. 2, 2026].

[11] N. U. Maulidevi, "IF3270 Issues in DTL-02: Continuous-valued Attribute," YouTube, 2021. [Video]. Available: https://www.youtube.com/watch?v=7x-62KqjO4k. [Accessed: Nov. 2, 2026].

[12] N. U. Maulidevi, "IF3270 Issues in DTL-03: Missing Attribute Values," YouTube, 2021. [Video]. Available: https://www.youtube.com/watch?v=ZR7lOFYZLF8. [Accessed: Nov. 2, 2026].

[13] N. U. Maulidevi, "IF3270 Issues in DTL-04: Alternative Measures for Selecting Attribute," YouTube, 2021. [Video]. Available: https://www.youtube.com/watch?v=4_Ueiuchxrk. [Accessed: Nov. 2, 2026].

[14] N. U. Maulidevi, "IF3270 Issues in DTL-05: Attributes with Differing Costs," YouTube, 2021. [Video]. Available: https://www.youtube.com/watch?v=GxH3xjtCFcY. [Accessed: Nov. 2, 2026].

[15] M. L. Khodra, "Logistic Regression: What & Why," YouTube, 2021. [Video]. Available: https://www.youtube.com/watch?v=QAKZ_pymEzc. [Accessed: Nov. 2, 2026].

[16] M. L. Khodra, "Logistic Regression: Stochastic Gradient Ascent," YouTube, 2021. [Video]. Available: https://www.youtube.com/watch?v=O5NSNMQO1yU. [Accessed: Nov. 2, 2026].

[17] F. Z. Ruskanda, "SVM: What & Why?," YouTube, 2021. [Video]. Available: https://www.youtube.com/watch?v=-aNlqGRdQy4. [Accessed: Nov. 2, 2026].

[18] F. Z. Ruskanda, "SVM for Linearly Separable Data," YouTube, 2021. [Video]. Available: https://www.youtube.com/watch?v=RTcwgAlUwlo. [Accessed: Nov. 2, 2026].

[19] F. Z. Ruskanda, "SVM for Non-linearly Separable Data," YouTube, 2021. [Video]. Available: https://www.youtube.com/watch?v=4kK5UJV-LhE. [Accessed: Nov. 2, 2026].

[20] F. Z. Ruskanda, "SVM for Multi-Class Data," YouTube, 2021. [Video]. Available: https://www.youtube.com/watch?v=Jf7pjSMx14s. [Accessed: Nov. 2, 2026].

[21] P. Cunningham and S. J. Delany, "k-Nearest Neighbour Classifiers: 2nd Edition (with Python examples)," arXiv:2004.04523, 2020. [Online]. Available: https://arxiv.org/abs/2004.04523. [Accessed: Nov. 2, 2026].

[22] GeeksforGeeks, "Iterative Dichotomiser 3 (ID3) Algorithm From Scratch," GeeksforGeeks. [Online]. Available: https://www.geeksforgeeks.org/machine-learning/iterative-dichotomiser-3-id3-algorithm-from-scratch/. [Accessed: Nov. 2, 2026].

[23] GeeksforGeeks, "CART (Classification And Regression Tree) in Machine Learning," GeeksforGeeks. [Online]. Available: https://www.geeksforgeeks.org/machine-learning/cart-classification-and-regression-tree-in-machine-learning/. [Accessed: Nov. 2, 2026].

[24] GeeksforGeeks, "Decision Tree Algorithms," GeeksforGeeks. [Online]. Available: https://www.geeksforgeeks.org/machine-learning/decision-tree-algorithms/. [Accessed: Nov. 2, 2026].

[25] GeeksforGeeks, "Support Vector Machine (SVM) Algorithm," GeeksforGeeks. [Online]. Available: https://www.geeksforgeeks.org/machine-learning/support-vector-machine-algorithm/. [Accessed: Nov. 2, 2026].

[26] GeeksforGeeks, "Logistic Regression in Machine Learning," GeeksforGeeks. [Online]. Available: https://www.geeksforgeeks.org/machine-learning/understanding-logistic-regression/. [Accessed: Nov. 2, 2026].
