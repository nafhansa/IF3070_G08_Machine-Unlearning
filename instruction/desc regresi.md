Overview
Prediksi Rating Pemain
Tugas Besar 2 · IF3070 Dasar Inteligensi Artifisial 2026/2027

Rating pemain sering menjadi ringkasan pertama yang dilihat klub, pencari bakat, dan pelatih ketika menilai seorang pemain. Di balik satu angka itu ada kombinasi atribut teknis, fisik, dan pengalaman; perbedaan posisi serta level kompetisi membuat penilaian yang konsisten tidak selalu mudah.

Dalam kompetisi ini, Anda akan membangun model yang memperkirakan rating keseluruhan seorang pemain dari atribut yang tersedia. Tantangannya adalah menghasilkan perkiraan yang wajar untuk pemain dari posisi dan level kompetisi yang berbeda, bukan hanya mengikuti contoh yang ada.

Hasil yang Anda kirimkan adalah perkiraan rating untuk setiap pemain di data uji. Fokus kompetisi ini adalah seberapa dekat perkiraan tersebut dengan rating sebenarnya pada pemain yang belum Anda lihat.

Start

5 days ago
Close

16 days to go
Description
Panduan Singkat
Unduh train.csv dan test.csv dari tab Data.
Latih model regresi pada train.csv, lalu prediksi target untuk setiap baris test.csv.
Unggah submission dengan kolom id,target; format lengkap ada di halaman Evaluation.
Evaluation
Evaluasi
Submission dinilai dengan RMSE antara prediksi dan rating asli. Semakin kecil, semakin baik. Baseline tebakan rata-rata: 6,9676.

Submission
Satu baris per id di test.csv:

id,target
a1b2c3d4,72.4
target adalah angka rating, bukan label kelas.

Leaderboard
Public leaderboard memakai 30% data uji; private leaderboard memakai 70%. Nilai akhir Tugas Besar:

AUC_norm  = clip((AUC - 0,5) / 0,5, 0, 1)
RMSE_norm = clip(1 - RMSE / 6,9676, 0, 1)
Skor      = 0,7 * AUC_norm + 0,3 * RMSE_norm



Dataset Description
Data
Ringkasan
Dataset ini berisi 18.405 pemain dengan 48 fitur profil, teknis, dan kiper. Data pelatihan berisi 12.883 baris; data pengujian berisi 5.522 baris. Target target adalah rating overall 47–91.

Berkas
Berkas	Baris	Ukuran	Isi
train.csv	12.883	2.51 MB	Fitur dan target
test.csv	5.522	1.06 MB	Fitur
sample_submission.csv	5.522	92 KB	Template submission
Target
target adalah rating overall pemain, bernilai 47–91. Kolom ini hanya tersedia di train.csv.

Kamus Data
Profil
Fitur	Tipe	Contoh	Deskripsi
potensi	numerik	61	Rating potensi maksimum pemain.
nilai_pasar	numerik	2,116,922	Nilai pasar pemain dalam euro.
gaji	numerik	505	Gaji pemain dalam euro.
usia	numerik	35	Usia pemain dalam tahun.
tinggi_cm	numerik	191	Tinggi badan pemain dalam sentimeter.
berat_kg	numerik	87	Berat badan pemain dalam kilogram.
level_liga	numerik	1	Tingkat liga tempat pemain bermain.
kaki_lemah	numerik	1	Rating kemampuan kaki lemah (1–5).
gerakan_skill	numerik	1	Rating gerakan skill (1–5).
reputasi_internasional	numerik	1	Rating reputasi internasional (1–5).
klausul_pelepasan	numerik	62,003	Nilai klausul pelepasan kontrak dalam euro.
Atribut teknis dan fisik
Fitur	Tipe	Contoh	Deskripsi
akselerasi	numerik	31	Kemampuan mencapai kecepatan maksimum.
kecepatan_sprint	numerik	30	Kecepatan lari maksimum.
penyelesaian	numerik	18	Akurasi penyelesaian peluang.
kekuatan_tembakan	numerik	46	Kekuatan tembakan.
tembakan_jarak_jauh	numerik	16	Akurasi tembakan jarak jauh.
posisi_mental	numerik	10	Kemampuan mengambil posisi.
tendangan_voli	numerik	17	Akurasi tendangan voli.
penalti	numerik	13	Akurasi tendangan penalti.
umpan_silang	numerik	12	Akurasi umpan silang.
umpan_pendek	numerik	21	Akurasi umpan pendek.
umpan_panjang	numerik	27	Akurasi umpan panjang.
visi	numerik	55	Visi permainan.
akurasi_tendangan_bebas	numerik	12	Akurasi tendangan bebas.
lengkung_bola	numerik	17	Kemampuan memberi efek lengkung pada bola.
skill_dribel	numerik	18	Kemampuan dribel.
kontrol_bola	numerik	18	Kontrol bola.
kelincahan	numerik	26	Kelincahan.
keseimbangan	numerik	33	Keseimbangan.
reaksi	numerik	61	Kecepatan reaksi.
ketenangan	numerik	38	Ketenangan di bawah tekanan.
intersepsi	numerik	16	Kemampuan intersepsi.
akurasi_sundulan	numerik	14	Akurasi sundulan.
kesadaran_menjaga	numerik	14	Kesadaran menjaga lawan.
tekel_berdiri	numerik	11	Kemampuan tekel berdiri.
tekel_meluncur	numerik	15	Kemampuan tekel meluncur.
lompatan	numerik	46	Kemampuan melompat.
stamina	numerik	38	Stamina.
kekuatan	numerik	48	Kekuatan fisik.
agresivitas	numerik	32	Agresivitas.
Kiper
Fitur	Tipe	Contoh	Deskripsi
kiper_menyelam	numerik	59	Kemampuan kiper menyelam.
kiper_menangkap	numerik	62	Kemampuan kiper menangkap bola.
kiper_menendang	numerik	62	Kemampuan kiper menendang bola.
kiper_posisi	numerik	62	Kemampuan kiper mengambil posisi.
kiper_refleks	numerik	63	Refleks kiper.
Kategorikal
Fitur	Tipe	Contoh	Deskripsi
posisi_utama	kategorikal	Kiper	Posisi utama pemain (Kiper, Bek Tengah, Gelandang, Penyerang).
kaki_dominan	kategorikal	Kanan	Kaki dominan pemain (Kiri/Kanan).
tipe_badan	kategorikal	Normal (185+)	Tipe badan pemain (Normal, Kurus, Kekar, Unik).
Submission
Berkas submission.csv berisi id,target, satu baris untuk setiap ID di test.csv. target adalah angka rating.

id,target
a1b2c3d4,72.4
Catatan
Baca id sebagai teks. Submission harus memuat setiap ID tepat satu kali.