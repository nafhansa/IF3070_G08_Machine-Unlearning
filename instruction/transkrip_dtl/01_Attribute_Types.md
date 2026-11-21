# 01. Attribute Types

Sumber: https://www.youtube.com/watch?v=UkZjVkVqUrQ
Bahasa: Indonesia  |  Durasi video: 00:06:50  |  Metode: subtitle otomatis asli YouTube

> Catatan: Ini adalah transkrip dari subtitle otomatis, bukan hasil audit audio manual. Istilah yang tidak jelas mungkin perlu diperiksa ulang.

## Pengantar

[00:00:04–00:00:16] Halo semuanya. Kita masuk ke dalam materi decision tree learning dan video ini adalah video pertama dalam rangkaian materi decision tree learning. Video ini akan menjelaskan
[00:00:16–00:00:28] mengenai jenis-jenis variabel atau atribut yang mungkin ada dalam dataset karena jenis-jenis variabel atau atribut ini nanti akan menentukan jenis penanganannya pada saat proses
[00:00:28–00:00:31] pembelajaran nanti.

## Atribut numerik

[00:00:31–00:00:40] Jenis yang pertama adalah numerik yaitu atribut yang dapat diukur dan biasanya direpresentasikan dengan nilai integer atau real.
[00:00:40–00:00:52] Untuk atribut numerik bisa dibedakan lagi menjadi yang pertama interval scaled atribut yaitu atribut yang diukur dengan unit yang skala antar nilainya sama.
[00:00:52–00:01:02] Sebagai contoh temperatur 20 derajat Celsius itu artinya 5 derajat lebih tinggi daripada temperatur 15 derajat Celsius.
[00:01:02–00:01:08] Contoh lain adalah tanggal tahun 2020 berjarak 8 tahun dari tahun 2012.
[00:01:08–00:01:21] Tapi kita tidak bisa menggunakan rasio pada atribut ini. Maksudnya begini, misal suhu 20 derajat Celsius itu kita tidak bisa menyatakan bahwa dia dua kali lebih hangat daripada suhu 10 derajat Celsius.
[00:01:21–00:01:34] Nah, perlu diingat juga sebuah atribut temperatur dengan nilai 0 derajat Celsius bukan berarti dia kosong tapi dia adalah suatu angka yang merepresentasikan nilai derajat tertentu.
[00:01:34–00:01:44] Nah, berbeda dengan interval scaled atribut ada juga yang namanya rasio scaled atribut. Di sini nilai numerik 0 memiliki makna kosong.
[00:01:44–00:01:56] Misalkan kita memiliki atribut berapa tahun pengalaman kerja seseorang maka jika atribut tersebut bernilai 0 artinya orang tersebut belum memiliki pengalaman kerja.
[00:01:56–00:02:02] Hal yang sama untuk atribut bobot. Bobot 0 artinya tersebut tidak memiliki bobot.
[00:02:02–00:02:13] Nah, untuk rasio scale atribut, kita bisa menggunakan rasio atau perbandingan. Misal bobot 20 artinya dua kali lebih berat daripada bobot 10.
[00:02:13–00:02:24] Namun pada prakteknya nanti kita jarang melakukan pembedaan ini. Selama atribut berjenis numerik kita bisa menghitung rata-rata, nilai tengah, atau modusnya.
[00:02:24–00:02:30] Jenis berikutnya adalah nominal atau kategorikal yang menyatakan simbol atau nama sesuatu.

## Atribut nominal

[00:02:30–00:02:39] Setiap nilai merepresentasikan suatu kategori, kode, atau status dan antar nilainya tidak memiliki urutan.
[00:02:39–00:02:51] Walaupun demikian atribut ini mungkin juga direpresentasikan dengan angka, hanya memang tidak digunakan sebagai nilai yang kuantitatif.
[00:02:51–00:03:04] Sebagai contoh untuk kode pos, NIM, atau jenis pekerjaan, atribut tersebut bisa saja direpresentasikan dengan angka, namun tidak memiliki makna terurut dan tidak bisa kita cari nilai rata-rata
[00:03:04–00:03:06] atau mediannya.

