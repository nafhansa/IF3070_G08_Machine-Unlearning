Overview
Deteksi Situs Phishing
Tugas Besar 2 · IF3070 Dasar Inteligensi Artifisial 2026/2027

Situs phishing sering meniru halaman login layanan yang dipercaya, sehingga pengguna bisa memasukkan kata sandi atau data pribadi tanpa menyadari bahwa halaman itu palsu. Pemeriksaan manual tidak mudah dilakukan dalam jumlah besar, sementara pola URL terus berubah dan tidak selalu terlihat mencurigakan pada pandangan pertama.

Dalam kompetisi ini, Anda akan membangun model yang memperkirakan peluang sebuah URL merupakan situs phishing. Tantangannya adalah membuat perkiraan yang tetap berguna ketika pola URL berbeda dari contoh yang Anda pelajari.

Hasil yang Anda kirimkan adalah perkiraan peluang untuk setiap URL di data uji. Fokus kompetisi ini adalah kualitas perkiraan pada URL yang belum pernah Anda lihat.

Start

7 days ago
Close

16 days to go
Description
Panduan Singkat
Unduh train.csv dan test.csv dari tab Data.
Latih model pada train.csv, lalu prediksi probabilitas target untuk setiap baris test.csv.
Unggah submission dengan kolom id,target; format lengkap ada di halaman Evaluation.
Evaluation
Evaluasi
Submission dinilai dengan ROC AUC antara probabilitas prediksi dan label asli. Nilai 0,5 setara tebakan acak; 1,0 sempurna.

Submission
Satu baris per id di test.csv:

id,target
a1b2c3d4,0.87
target adalah probabilitas antara 0 dan 1, bukan label 0/1.

Leaderboard
Public leaderboard memakai 30% data uji; private leaderboard memakai 70%. Nilai akhir Tugas Besar adalah 70% AUC ternormalisasi pada track ini dan 30% RMSE ternormalisasi pada track regresi.


Dataset Description
Data
Ringkasan
Dataset ini berisi 11.430 URL dengan 81 fitur struktur, teks, dan konten halaman. Data pelatihan berisi 8.021 baris; data pengujian berisi 3.409 baris. Target target bernilai 1 untuk phishing dan 0 untuk legitimate.

Berkas
Berkas	Baris	Ukuran	Isi
train.csv	8.021	2.43 MB	Fitur dan target
test.csv	3.409	1.03 MB	Fitur
sample_submission.csv	3.409	43 KB	Template submission
Target
target bernilai 1 untuk phishing dan 0 untuk legitimate. Kolom ini hanya tersedia di train.csv.

Kamus Data
Struktur URL
Fitur	Tipe	Contoh	Deskripsi
panjang_url	integer	20	Panjang URL dalam karakter.
panjang_hostname	integer	13	Panjang hostname dalam karakter.
alamat_ip	integer	0	1 jika hostname berupa alamat IP, 0 jika bukan.
jumlah_titik	integer	2	Jumlah karakter titik (.) pada URL.
jumlah_tanda_hubung	integer	0	Jumlah karakter hyphen (-).
jumlah_at	integer	0	Jumlah karakter @.
jumlah_tanda_tanya	integer	0	Jumlah karakter ?.
jumlah_dan	integer	0	Jumlah karakter &.
jumlah_sama_dengan	integer	0	Jumlah karakter =.
jumlah_garis_bawah	integer	0	Jumlah karakter garis bawah (_).
jumlah_tilde	integer	0	Jumlah karakter tilde (~).
jumlah_persen	integer	0	Jumlah karakter persen (%).
jumlah_garis_miring	integer	2	Jumlah karakter garis miring (/).
jumlah_bintang	integer	0	Jumlah karakter bintang (*).
jumlah_titik_dua	integer	0	Jumlah karakter titik dua (:).
jumlah_koma	integer	0	Jumlah karakter koma (,).
jumlah_titik_koma	integer	0	Jumlah karakter titik koma (;).
jumlah_dolar	integer	0	Jumlah karakter dolar ($).
jumlah_spasi	integer	0	Jumlah karakter spasi.
jumlah_www	integer	0	Jumlah kemunculan "www".
jumlah_com	integer	0	Jumlah kemunculan ".com".
jumlah_garis_miring_ganda	integer	0	Jumlah kemunculan "//".
http_di_path	integer	0	Jumlah kemunculan "http" pada path URL.
token_https	integer	0	1 jika URL memuat token "https", 0 jika tidak.
rasio_digit_url	float	0	Rasio digit terhadap panjang URL.
rasio_digit_host	float	0	Rasio digit terhadap panjang hostname.
domain_punycode	integer	0	1 jika domain menggunakan punycode.
port_nonstandar	integer	0	1 jika URL memakai port nonstandar.
tld_di_path	integer	0	1 jika top-level domain muncul di path.
tld_di_subdomain	integer	0	1 jika top-level domain muncul di subdomain.
subdomain_abnormal	integer	0	1 jika struktur subdomain tidak normal.
jumlah_subdomain	integer	1	Jumlah subdomain pada hostname.
awalan_akhiran	integer	0	1 jika domain memakai awalan/akhiran hyphen.
domain_acak	integer	0	1 jika domain tampak dibangkitkan secara acak.
layanan_pemendek	integer	0	1 jika URL memakai layanan pemendek URL.
ekstensi_path	integer	0	1 jika path diakhiri ekstensi berkas.
jumlah_redirect	integer	3	Jumlah redirect yang terdeteksi.
jumlah_redirect_eksternal	integer	0	Jumlah redirect menuju domain eksternal.
Domain dan teks
Fitur	Tipe	Contoh	Deskripsi
panjang_kata_mentah	integer	3	Total panjang kata pada URL mentah.
pengulangan_karakter	integer	4	Jumlah karakter yang berulang.
kata_terpendek_mentah	integer	3	Panjang kata terpendek pada URL mentah.
kata_terpendek_host	integer	4	Panjang kata terpendek pada hostname.
kata_terpendek_path	integer	0	Panjang kata terpendek pada path.
kata_terpanjang_mentah	integer	6	Panjang kata terpanjang pada URL mentah.
kata_terpanjang_host	integer	6	Panjang kata terpanjang pada hostname.
kata_terpanjang_path	integer	0	Panjang kata terpanjang pada path.
rata_kata_mentah	float	3.983	Rata-rata panjang kata pada URL mentah.
rata_kata_host	float	3.963	Rata-rata panjang kata pada hostname.
rata_kata_path	float	0	Rata-rata panjang kata pada path.
petunjuk_phishing	integer	0	Jumlah kata kunci yang lazim pada situs phishing.
domain_di_merek	integer	0	1 jika nama domain memuat nama merek.
merek_di_subdomain	integer	0	1 jika nama merek muncul di subdomain.
merek_di_path	integer	0	1 jika nama merek muncul di path.
tld_mencurigakan	integer	0	1 jika top-level domain termasuk kategori mencurigakan.
laporan_statistik	integer	0	1 jika domain tercatat di laporan statistik phishing.
Konten halaman
Fitur	Tipe	Contoh	Deskripsi
jumlah_hyperlink	integer	333	Jumlah hyperlink pada halaman.
rasio_hyperlink_internal	float	1	Rasio hyperlink yang menuju domain internal.
rasio_hyperlink_eksternal	float	0.009011	Rasio hyperlink yang menuju domain eksternal.
jumlah_css_eksternal	integer	0	Jumlah berkas CSS eksternal.
rasio_redirect_eksternal	float	0.3311	Rasio redirect eksternal.
rasio_error_eksternal	float	0	Rasio error eksternal.
formulir_login	integer	0	1 jika halaman memuat formulir login.
favicon_eksternal	integer	0	1 jika favicon dimuat dari domain eksternal.
tautan_dalam_tag	float	99.53	Rasio tautan yang berada di dalam tag.
rasio_media_internal	float	100	Rasio media internal.
rasio_media_eksternal	float	0	Rasio media eksternal.
penggunaan_iframe	integer	0	1 jika halaman memakai iframe.
jendela_popup	integer	0	1 jika halaman membuka popup.
anchor_aman	float	65.36	Rasio anchor yang menggunakan tautan aman.
event_onmouseover	integer	0	1 jika halaman memakai event onmouseover.
klik_kanan	integer	0	1 jika klik kanan dinonaktifkan.
judul_kosong	integer	0	1 jika judul halaman kosong.
domain_di_judul	integer	0	1 jika domain muncul di judul halaman.
domain_dengan_copyright	integer	1	1 jika domain muncul di teks copyright.
Sinyal eksternal
Fitur	Tipe	Contoh	Deskripsi
domain_terdaftar_whois	integer	0	1 jika domain terdaftar di WHOIS.
durasi_registrasi_domain	integer	288	Durasi registrasi domain; -1 jika tidak tersedia.
usia_domain	integer	2650	Usia domain; -1 jika tidak tersedia.
lalu_lintas_web	integer	373793	Peringkat lalu lintas web; -1 jika tidak tersedia.
catatan_dns	integer	0	1 jika domain memiliki catatan DNS.
indeks_google	integer	0	1 jika domain terindeks Google.
peringkat_halaman	integer	2	Nilai PageRank domain; -1 jika tidak tersedia.
Submission
Berkas submission.csv berisi id,target, satu baris untuk setiap ID di test.csv. target adalah probabilitas phishing antara 0 dan 1.

id,target
a1b2c3d4,0.87
Catatan
Baca id sebagai teks. Submission harus memuat setiap ID tepat satu kali.