## Atribut biner

[00:03:06–00:03:19] Sedangkan untuk modus masih bisa digunakan pada jenis atribut ini. Jenis ketiga adalah binary yang menyatakan bahwa suatu atribut hanya memiliki dua kategori atau status.
[00:03:19–00:03:28] Jika nilainya kebetulan adalah true atau false bisa kita nyatakan sebagai boolean. Untuk jenis binary ini nilainya mungkin bersifat simetrik.
[00:03:28–00:03:40] Artinya antar nilai tidak ada yang lebih penting daripada yang lain. Contohnya adalah jenis kelamin. Atau asimetrik yaitu saat akan melakukan pembelajaran sebuah nilai dianggap lebih penting
[00:03:40–00:03:51] daripada yang lain. Misalnya kelas pasien terdeteksi positif HIV direpresentasikan sebagai satu yang dianggap lebih penting.
[00:03:51–00:04:02] Pada bahasa pemrograman tertentu kakas atau pustaka pembelajarannya terkadang meminta kita untuk memasukkan nilai numerik untuk bisa memproses dataset
[00:04:02–00:04:14] atau training examples yang kita miliki. Nah, jenis binary ini bisa kita gunakan untuk merepresentasikan atribut nominal menjadi nilai rangkaian 0 dan 1.
[00:04:14–00:04:25] Sebagai contoh kita memiliki atribut red, green, dan blue. Bisa kita gunakan one hot encoding di mana red direpresentasikan dengan 1 0 0
[00:04:25–00:04:34] green menjadi 0 1 0 dan blue menjadi 0 0 1.
[00:04:34–00:04:42] Jenis berikutnya adalah ordinal yang mirip seperti nominal, namun antar nilainya memiliki makna urutan.

## Atribut ordinal

[00:04:42–00:04:53] Walaupun demikian kita tidak bisa menyatakan seberapa penting atau seberapa jauh jarak antar nilai yang berurutan pada jenis ini.
[00:04:53–00:05:02] Biasanya jenis ini digunakan untuk pemberian nilai secara subjektif, hasil survei misalnya atau ukuran minuman yang dijual pada restoran.
[00:05:02–00:05:08] Atribut ordinal juga mungkin diperoleh dari hasil diskritisasi atribut numerik.
[00:05:08–00:05:22] Contoh atribut ordinal adalah indeks nilai. Kita tidak bisa menentukan seberapa baik nilai A dibandingkan nilai AB. Yang kita ketahui bahwa A itu lebih baik daripada indeks AB.
[00:05:22–00:05:34] Hal yang sama untuk ukuran minuman. Kita tidak bisa memastikan bahwa ukuran medium itu dua kali ukuran small karena yang kita tahu bahwa ukuran medium itu lebih banyak daripada ukuran
[00:05:34–00:05:45] small. Terkadang kita juga mendengar jenis atribut diskrit atau continuous dan tiap jenis mungkin akan diproses dengan cara yang berbeda.

## Nilai diskrit dan kontinu

[00:05:45–00:05:59] Intinya untuk atribut yang memiliki himpunan nilai terbatas, misalnya ukuran minuman small, medium, large atau kemungkinan nilainya bisa tak terbatas tapi sebetulnya masih bisa
[00:05:59–00:06:08] dibuat korespondensi satu ke satu dengan bilangan natural. Maka dia termasuk sebagai jenis yang diskrit.
[00:06:08–00:06:20] Nah, jika tidak memenuhi dua hal tersebut, maka termasuk ke dalam jenis yang continuous. Untuk pembahasan awal mengenai algoritma DTR, kita akan fokus dulu ke jenis
[00:06:20–00:06:29] atribut diskrit. Demikian video mengenai jenis-jenis variabel atau atribut.
[00:06:29–00:06:40] Berikutnya kita akan belajar mengenai apa itu decision tree learning, mengapa kita menggunakan decision tree learning, dan kapan sebaiknya kita menggunakan decision tree learning
[00:06:40–00:06:47] sebagai algoritma pembelajaran untuk agent. Selamat belajar.
