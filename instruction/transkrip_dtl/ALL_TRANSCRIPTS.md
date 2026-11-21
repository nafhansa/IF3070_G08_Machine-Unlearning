# IF3270 — Decision Tree Learning: seluruh transkrip

Bahasa asli: Indonesia. Sumber: subtitle otomatis asli YouTube. Timestamp mengikuti cue sumber.
Teks yang tidak jelas pada subtitle otomatis dibiarkan dekat dengan bentuk sumber; lihat REPORT.md untuk batasan.

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

---

# 02. What, Why, and When

Sumber: https://www.youtube.com/watch?v=zBUe2ma_14A
Bahasa: Indonesia  |  Durasi video: 00:04:47  |  Metode: subtitle otomatis asli YouTube

> Catatan: Ini adalah transkrip dari subtitle otomatis, bukan hasil audit audio manual. Istilah yang tidak jelas mungkin perlu diperiksa ulang.

## Pengantar dan definisi

[00:00:00–00:00:12] halo halo semuanya masih dalam Modul decision Tree Learning Kita akan melanjutkan pembahasan dengan Apa itu
[00:00:12–00:00:25] yang dimaksud dengan decision Tree learning Bagaimana representasinya serta Kenapa kita melakukan pembelajaran dengan decision tree learning dan kapan sebaiknya kita melakukan pembelajaran
[00:00:25–00:00:37] dengan decision Tree learning of decision tree learning atau DPR awalnya diusulkan sebagai metode untuk melakukan aproksimasi fungsi target dengan nilai
[00:00:37–00:00:45] discrete walaupun pada perkembangannya nanti bisa juga digunakan untuk nilai yang tidak Describe fungsi targetnya direpresentasikan

## Representasi pohon keputusan

[00:00:45–00:00:56] dalam bentuk pohon keputusan dan bisa juga direpresentasikan sebagai sekumpulan aturan FDN agar lebih mudah dibaca dan dipahami
[00:00:58–00:01:10] setiap simpul internal pada pohon merepresentasikan pengujian nilai pada suatu atribut lebih mudahnya nama atribut biasanya diletakkan pada simpul
[00:01:10–00:01:24] internal tersebut nah cabang yang keluar dari suatu simpul internal adalah kemungkinan nilai dari atribut tersebut simpul daun atau simpel Terminal
[00:01:24–00:01:37] merepresentasikan hasil klasifikasi pada cabang tersebut DTA bisa merepresentasikan konsep sebagai disjungsi dari beberapa
[00:01:37–00:01:51] konjungsi antar batasan atau country Nilai suatu atribut jadi satu jalur atau paste dari akar hingga ke simpul daun dihubungkan dengan konjungsi dan jalur
[00:01:51–00:01:55] dengan hasil simpul daun yang sama dihubungkan dengan disjungsi Sebagai

## Representasi aturan

[00:01:55–00:02:05] contoh untuk pohon keputusan apakah akan bermain tenis seperti yang terlihat pada layar untuk konsep Yes maka bisa berupa
[00:02:05–00:02:15] deskripsi sebagai berikut jika Outlook sama dengan Sunny dan heme Dede sama dengan normal atau jika Outlook =
[00:02:15–00:02:28] overcast atau jika output = drain dan Win = w maka akan bermain tense dari
[00:02:28–00:02:39] penjelasan sebelumnya dtl adalah untuk aproksimasi fungsi target yang bernilai Describe dan representasinya cukup mudah dipahami dalam bentuk pohon
[00:02:39–00:02:52] keputusan atau sekumpulan aturan f&d TL juga cukup tangguh ketika ada data yang kotor namun pembahasan Penanganannya akan diberikan di materi selanjutnya
[00:02:52–00:03:01] setelah itu dibandingkan dengan konsep learning menggunakan algoritma Candi determination dtl mampu belajar untuk

## Alasan menggunakan decision tree learning

[00:03:01–00:03:14] menghasilkan hipotesis dengan representasi disjungsi Nah hal-hal inilah yang membuat detail menjadi algoritma inferensi induksi yang cukup
[00:03:14–00:03:27] populer dan sudah banyak digunakan dengan sukses pada berbagai ranah persoalan antara lain kasus sejarah nosis medis hingga penentuan resiko kredit dari pelanggan yang mengajukan
[00:03:27–00:03:40] pinjaman berdasarkan dari dtl yang sudah disebutkan sebelumnya maka persoalan yang bisa diselesaikan dengan pendekatan CTL adalah persoalan yang training examples
[00:03:40–00:03:53] atau datasheetnya direpresentasikan dengan pasangan atribut nilai Describe sebetulnya untuk data kontinyu juga bisa menggunakan dtl dengan pendekatan deskriptif Sasi tapi nanti akan dibahas
[00:03:53–00:03:56] pada materi selanjutnya Selain itu

## Kapan decision tree learning digunakan

[00:03:56–00:04:08] persoalan yang fungsi targetnya adalah nilai Describe serta diperlukan representasi disjungsi untuk targetnya cocok menggunakan pendekatan CTL Na persoalan yang mengandung
[00:04:08–00:04:19] kesalahan atau data kotor atau mungkin ada nilai yang hilang pada suatu atribut bisa menggunakan pendekatan CTL isu-isu terkait detail ini nanti akan diberikan
[00:04:19–00:04:31] pada materi yang terpisah untuk Nah setelah kita mengetahui apakah itu disusun turning Bagaimana representasinya Kenapa dan kapan sebaiknya kita menggunakan deskriptif
[00:04:31–00:04:45] learning berikutnya kita akan belajar mengenai bagaimana sih proses yang ada di dalam decision to download link kita akan mulai dengan langkah-langkah dasarnya terlebih dahulu Selamat belajar [Musik]
[00:04:45–00:04:48] ya

---

# 03. Basic DTL Algorithm (ID3)

Sumber: https://www.youtube.com/watch?v=uSTgx9NiEHQ
Bahasa: Indonesia  |  Durasi video: 00:08:49  |  Metode: subtitle otomatis asli YouTube

> Catatan: Ini adalah transkrip dari subtitle otomatis, bukan hasil audit audio manual. Istilah yang tidak jelas mungkin perlu diperiksa ulang.

## Pengantar algoritma ID3

[00:00:00–00:00:13] halo halo semuanya video ini akan membahas cara kerja Dasar atau tahapan dalam pembelajaran dengan algoritma decision Tree learning yaitu algoritma
[00:00:13–00:00:26] id3 hidrat if the Academy SS3 yang diusulkan oleh quinton pada tahun 1986 Albert maytri bekerja secara top-down
[00:00:26–00:00:40] dengan tiap titrasinya menggunakan prinsip pencarian grade yaitu memilih atribut terbaik untuk diletakkan pada simpul Jadi pertama dari training examples
[00:00:40–00:00:45] kita pilih atribut terbaik caranya nanti dengan menghitung information gain dari

## Tahapan pembentukan pohon

[00:00:45–00:00:58] setiap atribut nah penjelasan mengenai information gain diberikan pada vidio berikutnya segera mendapatkan atribut terbaik kita Letakkan atribut tersebut pada simpul pohon yang saat itu sedang
[00:00:58–00:01:11] dibentuk untuk setiap kemungkinan nilai pada atribut kita bentuk cabang ke bawah lalu kelompokkan training examples
[00:01:11–00:01:24] sesuai dengan nilai pada pencabangan lalu kita periksa Apakah hasil pengelompokan tadi membuat Rene examples pada suatu cabang semuanya sudah
[00:01:24–00:01:35] memiliki kelas yang sama jika sudah maka kita bentuk simpul daun atau simpul Terminal dengan nilai kelasnya tapi kalau masih ada training examples dengan
[00:01:36–00:01:49] kelas yang berbeda maka diharuskan melakukan khusus untuk data pencabangan tersebut untuk memilih atribut terbaik berikutnya adalah
[00:01:49–00:02:02] Mari kita lihat contoh penerapan algoritma id3 pada training examples berikut ini terdapat 14 data pada

## Contoh data bermain tenis

[00:02:02–00:02:16] training examples hasil observasi 14hari mengenai cuaca dan keputusan untuk bermain tenis atau tidak terdapat empat atribut pada data tersebut yaitu abduk
[00:02:16–00:02:26] temperature humidity dan mint langkah pertama kita mencari atribut terbaik dan misalnya kita dapatkan Outlook adalah
[00:02:26–00:02:40] atribut terbaik diantara yang lain maka atribut tersebut kita Letakkan pada simpul akar karena atribut alt memiliki tiga kemungkinan nilai yaitu Shandi Cover
[00:02:40–00:02:53] Case danrin maka kita bentuk tiga pencabangan untuk simpul Terdapat lima data yang memiliki nilai output lux sama dengan Sunny dan
[00:02:53–00:03:04] dari lima data tersebut terdapat dua data berkelas Yes dan 3data berkelas now artinya belum semua data terklasifikasi
[00:03:04–00:03:16] kan pada kelas yang sama sehingga belum bisa dibentuk simpul daun atau terminal untuk percabangan tersebut Nah untuk Outlook = overcast terdapat empat data
[00:03:16–00:03:28] dan semuanya berkelas Yes jadi kita bisa bentuk simpul daun dengan nilai nya adalah Yes untuk Outlook sama dengan rem
[00:03:28–00:03:41] Terdapat lima data dengan 3data berkelas Yes dan 2D data berkelas no no jadi kita juga belum bisa membentuk simpul daun di bawah pencabangan Outlook
[00:03:41–00:03:52] sama dengan range Indonesia berikutnya Ayo kita kembali ke langkah pertama
[00:03:52–00:03:56] untuk mencari atribut Apa yang

## Pemilihan atribut dan pencabangan

[00:03:56–00:04:07] sebaiknya diletakkan pada simpul di bawah pencabangan Outlook sama dengan Sunny disini kita hanya melihat atribut
[00:04:07–00:04:17] temperature humidity dan when i dan hanya ada lima data yang nilai atribut outputnya sama dengan Sunny
[00:04:17–00:04:29] yaitu D1 D2 d8d 9 dan dari ketiga atribut tersebut yaitu
[00:04:29–00:04:41] temperature humidity dan with kita cari atribut yang terbaik berikutnya misalkan kita pilih ternyata humidity adalah
[00:04:41–00:04:55] atribut terbaik maka humidity kita Letakkan pada simpul pohon dengan pencabangannya adalah semua kemungkinan nilai untuk atribut humidity yaitu
[00:04:55–00:05:07] dan normal untuk data dengan Outlook sama dengan Sunny dan hem editingnya terdapat tiga data dan semuanya berkelas
[00:05:07–00:05:18] not yaitu D1 D2 dan deh 8 jadi kita bisa membuat simpul daun dengan nilainya adalah no Sedangkan
[00:05:18–00:05:28] untuk data dengan nilai Outlook sama dengan Sunny dan hiu meditasinya sama dengan normal terdapat dua data dan
[00:05:28–00:05:41] semuanya berkelas Yes yaitu d9 dan di 11 jadi bisa kita bentuk simpul daun dengan nilainya Yes karena semua data pada
[00:05:41–00:05:52] pencabangan ini sudah terkelompokkan pada kelas klasifikasi yang sama maka pembentukan pohon di cabang ini sudah selesai Na berikutnya Kita tentukan
[00:05:52–00:06:04] percabangan untuk upload sama dengan Rin dari lima data dengan nilai output = Rey ternyata atribut terbaik berikutnya
[00:06:04–00:06:17] misalnya maka kita Letakkan Win pada simpul pohon dan pencabangannya adalah nilai Storm dan week
[00:06:17–00:06:30] untuk data dengan out look = Rey dan Windu = strong terdapat dua data dan semuanya berkelas now
[00:06:30–00:06:38] jadi kita bisa membuat simpul daun dengan nilainya adalah loh Sedangkan untuk data dengan Outlook
[00:06:38–00:06:49] = Rain danwin = W terdapat tiga data dan semuanya berkelas yes jadi kita bisa membentuk simpul daun
[00:06:49–00:06:53] lagi dengan nilainya adalah Yes Nah

## Pohon keputusan yang terbentuk

[00:06:53–00:07:04] karena semua data pada pencabangan ini sudah terkelompokkan pada kelas klasifikasi yang sama maka pembentukan pohon di cabang sudah selesai Setelah
[00:07:04–00:07:15] semua pencabangan sampai pada simpul daun maka proses pembelajaran Idris selesai dan pohon yang terbentuk untuk training examples spray times adalah
[00:07:15–00:07:28] seperti yang tampak pada layar nah lalu apa sih yang disebut sebagai atribut terbaik yang secara gede akan dipilih untuk diletakan pada simpul pohon
[00:07:28–00:07:42] atribut yang baik idealnya bisa mengelompokkan training examples menjadi kelompok-kelompok dengan nilai kelas yang sama Jadi intinya dengan mengetahui nilai dari atribut tersebut saya sudah
[00:07:42–00:07:54] bisa mengambil keputusan atau menentukan kelas dari data yang masuk ngaco nya untuk gambar di bagian bawah pada layar atribut patrons merupakan atribut
[00:07:54–00:08:06] yang lebih baik daripada atribut tipe karena dengan kemungkinan nilai tertentu dari atribut Veteran yaitu nilai nan atau Sam kita sudah bisa menentukan
[00:08:06–00:08:19] kelas datanya Sedangkan untuk atribut tipe semua kemungkinan nilai untuk atribut tersebut belum ada yang bisa menghasilkan pengumpulan data menjadi
[00:08:19–00:08:32] satu kelas yang sama Dalam nah bagaimana caranya untuk menentukan atribut terbaik ini kita akan menggunakan information gain dan ini
[00:08:32–00:08:43] akan kita pelajari pada video berikutnya cek demikian materi mengenai algoritma umum audit Rin selanjutnya kita akan belajar mengenai information gain
[00:08:43–00:08:50] Selamat belajar ya

---

# 04. Information Gain

Sumber: https://www.youtube.com/watch?v=aVE7xQJNuCA
Bahasa: Indonesia  |  Durasi video: 00:20:17  |  Metode: subtitle otomatis asli YouTube

> Catatan: Ini adalah transkrip dari subtitle otomatis, bukan hasil audit audio manual. Istilah yang tidak jelas mungkin perlu diperiksa ulang.

## Pengantar

[00:00:00–00:00:11] halo halo semuanya kita akan melanjutkan materi decision tree learning dan video ini membahas mengenai information gain yaitu
[00:00:11–00:00:22] cara untuk mendapatkan atribut terbaik dalam dtla-4 sebelum masuk ke information gain kita bahas dulu entropi atau information
[00:00:22–00:00:35] content entropi adalah suatu pengukuran dalam informations Teori yang menyatakan nilai ketidakmurnian dari sembarang Kumpulan data dalam hal ini nanti yang

## Entropi

[00:00:35–00:00:47] kita bicarakan adalah training examples misal s adalah himpunan training examples entropi dari es menyatakan Berapa banyak bit informasi yang kita
[00:00:47–00:00:59] perlukan atau yang harus dikirimkan agar ketika kita mengambil sebuah data dari es cara acak kita bisa tahu kelas dari data tersebut
[00:00:59–00:01:12] formulanya adalah total dari negatif proporsi atau bagian es dengan kelas tertentu dikalikan log-2 dari proporsi tersebut
[00:01:12–00:01:24] proporsi dari tiap kelas nilainya minimal 0 dan maksimal oke Sekarang mari kita lihat seandainya training examples kita memiliki dua
[00:01:24–00:01:36] kelas misalnya kelas positif dan kelas negatif entropi dari es adalah penjumlahan dari negatif atau minus
[00:01:36–00:01:45] proporsi kelas positif kali log-2 proporsi kelas positif dengan negatif atau minus dari proporsi kelas negatif
[00:01:45–00:01:58] kali love2 proporsi kelas negatif nah grafik pada layar menunjukkan kemungkinan nilai proporsi kelas positif dengan nilai entropinya jika proporsi
[00:01:58–00:02:11] kelas positif bernilai nol artinya semua training examples pada s-class negatif dan proporsi kelas negatif nilainya
[00:02:11–00:02:24] jika dimasukkan ke dalam formula entropi maka entropi dari es akan bernilai nol yang artinya nilai impurity dari dataset es adalah 0bid jadi ketika
[00:02:24–00:02:36] saya mengambil sembarang data atau Instance dari es saya tahu kelasnya dengan aktif sehingga tidak perlu dikirimkan informasi apapun untuk bisa menentukan kelas dari intense yang saya
[00:02:36–00:02:48] ambil tadi Nah hal ini juga berlaku ketika nilai proporsi dari kelas positifnya satu yang artinya semua trendex simbol pada es berkelas positif
[00:02:48–00:02:50] yang berbeda ketika proporsi kelas

## Contoh perhitungan entropi

[00:02:50–00:03:03] positif bernilai setengah yang artinya separuh Trada example Saya berkelas positif dan separuhnya lagi berkas negatif jadi ketika saya mengambil sebuah instan secara sembarang dari
[00:03:03–00:03:13] trainee example es saya perlu informasi sejumlah 1-bit untuk mengetahui kelas dari instansi yang saya ambil tadi
[00:03:13–00:03:25] nah kaitannya dengan dtl kita ingin memilah training examples sedemikian supaya nilai entropinya sekecil mungkin
[00:03:25–00:03:38] jadi tanpa perlu mengirimkan banyak informasi kita bisa mengetahui kelas dari suatu Instance Mari kita lihat contoh berikut ya pada layar kiri bawah
[00:03:38–00:03:49] terdapat trading examples yang memiliki lima data kelas merah dan lima data kelas biru jadi proporsi kelas merah adalah setengah dan proporsi dari kelas
[00:03:50–00:04:00] biru juga setengah entropi dari data tersebut adalah Ndah misal Saya memilih nih atribut
[00:04:00–00:04:10] pertama sehingga pengelompokkan datanya menjadi data pada gambar yang paling kiri dengan pemilihan atribut tersebut
[00:04:10–00:04:22] ternyata nilai entropi tidak berkurang Nah sekarang kita lihat kalau misalnya saya membeli atribut yang kedua misalnya pada gambar yang
[00:04:22–00:04:34] entropi menjadi lebih kecil sedangkan jika saya memilih atribut yang ketiga pada gambar paling kanan entropi berkurang menjadi Nah dari ketiga atribut tersebut
[00:04:34–00:04:48] maka atribut ketiga adalah atribut yang paling baik dibandingkan dengan atribut pertama dan atribut Indonesia Nah untuk training examples vs
[00:04:48–00:05:00] dengan banyaknya kelas lebih dari dua maka nilai entropi paling besar bisa mencapai log-2 dari banyaknya kelas tersebut nah grafik pada layar

## Rumus information gain

[00:05:00–00:05:14] menunjukkan contoh jika banyaknya kelas itu adalah nol hingga 16 maka kemungkinan nilai entropinya pun juga beragam Indonesia Lalu bagaimana kaitannya
[00:05:14–00:05:27] dengan information gain Nani Legend inilah yang kita gunakan untuk memilih atribut terbaik dalam algoritma id3 jadi gen dari suatu atribut pada training
[00:05:27–00:05:39] example es adalah ekspektasi pengurangan nilai entropi dataset es jika kita kelompokkan datanya berdasarkan nilai
[00:05:39–00:05:52] pada atribut a&k renang kita ingin hell entropinya Makin kecil maka kita cari atribut yang gamenya atau ekspektasi pengurangan nya paling besar
[00:05:52–00:06:03] sehingga dia akan bisa mengurangi dengan cukup banyak nilai entropi semula Oh no formula dari game suatu atribut A4
[00:06:03–00:06:15] rending examples adalah entropi dari es dikurangi dengan total penjumlahan proporsi tiap kemungkinan nilai atribut
[00:06:15–00:06:27] a.di kalikan dengan entropi dari training examples yang atribut hanya bernilai tertentu namari kita terapkan
[00:06:27–00:06:39] cara pencarian information gini tersebut untuk membentuk pohon dari data training example Cuaca 14hari dan penentuan
[00:06:39–00:06:53] Apakah bermain tenis atau tidak jadi dari Kumpulan data yang kita miliki sama seperti pada video Sebelumnya kita akan mencari atribut terbaik atribut terbaik adalah atribut yang
[00:06:53–00:06:56] nilai game-nya paling besar sehingga

## Perhitungan pada data contoh

[00:06:56–00:07:08] kita mencari nilai gen yang paling maksimum di antara oklo temperature humidity dan band pertama kita cari dulu nilai entropi dari es atau keseluruhan
[00:07:08–00:07:20] data pada training examples nya jadi entropi pada es adalah proporsi dari kelas Yes di sini ada 9 data yang
[00:07:20–00:07:32] memiliki classiest dibagi dengan 14 itu adalah keseluruhan data kalikan dengan log-2 dari 90142 dan kemudian proporsi berikutnya itu
[00:07:32–00:07:45] adalah lima yaitu kelas no Terdapat lima data yang memiliki kelas no dibagi dengan 14 itu keseluruhan data yang ada kaitan dengan log 25 atau 14 maka
[00:07:45–00:07:57] entropi esnya adalah 0,9 Nah dari sini kita mulai menghitung misalnya yang pertama kita hitung gendari atribut of Light
[00:07:57–00:08:09] Ayo kita ingat kembali formulanya adalah entropi dari es dikurangi dengan penjumlahan proporsi dari semua nilai yang
[00:08:09–00:08:19] mungkin untuk atribut Outlook dikalikan dengan entropinya dia Mari kita lihat satu persatu kejadian trophy es itu
[00:08:19–00:08:32] adalah 0,9 40 lalu kita tahu bahwa untuk atribut outgroup nilainya adalah Sunny Cover Case dan Reigns
[00:08:32–00:08:43] nomor kita lihat berapa proporsi untuk atribut out look yang nilainya Sunny
[00:08:43–00:08:54] oke di sini ada 12 2345 Jadi ada lima data dari 14 data
[00:08:54–00:09:05] yang nilai Outlook nya sama dengan Sunny jadi ke nanti akan dikalikan dengan entropi untuk Sunny berikutnya adalah
[00:09:05–00:09:17] proporsi untuk Outlook = overcast kita lihat di sini over casnya ada 1234 berarti proporsi adalah empat dari 14
[00:09:17–00:09:28] data itu nilai atribut out truknya = overcast nanti akan kita kalikan dengan entropi overcast berikutnya adalah untuk
[00:09:28–00:09:41] yang lain terdapat 123455 data dari 14 data yang atribut outputnya bernilai untuk nanti kemudian kita kalikan dengan
[00:09:41–00:09:53] intropia print Nah kita sudah tahu proporsinya masing-masing nah untuk menghitung entropi dari Sunny kita ingat lagi rumus
[00:09:53–00:10:07] entropinya mirip seperti ini tapi kita ingat ketika menghitung entropi Sunny yang kita perhatikan hanya lima data yang out look nya sama dengan Sunny saja
[00:10:07–00:10:19] Oke Nah dari lima data tersebut ternyata ada dua yang kelasnya yes ya yaitu di sini
[00:10:19–00:10:31] a bad disini sehingga entropinya adalah minus 2 dari 5 log 2 2/5 dikurangi dengan proporsi untuk kelas nonya
[00:10:31–00:10:45] terdapat tiga data yang kelasnya no dari lima data yang outputnya sama dengan Sunny kalikan dengan log-2 dari 3/5 nah hal yang sama untuk entropi overcast
[00:10:45–00:10:57] ketika menghitung entropi overcast maka yang kita lihat adalah hanya data yang outputnya = Cover Case yo yah kita punya empat data yaitu D3
[00:10:57–00:11:10] dituju d12 dan d13 nah Dari keempat data ini semuanya berkelas Yes jadi ada 4 data yang berkelas Yes dari empat data
[00:11:10–00:11:22] yang outputnya = overcast kalikan dengan log-2 dari proporsi classiest di tempat-tempat proporsi untuk kelas nonya untuk
[00:11:22–00:11:36] upload = overcast itu adalah 0/4 kalian log-2 dari 046 but Bagaimana nanti kalau menghitung log 2 dari 04 Nah kita abaikan yang bagian sini karena an004au
[00:11:36–00:11:48] itu pasti nol dikalikan berapa pun nilainya pasti noh begitu ya selanjutnya untuk entropi Rein caranya sama kita cari proporsi dari data yang outputnya
[00:11:48–00:12:00] sama dengan rem dengan classiest ya datanya hanya ada lima Yang output = Rein dan tiga diantaranya berkelas Yes jadi 3/5 proporsinya kalikan log-2 dari
[00:12:00–00:12:14] 35 untuk kelas yang no terdapat dua data dari lima data tersebut sehingga proporsinya 25 kalikan log-2 dari dua per lima sub
[00:12:14–00:12:27] Nah dari sini kita lakukan perhitungan dan menghasilkan game untuk atribut Outlook adalah 0,2
[00:12:27–00:12:39] dengan cara yang sama kita bisa menghitung Gen untuk atribut yang lain mari kita lihat contoh satu lagi untuk penghitungan gendari humidity enter punya masih sama seperti sebelumnya ya
[00:12:39–00:12:51] dari 14 data tersebut untuk kemudian cara perhitungan gamenya juga sama Nah di sini kita punya tujuh data yang atribut humidity nya bernilai
[00:12:51–00:13:04] sehingga proporsi 7/14 sekali entropi dan 7 data yang nilai humidity nya bernilai normal jadi 7-14 valika dengan entropi normal untuk penghitungan
[00:13:04–00:13:16] entropi itu sama dari tujuh data yang yummy dirinya sama dengan itu terdapat tiga data berkelas Yes dan empat data bernilai nol jadi kita punya
[00:13:16–00:13:30] proporsi untuk kelas ya adalah 3/7 dan proporsi untuk kelas semuanya 4 per tujuh hal yang sama untuk humidity yang nilainya normal maka cara PT cerpen normalnya adalah proporsi kelas
[00:13:30–00:13:40] Yes nya yaitu terdapat enam data dari tujuh data dengan Hymne bersama dengan normal berkelas Yes dan terdapat satu data yang berkelas

## Memilih atribut terbaik

[00:13:40–00:13:54] Nah dari sana kita dapatkan nilai hiu meditasinya gendari Hamidi tinggi adalah 0,15 10 Nah setelah kita melakukan penghitungan Gen untuk semua
[00:13:54–00:14:06] atribut maka kita dapatkan nilai sebagai berikut dan disana terlihat bahwa atlub memiliki nilai gen yang paling besar dibandingkan dengan atribut yang lain Oleh karena itu out look terpilih
[00:14:06–00:14:19] sebagai atribut terbaik ya karena ekspektasi pengurangan entropinya paling besar kemudian atribut-atribut kita Letakkan pada simpul pohon dan pencabangannya adalah nilai-nilai dari
[00:14:19–00:14:32] atribut Out Loud seperti kita tahu pada video sebelumnya muntuk nilai Outlook = over charge kita sudah bisa mengelompokkan semua datanya pada kelas yang sama yaitu Yes Nah sekarang persoalannya adalah untuk output sama
[00:14:33–00:14:46] dengan Sunny karena nilai datanya masih ada yang berkelas Yes masih ada yang berkelas no Oleh karena itu kita perlu menentukan atribut terbaik Apa yang sebaiknya
[00:14:46–00:14:57] diletakkan pada simpul pencabangan Outlook sama dengan Sunny the lounge caranya sebetulnya sama seperti langkah sebelumnya hanya perlu
[00:14:57–00:15:10] diperhatikan yang kita pertimbangkan pada saat pemilihan atribut ini hanya data yang nilai out klubnya sama dengan Sunny saja sehingga hanya ada lima data
[00:15:10–00:15:23] yang kita perhatikan Oleh karena itu nilai entropi set esnya pun juga harusnya berubah hanya melibatkan lima data ini saja Oke jadi entropi esnya adalah maka kita lihat kelasnya tetap
[00:15:23–00:15:35] ada dua yaitu Yes sudah now kita lihat dari data D1 D2 d8d 9 dari 11 terdapat dua data bernilai Yes sehingga proporsinya adalah dua dari lima
[00:15:35–00:15:47] sedangkan data yang berkelas noda 3 sehingga proporsi adalah 3/5 nya formula interfacenya sama saja kita dapatkan lain tropinya 0,97 satu untuk lima data
[00:15:47–00:15:59] yang sedang kita pertimbangkan ini nah berikutnya misalnya kita hitung gendari humidity kyahi jadi kita formatnya sama yaitu
[00:15:59–00:16:13] entropi S dikurangi dengan total penjumlahan proporsi suatu nilai untuk atribut biomedical ikan dengan entropi nilai tersebut Oke jangan lupa interfacenya adalah entropi dari lima
[00:16:13–00:16:24] data ini saja yaitu 0,97 satu dikurangi dengan nah proporsi untuk data yang nilai hidupnya itu ada
[00:16:24–00:16:37] tiga data jadi proporsinya 3/5 Sedangkan untuk data yang nilai hidupnya sama dengan normal itu ada dua data sehingga proporsi adalah 2/5 nanti dikalikan
[00:16:37–00:16:48] dengan entropi masing-masing nilai untuk entropi itu ternyata ketiga datanya semuanya berkelas no
[00:16:48–00:16:52] Oke sehingga proporsi kelasnya 03

## Melanjutkan pencabangan

[00:16:52–00:17:06] proporsi untuk kelas Noya 3/3 Sedangkan untuk entropi normal terdapat dua data ternyata dua-duanya berkelas Yes sehingga proporsi untuk prosesnya dua
[00:17:06–00:17:17] dari dua data dengan nilai limitnya normal dan proporsi untuk kelas menunya adalah nol dari dua data dari sana kita
[00:17:17–00:17:31] dapatkan nilainya adalah 0,97 Nah kita hitung juga untuk game dari temperatur dan Band Ingat disini kita
[00:17:31–00:17:43] tidak lagi menghitung game dari Outlook karena al-qur'an sudah terpilih Dia sudah menjadi simpul akar pada persoalan ini Nah dengan cara yang sama kita
[00:17:43–00:17:55] hitung Gen untuk temperatur dan b dengan entropinya yaitu 0,97 satu yang lima data ini maka kita dapatkan nilai G dari tiga atribut adalah sebagai berikut dan
[00:17:55–00:18:08] nilai game tertinggi adalah atribut humidity yaitu 0,97 satu Oleh karena itu hiu mediti kita pilih sebagai atribut dia akan diletakkan pada simpul pada
[00:18:08–00:18:20] pencabangan Outlook sama dengan Sunny nah seperti kita ketahui dari video sebelumnya dengan meletakkan humidity
[00:18:20–00:18:31] sebagai simpul pada pencabangan otot sama dengan Sunny kita sudah bisa mengelompokkan training examples ya menjadi class Yes Danau sehingga kita
[00:18:31–00:18:44] tidak perlu mencari atribut lagi suntuk di bawah imrithi nah berikutnya kita lakukan hal yang sama untuk Outlook sama dengan Rin jangan lupa data yang
[00:18:45–00:18:55] digunakan untuk menghitung entropi esnya itu hanya data yang nilai outputnya sama dengan Rin saja untuk kemudian dihitung
[00:18:55–00:19:07] lagi gendari atribut temperatur hiu mediti danwin yang nilai outputnya = Rein dari sana kita pilih atribut
[00:19:07–00:19:19] terbaik atau atribut yang memiliki nilai Jin tertinggi hingga semua data Nanti pada saat sudah kita tentukan atributnya kita bisa
[00:19:19–00:19:33] mengelompokkannya menjadi Kumpulan data dengan kelas yang sama Dalam Indonesia Nah setelah kita belajar mengenai information gain itu sebetulnya
[00:19:33–00:19:46] kita sudah tahu bagaimana cara melakukan pembelajaran dengan decision Tree tepatnya dengan algoritma id3 itu ya Nah silahkan Anda coba latihan ini
[00:19:46–00:19:59] bisa nda boleh memanfaatkan Excel gitu ya untuk kemudian dibahas di kelas Apakah hasilnya sebaiknya dicatat ya Berapakah nilai Gen untuk setiap atributnya sehingga dipilih atribut yang
[00:19:59–00:20:12] mana untuk kemudian bis bebas bersama di kelas Apakah setiap mahasiswa menghasilkan pohon keputusan yang sama Noah demikian video mengenai information
[00:20:12–00:20:19] game Selamat belajar ya

---

# 05. Overfitting

Sumber: https://www.youtube.com/watch?v=hkxC117tEu4
Bahasa: Indonesia  |  Durasi video: 00:21:10  |  Metode: subtitle otomatis asli YouTube

> Catatan: Ini adalah transkrip dari subtitle otomatis, bukan hasil audit audio manual. Istilah yang tidak jelas mungkin perlu diperiksa ulang.

## Pengantar isu overfitting

[00:00:00–00:00:13] halo halo semuanya berjumpa lagi bersama saya Ulfa untuk kuliah pembelajaran mesin video ini adalah video pertama
[00:00:13–00:00:25] yang menjadi rangkaian video kuliah dengan materi isu-isu yang terkait dalam decision Tree learning untuk materi dalam video ini kita akan membahas isu
[00:00:25–00:00:38] yang pertama yaitu overfitting dalam video-video sebelumnya kita sudah mempelajari bagaimana tahapan dalam decision Tree Learning Kita sudah
[00:00:38–00:00:52] belajar dengan data yang berupa simbolik dan semua datanya lengkap namun sebetulnya terdapat beberapa isu dalam decision tree learning antara lain yang pertama adalah overfitting dari training
[00:00:52–00:01:04] data kemudian Bagaimana kalau atribut yang akan dipelajarinya berupa nilai kontinyu dan karena jika dalam training examples atau dataset yang akan kita pelajari terdapat
[00:01:04–00:01:18] nilai yang hilang dan ada juga kemungkinan pengukuran alternatif untuk menentukan atribut terbaik ketika ada atribut-atribut tertentu yang cenderung
[00:01:18–00:01:30] untuk dipilih pada dia sebetulnya tidak mewakili atribut yang terbaik dalam menentukan kelas dan isu yang kelima adalah bagaimana kalau ternyata di antara atribut-atribut
[00:01:30–00:01:40] yang akan kita pelajari ternyata terdapat biaya yang berbeda di mana kita ingin melakukan pembelajaran sedemikian sehingga biaya yang harus dikeluarkan
[00:01:40–00:01:54] cukup murah nah pada video ini kita akan membahas isu yang pertama yaitu overfitting training data sebetulnya Apa
[00:01:54–00:01:58] sih yang disebut dengan overfit overfed

## Pengertian overfitting

[00:01:58–00:02:11] itu kita katakan ketika kita memiliki suatu hipotesis dimana hipotesis yang dihasilkan dari proses pembelajaran itu sangat sesuai atau memberikan hasil yang
[00:02:11–00:02:24] sangat baik untuk training data atau tradisi examples namun hipotesis tersebut ketika dicobakan untuk keseluruhan distribusi data itu hasilnya
[00:02:24–00:02:36] tidak terlalu bagus Jadi seandainya kita punya sebuah hipotesis h0 yang merupakan himbauan gotta dari suatu himpunan hipotesis kita juga memiliki alternatif hipotesis
[00:02:36–00:02:46] haksen yang juga menjadi anggota dari himpunan hipotesis dan kita memiliki data training untuk Ayo kita juga memiliki keseluruhan
[00:02:46–00:03:00] distribusi data yaitu deh maka suatu hipotesis H dinyatakan overfed ketika error untuk training datanya itu lebih
[00:03:00–00:03:13] kecil daripada hipotesis hak set tapi ketika dicobakan pada keseluruhan distribusi datanya maka error dari hipotesis hal tersebut lebih
[00:03:13–00:03:26] besar daripada hipotesis ha aksen jadi hipotesa itu hanya cocok atau sesuai untuk training data saja Nah untuk
[00:03:26–00:03:32] ilustrasinya Mari kita lihat contoh seperti contoh pada saat pembelajaran

## Contoh pada pohon keputusan

[00:03:32–00:03:45] pemohon keputusan sebelumnya ya kita memiliki data 14hari disini dan pohon yang terbentuk adalah seperti yang tampak pada layar jika kemudian kita memiliki 15
[00:03:45–00:03:58] sesuai dengan data yang ke-15 diumpamakan sebagai data noise dia maka pohon yang akan terbentuk tentunya berbeda dibandingkan dengan pohon yang ada pada layar smartphone
[00:03:58–00:04:11] karena disini ketika Outlook sama dengan Sunny dan Hymne ditanya normal hasilnya tidak lagi semuanya Yes karena berdasarkan data yang ke-15 ini hasilnya klasifikasinya adalah Now tidak bermain
[00:04:11–00:04:25] tenis Oleh karena itu pada saat membentuk pohon keputusan tentunya akan dibentuk lagi pencabangan baru dalam kedalaman yang lebih banyak sehingga pohon yang dihasilkannya pun akan lebih
[00:04:25–00:04:34] kompleks tidak lagi sesederhana pohon yang tampak pada layar Oh ya Nah jika nanti ada lagi penambahan
[00:04:34–00:04:47] data noise yang rendem baru Maka pohon yang terbentuk nantinya akan sesuai dengan training examples yang diberikan baik dia
[00:04:47–00:05:01] mengandung noise ataupun tidak jadi dia sangat Fit sangat sesuai dengan training examples ya tapi kemudian ketika dicobakan ke keseluruhan distribusi datanya untuk data baru yang belum
[00:05:01–00:05:12] digunakan sebelumnya pada tren examples maka kemungkinan hasil prediksinya pun tidak tepat karena apa pohon yang terbentuk itu sebetulnya sudah sangat
[00:05:13–00:05:25] Fit dengan training examples nya Nah karena pohon yang sangat kompleks karena setiap kali ada perbedaan dengan data yang sebelumnya ada tentunya akan kita akan menambahkan
[00:05:25–00:05:37] lagi pencabangan atau kedalaman pada pohon keputusan dia akan semakin Kompleks semakin Fit dengan data trainingnya tapi mungkin untuk prediksi
[00:05:37–00:05:47] data yang belum diketahui sebelumnya akurasinya akan turun Nah itu dalam salah satu contoh atau ilustrasi
[00:05:47–00:05:59] Bagaimana proses pembelajaran dalam decision Tree bisa mengakibatkan overfit terhadap training examples nya sebetulnya tidak hanya data noise saja
[00:05:59–00:06:11] yang menyebabkan overfed bisa saja ketika datanya yang dipelajarinya cukup sedikit maka overfit pun juga bisa terjadi
[00:06:11–00:06:18] nah cover begini bisa mengurangi akurasi 10-25 persen Berdasarkan

## Cara mencegah overfitting

[00:06:18–00:06:28] pengalaman pada persoalan nyata sebelumnya lalu sebaiknya Apa yang perlu kita lakukan supaya pohon yang kita
[00:06:28–00:06:41] hasilkan itu cukup sederhana tapi memiliki akurasi yang cukup baik nge-rap Man terdapat dua pendekatan
[00:06:41–00:06:53] untuk menghasilkan pohon yang cukup sederhana namun memiliki akurasi yang cukup baik yang pertama kita coba untuk
[00:06:53–00:07:04] menghentikan proses penambahan simpul pada kedalaman pohon sebelum dia mencapai akhir yang dimaksud akhir
[00:07:04–00:07:15] disini adalah perfect lesifit semua training data ya Jadi sebelum semua ternyata klasifikasikan dengan baik kita sudah menghentikan dulu proses
[00:07:15–00:07:27] penambahan simpul pada pohon pendekatan yang kedua itu adalah ketika kita sudah membentuk pohon sampai semua simpulnya
[00:07:27–00:07:40] nilainya bisa secara baik eh mengklasifikasikan training datanya artinya disini kita membiarkan dia untuk overfit dulu baru kemudian kita melakukan proming
[00:07:40–00:07:52] atau pemotongan dari pohon keputusan yang sudah dihasilkan pada proses pembelajaran sebelumnya nah setiap pendekatan ini memiliki kelebihan dan
[00:07:52–00:08:06] kekurangan untuk pendekatan yang pertama dimana kita berusaha untuk menghentikan penambahan simpul atau menghentikan menambah kedalaman dalam pohon caranya cukup mudah dia tinggal kita hentikan
[00:08:06–00:08:17] saja pada suatu saat pada suatu langkah kita hentikan proses untuk melakukan pembelajaran atau penambahan simpul pada pohon namun
[00:08:17–00:08:30] Ayo kita menjadi memiliki masalah baru yaitu Kapan sebaiknya kita melakukan proses penghentian pembelajaran karena memang mungkin sulit ketika kita harus
[00:08:30–00:08:44] mengetahui bagaimana Apakah dengan kedalaman dua atau kedalaman tiga atau kedalaman 4 kita sudah memiliki pohon yang cukup sederhana namun bisa memiliki akurasi yang cukup baik nah Sedangkan
[00:08:44–00:08:57] untuk pendekatan yang kedua keuntungannya adalah sudah banyak digunakan dalam praktek dan dia memiliki kecenderungan lebih sukses dibandingkan pada pendekatan yang pertama
[00:08:57–00:09:09] namun kesulitannya tentunya kita memerlukan langkah yang lebih banyak karena apa kita harus membentuk dulu pohonnya sampai semua training datanya terklasifikasi kan dengan baik ya
[00:09:09–00:09:21] Artinya kita membiarkan dia overfit dulu ngantuk sampai coverfit mungkin saja kita perlu membentuk pohon dengan kedalaman yang cukup banyak baru Setelah itu kita tambahkan langkah lagi untuk
[00:09:21–00:09:33] melakukan pruning setelahnya nah mau pendekatan yang pertama ataupun pendekatan kedua yang dilakukan sebetulnya yang lebih penting lagi
[00:09:33–00:09:47] adalah bagaimana atau kriteria apa yang bisa kita gunakan untuk menentukan bahwa pohon yang dihasilkan ini adalah pohon
[00:09:47–00:09:58] yang sudah final dengan akurasi yang cukup baik ya jadi idenya adalah kita mau membuat pohon sesederhana mungkin
[00:09:58–00:10:02] jadi Apakah dia kemudian dipangkas dulu

## Evaluasi pohon dan data validasi

[00:10:02–00:10:15] sebelum sampai overfit atau dibiarkan overfit dulu baru kemudian dipangkas maka yang penting untuk kita ketahui adalah bagaimana menilai bahwa suatu
[00:10:15–00:10:28] pohon yang sudah dipangkas itu memberikan akurasi yang cukup baik terdapat tiga pendekatan untuk
[00:10:28–00:10:39] menentukan apakah pohon hasil pemangkasan kita sudah final yang artinya sudah memberikan akurasi yang cukup baik yang pertama kita memisahkan antara training examples yang digunakan
[00:10:39–00:10:53] untuk membentuk pohon dengan validation untuk menguji apakah hasil pemangkasan tadi memiliki akurasi yang sudah cukup baik biasanya digunakan 2/3 untuk
[00:10:53–00:11:05] training membentuk pohon sepertiganya untuk validasi untuk pendekatan yang kedua kita menggunakan semua teriring data baik untuk pembentukan pohonnya maupun untuk
[00:11:05–00:11:18] pengujian dan pohon hasil pemangkasan nya Nah ketika kemudian hasil pemangkasan tadi pada keseluruhan data yang ada memiliki akurasi yang cukup
[00:11:18–00:11:30] baik maka dia akan diambil sebagai pohon yang final untuk pendekatan yang ketiga terdapat pengukuran secara eksplisit mengenai panjangnya informasi yang harus
[00:11:30–00:11:43] dikirimkan terkait training examples dan pohon keputusannya dari sini kita menggunakan beach seperti dalam information theory Dan harapannya pohon
[00:11:43–00:11:53] keputusan yang dihasilkan bisa seminimal mungkin sehingga panjang informasi yang perlu dikirimkan ketika kita mengambil sebuah examples untuk mengetahui
[00:11:53–00:12:00] kelasnya atau hasil hipotesisnya kita ia berusaha menerapkan heretic minimum

## Minimum description length

[00:12:00–00:12:13] description leave principle jadi sebisa mungkin panjangnya yang dihasilkan itu seminimal mungkin nah formulanya adalah untuk MDL minum description lainnya
[00:12:13–00:12:24] adalah kita berusaha mendapatkan bentuk encoding terhadap hipotesis pohon keputusannya ditambahkan dengan bentuk encoding
[00:12:24–00:12:36] untuk data yang diujikan terhadap hipotesis tersebut keduanya ketika dijumlahkan panjangnya itu memiliki panjang yang cukup minimal Nah dengan
[00:12:36–00:12:49] demikian harapannya adalah kita tetap mendapatkan pohon sesederhana mungkin namun akurasinya juga sudah cukup baik untuk memprediksi data kedepannya
[00:12:49–00:13:02] lebih detil mengenai MDL bisa anda baca dalam buku machine Beto Michelle pada subbab nah sebetulnya bagaimana kita
[00:13:02–00:13:16] memanfaatkan validation set untuk mengurangi error pada saat melakukan pemangkasan pada pohon hasil pembelajaran Nasa the kita mau mempertimbangkan sebuah atribut atau
[00:13:16–00:13:28] nodya simpul pada pohon keputusan untuk kita pruning maka sebaiknya kelas apa yang harus diberikan pada daun simpul daunnya maka Biasanya kita bisa mengusai
[00:13:28–00:13:38] MS suatu nilai klasifikasi yang paling banyak muncul yang berhubungan pada not tersebut ya kita SM kelas tersebut
[00:13:38–00:13:51] nah Artinya kita membangun dulu pohonnya sampai profitku atau sampai semua datanya pada tebing sampel terklasifikasi kan dengan baik Baru
[00:13:52–00:14:03] kemudian kita potong ini Nah kita makan melakukan pemisahan antara drink samples dengan data untuk validasinya
[00:14:03–00:14:17] jadi kita akan melakukan Brunei sampai proses pemotongan itu justru mengakibatkan akurasinya makin buruk nah ketika belum sampai pada tahap tersebut
[00:14:17–00:14:29] maka kita mengevaluasi dampak dari pemotongan pohon pada himpunan validasi
[00:14:29–00:14:40] dan kita akan menghapus simpul yang Jika ternyata dia dipotong maka akurasinya bisa meningkat
[00:14:41–00:14:52] tapi proses ini dia akan baik digunakan pada saat kita memiliki data yang cukup banyak sehingga kita bisa melakukan pemisahan untuk training
[00:14:52–00:15:05] examples dan untuk validation setnya tapi kalau datanya cukup sedikit ketika kita pisahkan antara training examples dengan validation set maka pada saat membentuk pohon pun tray smp-nya sudah
[00:15:05–00:15:10] sedikit maka kemungkinan untuk pemotongannya pun menjadi bisa

## Pruning berbasis aturan

[00:15:10–00:15:23] mengakibatkan akurasi pohon yang dihasilkan semakin buruk nah ketika datanya terbatas Maka terdapat peningkatan atau perbaikan dari
[00:15:23–00:15:35] algoritma id3 yaitu pada algoritma sih four point five yang ditemukan ditemukan oleh online ini dia berusaha untuk membentuk pohon sedemikian sehingga semua training
[00:15:35–00:15:48] example Ciater klasifikasikan dengan baik ya Jadi sampai overfed pun tidak menjadi persoalan Kemudian dari sana hasil pengepul tulisannya diubah
[00:15:48–00:15:58] representasinya menjadi sekumpulan aturan event kita sudah belajar di modul sebelumnya bahwa representasi pohon keputusan itu juga bisa dibentuk menjadi
[00:15:58–00:16:11] keputusan yang berupa kumpulan aturan events nah kemudian ketika sudah dalam bentuk kumpulan aturan fifteen kita coba
[00:16:11–00:16:24] hilangkan satu atau lebih proposisi atau atribut yang ada di bagian IV untuk kemudian ketika sudah dihilangkan kita
[00:16:24–00:16:37] hitung akurasinya lalu kita Urutkan Crush yang sudah dipangkas tadi berdasarkan perkiraan akurasinya
[00:16:37–00:16:50] dan kemudian urutan Mini nanti yang akan diterapkan ketika kita akan mengklasifikasikan data baru dalam hipotesis ini
[00:16:50–00:17:04] cewek ilustrasinya dengan sebagai berikut misal kita sudah memiliki pohon keputusan hasil pembelajaran teknik sampel seperti yang tampak pada layar maka kita bisa mengubahnya menjadi
[00:17:04–00:17:17] bentuk aturan event contohnya adalah seperti ini kita tahu dalam satu plastik tuh bisa terbentuk dalam satu produk nah ketika melakukan Brunei
[00:17:17–00:17:31] maka decision rules yang pertama if Outlook sama dengan Sunny and humidity = kita coba hilangkan salah satu proposisi atau atribut di bagian IV ya
[00:17:31–00:17:43] jadi produknya bisa menjadi Ivo blog sama dengan Sunny dan no atau menjadi if you my life = Dino hasil perundingan ini kita coba kan
[00:17:43–00:17:54] dalam teknik sampel semua pun dalam validation set untuk kemudian kita lihat akurasinya meningkat atau justru menurun Nah kita coba kan untuk semua
[00:17:54–00:18:06] decision rules atau aturan FDN yang dihasilkan dari pohon keputusan yang tampak pada layar
[00:18:06–00:18:18] Nah kalau dalam algoritma SilverQueen five Kita juga bisa menerapkan hasil perundingan pinknya untuk diujikan pada training set jadi tidak harus dipisahkan antara validation
[00:18:18–00:18:29] set dengan streaming set Nah kenapa sih sebetulnya kena kau kita harus mengubah dulu dari decision Tree menjadi decision rules karena sebetulnya ketika kita
[00:18:29–00:18:41] sudah mengubah suatu pas pada decision Tree menjadi rules maka kita bisa memisahkan pas yang berbeda itu menghasilkan sebuah suatu roll yang
[00:18:41–00:18:55] berbeda pula sehingga ketika melakukan pemotongan itu bisa independen antar rusnya oke karena ketika kita memotongnya nanti masih dalam bentuk decision Tree ketika kita potong sebuah node maka
[00:18:55–00:19:07] beberapa harus akan ikut menerima akibatnya dan itu akan memusingkan kita ketika melihat rules mana saja yang sebetulnya ikut mendapatkan efek pada
[00:19:07–00:19:21] saat suatu not dihapus tapi ketika kita sudah mengubah dalam betuk rule kemudian kita menghapus proposisi atau atribut dalam sebuah rotadi makaru yang lain tetap akan memiliki atribut atau not
[00:19:21–00:19:33] atau proposisi tersebut ndak kemudian alasan Yang kedua anda Ayo kita tidak melihat apakah suatu node
[00:19:33–00:19:45] atau proposisi atau atribut yang dihapus itu sebetulnya atribut yang lebih dekat kerut akar atau atribut yang Justru lebih dekat ke daun karena kalau
[00:19:45–00:19:56] misalnya tidak dalam bentuk rules masih dalam bentuk decision Tree ketika kita menghapus suatu atribut yang dekat dengan akar pohon Makita menjadi pusing
[00:19:56–00:20:02] kalau begitu nanti simpul-simpul yang berada dibawahnya bagaimana kaitannya

## Penutup

[00:20:02–00:20:14] dengan akar ketika simpul yang dekat dengan akar itu dihapus nah ketika bentuknya sudah dalam decision rule Maka hal itu tidak perlu kita pusingkan lagi selama kita menghapus maka harus yang
[00:20:14–00:20:26] lainnya pun akan tetap memiliki proposisi seperti yang dia miliki Ini alasan yang ketiga adalah decision rules biasanya lebih mudah dipahami oleh
[00:20:26–00:20:38] manusia dibandingkan dalam bentuk sin-30 karena itu cara ini yang banyak dipakai dan ini adalah diterapkan pada algoritma
[00:20:38–00:20:50] Survive ya untuk melakukan pruning pada pohon keputusan supaya lagi-lagi ingat tujuan kita di awal adalah menghindari overfed pohon kita sesederhana mungkin
[00:20:51–00:21:02] tetapi memiliki akurasi yang cukup baik demikianlah video mengenai isu disentri dari yang pertama yaitu apa
[00:21:02–00:21:12] fitting beserta penanganannya Selamat belajar ya

---

# 06. Continuous-Valued Attribute

Sumber: https://www.youtube.com/watch?v=7x-62Kqj04k
Bahasa: Indonesia  |  Durasi video: 00:07:13  |  Metode: subtitle otomatis asli YouTube

> Catatan: Ini adalah transkrip dari subtitle otomatis, bukan hasil audit audio manual. Istilah yang tidak jelas mungkin perlu diperiksa ulang.

## Pengantar

[00:00:05–00:00:13] Halo semuanya. Masih bersama Ulfa dan kita masih membahas isu-isu seputar decision tree learning.
[00:00:14–00:00:26] Kali ini kita akan membahas bagaimana jika atribut yang akan dipelajari bukan berupa nilai nominal tapi berupa nilai continue.
[00:00:26–00:00:34] Seperti yang sudah pernah kita bahas pada video sebelumnya, terdapat lima isu di dalam decision tree learning.
[00:00:34–00:00:43] Kali ini kita akan membahas isu yang terkait dengan atribut yang memiliki nilai continue.
[00:00:43–00:00:55] Algoritma ID3 yang sudah kita pelajari sebelumnya menuntut kita untuk melakukan pemrosesan terhadap atribut yang sifatnya nominal atau simbolik

## Mengubah atribut kontinu menjadi ambang batas

[00:00:55–00:01:04] sehingga jelas nilainya. Misalnya untuk atribut outlook, kemungkinan nilainya ada tiga yaitu sunny, overcast atau rain.
[00:01:04–00:01:13] Nah, bagaimana jika ternyata atributnya adalah berupa nilai continue? Maka yang bisa kita lakukan adalah dengan melakukan diskritisasi.
[00:01:13–00:01:26] Jadi atribut yang memiliki nilai continue tersebut kita buat seolah-olah menjadi suatu atribut yang memiliki nilai diskrit dengan
[00:01:26–00:01:37] ambang batas tertentu yaitu C. Jadi kita nanti bisa menentukan pencabangan untuk atribut tersebut adalah
[00:01:37–00:01:49] true jika nilai atributnya lebih kecil daripada C dan jika nilainya lebih besar daripada ambang batas, maka
[00:01:49–00:01:57] nilainya akan menjadi false. Jadi cukup dua pencabangan ini dengan suatu nilai ambang batas tertentu.
[00:01:58–00:02:08] Nah, misalnya saja kita memiliki temperatur yang tidak lagi berupa atribut nominal tapi berupa nilai kontinu seperti ini.
[00:02:08–00:02:22] Maka kita memiliki nilai temperatur dengan kelasnya masing-masing. Ketika kita sudah mengurutkan nilai temperatur dari kecil ke besar, maka kita mencoba mencari ambang batas nilai
[00:02:22–00:02:29] C tadi di suatu nilai yang memiliki kelas yang berbeda.
[00:02:29–00:02:42] Di sini berarti potensialnya itu ada di antara 48 dan 60 dan threshold berikutnya yang mungkin dijadikan ambang batas adalah antara 80
[00:02:42–00:02:48] dengan 90 karena di antara batas-batas inilah kelasnya berubah.
[00:02:48–00:02:56] Yang tadinya no menjadi yes, yang tadinya yes yang tadinya yes menjadi no. Sehingga kita punya dua kemungkinan

## Kandidat nilai ambang

[00:02:56–00:03:07] nilai C atau nilai ambang batas yang bisa menjadi kandidat untuk menjadi pencabangan pada atribut tersebut.
[00:03:07–00:03:18] Yaitu yang pertama nilai tengah antara 48 dengan 60 dan kandidat yang kedua itu adalah nilai tengah antara 80 dan 90.
[00:03:18–00:03:29] Lalu mana yang sebaiknya kita pilih? Yang sebaiknya kita pilih adalah yang memiliki nilai gain terbesar.
[00:03:29–00:03:40] Maka kita menggunakan information gain sama seperti cara kita mencari atribut terbaik ketika mau memilih suatu atribut untuk diletakkan pada node tertentu.
[00:03:40–00:03:51] Nah, yang memiliki gain terbaik inilah yang menjadi kandidat untuk diletakkan sebagai break point pada simpul tersebut.
[00:03:51–00:04:00] Mari kita lihat ilustrasi berikut ini. Kita memiliki contoh data sederhana ya, hanya ada enam data dan kita hanya fokus pada atribut temperatur yang memiliki

## Memilih ambang dengan information gain

[00:04:00–00:04:12] nilai kontinu. Pertama kita urutkan dulu datanya berdasarkan atribut nilai continue tersebut dari mulai nilai terkecil sampai yang terbesar dan kita sesuaikan
[00:04:12–00:04:26] kelasnya untuk setiap data yang bernilai continuous tersebut. Nah, kemudian kita cari nilai mana saja yang saling bertetangga dan memiliki kelas yang berbeda.
[00:04:26–00:04:33] Maka di sini kita memiliki dua kandidat ya, yaitu antara nilai 48 dan 60 kelasnya berubah.
[00:04:33–00:04:41] Kemudian di antara nilai 80 dan 90 kelasnya juga berubah. Berbeda ya dengan tetangganya.
[00:04:41–00:04:53] Nah, dari dua kandidat ini kita mencari nilai tengahnya yaitu 54 nilai tengah antara 48 dan 60 dan 85 nilai tengah antara 80 dan 90.
[00:04:53–00:05:07] Kemudian kita cari gain dari setiap kandidat tersebut. Cara mencari gain-nya sama persis seperti yang sudah kita pelajari sebelumnya ya dengan memanfaatkan entropi data.
[00:05:07–00:05:14] Nah, dari sana nanti kita akan menemukan berapakah gain ketika kandidatnya 54.
[00:05:14–00:05:27] Di situ kita tahu bahwa kalau temperaturnya batasnya adalah 54 jika kurang dari 54 terdapat dua Semuanya berkelas no. Jika lebih besar sama dengan 54 terdapat empat
[00:05:27–00:05:38] dengan tiga berkelas yes dan satu berkelas no. Sedangkan untuk 85 jika nilai temperatur kurang dari 85 terdapat lima
[00:05:38–00:05:50] tiga berkelas yes, dua berkelas no. Jika lebih besar dari 85 maka terdapat satu dan kelasnya adalah no.
[00:05:50–00:06:02] Nah, proses mencari gain untuk setiap kandidat ini nanti bisa dilakukan bersama-sama dengan mencari gain untuk atribut nominal yang lain.
[00:06:02–00:06:07] Maka kita akan bandingkan berapakah gain untuk gain untuk
[00:06:09–00:06:19] untuk ambang batas 54 pada temperatur dan juga gain untuk ambang batas 85 pada temperatur. Lalu kita pilih gain mana yang terbaik.
[00:06:19–00:06:26] Gitu ya dan itu nanti yang akan menjadi atribut untuk diletakkan pada simpul pohon yang pada saat itu sedang kita

## Penutup

[00:06:26–00:06:37] periksa. Nah, beginilah caranya untuk menangani atribut yang bernilai continue. Maka kita coba diskritisasi
[00:06:37–00:06:44] dengan mencari ambang batas nilai yang bisa memisahkan cukup baik kelasnya.
[00:06:44–00:06:56] Sama seperti yang nominal. Kita mencari atribut yang bisa memisahkan dengan baik berdasarkan kelasnya.
[00:06:56–00:07:10] Demikianlah video mengenai penanganan atribut dengan nilai continue pada saat proses pembelajaran dalam Selamat belajar.

---

# 07. Missing Attribute Values

Sumber: https://www.youtube.com/watch?v=ZR7l0FYZLF8
Bahasa: Indonesia  |  Durasi video: 00:09:20  |  Metode: subtitle otomatis asli YouTube

> Catatan: Ini adalah transkrip dari subtitle otomatis, bukan hasil audit audio manual. Istilah yang tidak jelas mungkin perlu diperiksa ulang.

## Pengantar

[00:00:00–00:00:11] halo halo semuanya Masih bersama saya Ulfa dalam rangkaian video untuk isu-isu
[00:00:11–00:00:25] dalam decision Tree learning kali ini kita akan belajar Bagaimana penanganan pada suatu atribut yang mengandung nilai yang hilang itu nah mengingatkan kembali Berikut ini
[00:00:25–00:00:37] adalah issue-issue yang ada pada decision Tree Learning Kita sudah membahas mengenai overfitting kemudian atribut yang bernilai ketik nah sekarang kita
[00:00:37–00:00:51] akan membahas Bagaimana menangani adanya nilai yang hilang pada suatu atribut pada saat baik kita melakukan proses pembelajarannya maupun pada saat klasifikasinya
[00:00:51–00:00:57] ini memang jika kita menemukan suatu examples yang salah satu nilai pada

## Mengisi dengan nilai yang paling sering

[00:00:57–00:01:10] sebuah atributnya hilang Maka terdapat beberapa strategi yang bisa kita lakukan yang pertama adalah dengan mengisi nilai yang hilang tersebut dengan nilai yang
[00:01:10–00:01:22] paling banyak muncul untuk atribut tersebut ya jadi nilai hilang pada suatu atribut terlihat nilai apa yang paling banyak muncul untuk aktivitas sebut alternatif kedua adalah kita lihat dulu
[00:01:22–00:01:35] untuk atribut yang nilainya hilang pada examples tersebut atau data tersebut kita lihat kelasnya Apakah kelas dari Instance atau examples yang nilainya
[00:01:35–00:01:45] hilang nah kemudian kita cari Instance lain yang kelasnya sama lalu diantar instansi yang kelasnya sama tadi kita

## Membagi data berbobot

[00:01:45–00:01:57] cari nilai apa yang paling banyak muncul untuk atribut yang nilainya hilang pada example seputar lebih diisikan untuk sebegitu nah alternatif yang lain adalah
[00:01:57–00:02:11] dengan memberikan suatu probabilitas pada nilai yang hilang Jadi kalau misalnya atribut tersebut memiliki dua kemungkinan nilai maka kita usai dengan
[00:02:11–00:02:24] dua kemungkinan nilai tersebut Tapi masing-masing kemungkinan akan memiliki probabilitas tertentu dan ini yang digunakan di dalam algoritma si four point five yang merupakan perbaikan dari
[00:02:24–00:02:36] algoritma id3 nah ketika dia atribut yang hilang pada saat mencari nilai gamenya pada examples ya maka kita tidak
[00:02:36–00:02:49] lagi mengikutsertakan data atau example atau Instance the yang memiliki nilai yang hilang tadi Oh ya jadi ketika kita mau menghitung
[00:02:49–00:02:56] game suatu atribut maka data yang nilainya hilang untuk atribut tersebut tidak kita sertakan dalam proses

## Menghitung gain dengan data hilang

[00:02:56–00:03:09] perhitungan jadi misalnya ini saya punya 11 examples tapi ada satu data hilang sehingga saya hanya punya 10 nih yang nilai untuk atribut hanya diketahui maka
[00:03:09–00:03:23] caranya adalah untuk menghitung gamenya saya akan mengalihkan proporsi data yang diketahuinya yaitu 1011 kemudian dikalikan dengan nah proses belakangnya itu adalah proses menghitung
[00:03:23–00:03:33] geng seperti biasa yaitu entropi dari esnya tapi ingat esnya disini juga hanya memperhitungkan nilai yang diketahui
[00:03:33–00:03:46] saja yah jadi ada 10 nah kemudian pengurangnya yaitu total dari proporsi kali entropi setiap kemungkinan nilai untuk atribut tersebut
[00:03:46–00:03:59] ini juga hanya memperhitungkan data yang diketahui nilainya sehingga data yang missing itu tidak termasuk dalam proses penghitungan
[00:03:59–00:04:12] ke itu ketika mencari gamenya nah ketika misalnya di atribut ini ternyata memiliki gender besar maka yang harus kita lakukan kan melakukan pencabangan untuk setiap kemungkinan nilai dan kita
[00:04:12–00:04:26] pilih datanya mana yang memiliki nilai satu misalnya mana yang memiliki nilai kemungkinan yang kedua jika Misalnya tributa ini memiliki dua kemungkinan nilai nah tapi bagaimana dengan Instance

## Pencabangan dengan nilai hilang

[00:04:26–00:04:37] atau examples yang tadi tidak ketahuan nilainya untuk atribut ini maka kita lakukan adalah dengan membaginya dan proporsi tertentu sesuai dengan nilai
[00:04:37–00:04:50] yang diketahui misalnya nih dari 10 data yang diketahui nilainya 6 itu memiliki nilai misalnya satu gitu ya dan empat data
[00:04:50–00:05:01] atau empat examples itu memiliki nilai V2 atau nol maka berarti kita tambahkan 6/10
[00:05:01–00:05:11] nilai V1 ke dalam pecabangan untuk v1dan 4 persepuluh kita tambahkan untuk
[00:05:11–00:05:23] pencabangan nilai Karena pada saat pembelajaran decision Tree learning sebelumnya yang kita pelajari semua datanya kan nominal
[00:05:23–00:05:35] jadi kita bisa memisahkan datanya dengan baik dan semua datanya lengkap Yes nya ada berapa kemungkinan nilainya ada lima examples maka Ya sudah lima SMP masuk ke
[00:05:35–00:05:47] satu cabang tertentu tetapi ketika ada nilai yang hilang maka proses pencabangannya itu mungkin ada proporsi tertentu yang tidak lagi utuh nilainya tidak lagi integer karena apa
[00:05:47–00:05:55] mempertimbangkan semua kemungkinan nilai untuk instansi atau examples yang

## Klasifikasi ketika nilai hilang

[00:05:55–00:06:09] nilainya hilang nah proses yang sama itu nanti juga kita terapkan pada saat kita melakukan klasifikasi jadi misalnya pohonnya sudah terbentuk maka untuk atribut ah yang
[00:06:09–00:06:22] terdapat nilai yang hilang tadi maka kita punya proporsi bahwa dia itu mungkin punya nilai V1 dengan proporsi 610d dia juga mungkin punya nilai lv2
[00:06:22–00:06:33] dengan proporsinya 4/10 ini juga bisa kita terapkan juga pada saat proses klasifikasi jadi ada bobot nah kelasnya nanti mungkin jadi dihitung dua-duanya
[00:06:33–00:06:47] semua kelas kemungkinannya akan dihitung dengan nilai proporsinya mana yang lebih besar itulah yang akan menjadi keras akhirnya nah dalam algoritma sea
[00:06:47–00:07:01] fourpoint fase itu terdapat penanganan khusus untuk missing value yang dituliskannya dalam bentuk tanda tanya yang menyatakan sebagai null value nah ini artinya tiga diisikan dengan
[00:07:01–00:07:07] nilai tertentu seperti alternatif-alternatif sebelumnya tapi dianggap sebagai sebuah nilai tersendiri

## Nilai hilang sebagai kategori tersendiri

[00:07:07–00:07:19] jadi ada nilai sendiri yang tanda tanya itu yaitu novel itu hanya harus dilihat kasus per kasus karena tidak Untuk Sembarang kasus ini bisa diterapkan nah
[00:07:19–00:07:32] dia tidak akan sesuai diterapkan pada saat nilai yang hilang yang misinya itu karena alasannya bukan karena memang dia itu nilai null value
[00:07:32–00:07:45] Jadi sebetulnya di ada nilainya tapi masalahnya karena misalnya nih contohnya untuk data gula darah gitu ya karena dia terlalu tinggi atau terlalu rendah maka dia Jadi tidak ada nilainya tapi bukan
[00:07:45–00:07:56] nulis sebetulnya dia sehingga tidak bisa diterapkan sebagai sepeda trail you hal yang sama juga ketika misalnya ada data untuk menyatakan Apakah seorang Pasien
[00:07:56–00:08:07] itu fragment saat hamil atau tidak Nah kalau misalnya pasiennya itu pria maka harusnya dia bukan dianggap sebagai dulu
[00:08:07–00:08:20] tapi now karena apa kalau yang lalu itu misalnya ada kalau dia pasien wanita usianya misalnya 25 tapi datanya itu
[00:08:20–00:08:32] tidak diketahui Apakah dia hamil atau tidak anu itunya sehingga dianggap sebagai novel you Nah jadi kita harus tahu juga kapan kita menerapkan missing value
[00:08:32–00:08:45] Hey nilai yang berbeda ya seolah-olah kita punya kemungkinan nilai untuk atribut tersebut itu bertambah dengan yang tanda tanya ini nah ini kira-kira
[00:08:45–00:08:55] penanganan missing value dalam decision Tree learning memang sebagian besar ini sudah difasilitasi dalam algoritma

## Penutup

[00:08:55–00:09:06] serverpoint X yang menjadi perbaikan dari algoritma id3 sebelumnya demikianlah video mengenai penanganan
[00:09:06–00:09:13] isu dalam decision Tree untuk atribut yang memiliki missing value atau nilai
[00:09:13–00:09:22] yang hilang Selamat belajar ya

---

# 08. Alternative Measures for Selecting Attribute

Sumber: https://www.youtube.com/watch?v=4_Ueiuchxrk
Bahasa: Indonesia  |  Durasi video: 00:09:23  |  Metode: subtitle otomatis asli YouTube

> Catatan: Ini adalah transkrip dari subtitle otomatis, bukan hasil audit audio manual. Istilah yang tidak jelas mungkin perlu diperiksa ulang.

## Pengantar

[00:00:00–00:00:12] halo halo semuanya saya Ulfa dalam rangkaian video untuk penanganan isu-isu
[00:00:12–00:00:24] dalam decision Tree learning untuk video kali ini kita akan mempelajari alternatif cara memilih atribut terbaik untuk diletakkan dalam
[00:00:24–00:00:36] simpul pohon keputusan dari video-video sebelumnya kita tahu bahwa terdapat beberapa isu dalam decision tree learning yang sudah kita bahas
[00:00:36–00:00:49] adalah overfitting atribut dengan nilai kontinu dan juga bagaimana menangani trend examples ketika terdapat atribut yang nilainya hilang Nah sekarang kita
[00:00:49–00:01:03] akan membahas mengenai pengukuran alternatif dalam menentukan atribut mana yang terbaik yang bisa kita letakkan dalam simpul pohon keputusan sebetulnya
[00:01:03–00:01:05] Kenapa kita memerlukan alternatif

## Bias information gain

[00:01:05–00:01:18] pengukuran dari pengukuran gen yang sudah kita pelajari pada algoritma editri sebelumnya Mari kita lihat ilustrasi sebagai berikut Shade kita memiliki atribut tanggal
[00:01:18–00:01:31] maka kemungkinan nilai untuk atribut tersebut Pasti sangat banyak yaitu banyaknya hari misalnya kita punya dataset yang mencatat bahwa Apakah Sesuatu hari kita bermain tenis atau
[00:01:31–00:01:44] tidak maka dengan data yang berbeda-beda setir kemungkinan nilai pasti dia akan memiliki satu nilai kelas saja ya hari ini saya bermain tenis Besok saya tidak
[00:01:44–00:01:56] Kemarin saya tidak jadi untuk setiap kemungkinan nilai dia hanya memiliki satu kelas saja sehingga kita tahu entropi untuk setiap kemungkinan
[00:01:56–00:02:07] nilainya pasti tidak akan besar nol yang mengakibatkan ketika kita menghitung Gen untuk atribut tersebut maka entropi data dikurangi dengan nilai yang sangat kecil
[00:02:07–00:02:19] atau nol maka pasti nilainya akan sangat besar mereka itu dia pasti akan terpilih Padahal kita tahu atribut data edit
[00:02:19–00:02:31] tanggal ini sebetulnya dia tidak bisa mengklasifikasikan training examples dengan baik tapi personal karena entropinya dia kecil sehingga pengurang
[00:02:31–00:02:43] dari entropi keseluruhan datanya tidak terlalu signifikan nah Oleh karena itu algoritma si four point five itu berusaha memberikan perbaikan dari
[00:02:43–00:02:52] algoritma id3 dengan menggunakan genre shio dan tidak hanya game saja dalam menentukan atribut terbaik yang

## Gain ratio

[00:02:52–00:03:05] sebaiknya dipilih hal ini untuk mengatasi kasus seperti tadi atribut yang memiliki banyak kemungkinan nilai maka kemungkinan terpilih sebagai atribut terbaiknya semakin besar dengan
[00:03:05–00:03:17] formula Generation nya itu adalah game in Cerme hidupnya sama seperti sebelumnya dibagi dengan Sprite information nah step information sendiri
[00:03:17–00:03:31] itu untuk suatu atribut itu adalah minus dari penjumlahan proporsi proporsi banyaknya data dengan nilai
[00:03:31–00:03:44] kemungkinan tertentu dikalikan log-2 dari proporsi data tersebut Nadine formulanya seperti formula entropi sanjeev gitu ya karena kalau misalnya
[00:03:44–00:03:57] kemungkinan nilainya banyak atau nilai ingat banyak ya maka spread information nya akan memiliki nilai yang cukup besar
[00:03:57–00:04:10] ketika speed information yang memiliki nilai yang cukup besar maka genrenya akan semakin kecil karena pembaginya nilainya besar ya karena generasinya
[00:04:10–00:04:20] kecil maka kemungkinan dia untuk terpilih juga akan semakin kecil tapi kalau misalnya kemungkinan nilai dari suatu atribut atau tadi tidak
[00:04:20–00:04:32] banyak maka kemungkinan genre Sonya bisa lebih besar lagi kemungkinan untuk dipilihnya lebih besar dibandingkan dengan atribut yang banyaknya
[00:04:32–00:04:40] kemungkinan Nilainya sangat besar jadi disini si itu adalah banyaknya data yang

## Split information pada contoh atribut

[00:04:40–00:04:53] dari atribut ada dengan nilai tertentu porno ke mari kita lihat ilustrasinya pada contoh data sheet berikut yang tampak pada layar
[00:04:53–00:05:05] Ayo kita memiliki atribut di tangga Oden kita juga memiliki atribut2 dan atribut tiga tapi kita hanya memberikan contoh untuk yang satu atribut saja yaitu tipe 200 disini akan diperlihatkan Bagaimana
[00:05:05–00:05:17] proses penghitungan Sprite information untuk atribut date dan untuk atribut-atribut 20 tukde kita memiliki
[00:05:17–00:05:30] enam kemungkinan nilai pada dataset ini sehingga kita menjumlahkan proporsi untuk setiap Instance kemungkinan nilainya dikalikan log-2 dari proporsi
[00:05:30–00:05:43] tersebut Oke karena kita punya kemungkinan nilai masing-masing ada satu data maka kita Solo mengalihkan 1/6
[00:05:43–00:05:55] kali log 216 sebanyak enam kali Oh ya tuh cara menghitung subnet information untuk atribut tetot nah sebelum information nanti akan digunakan
[00:05:55–00:06:05] sebagai pembagi untuk menghitung generasi yang dibagi adalah nilai game dari datenya Sedangkan untuk seperti
[00:06:05–00:06:16] information atribut dua maka Prof kemungkinan nilainya ada dua yaitu V1 dan V2 kemungkinan nilai V1 itu ada
[00:06:16–00:06:27] empat maka proporsinya 46 kalikan lock 2406 sedangkan kemungkinan nilai untuk V2 itu hanya ada dua dari enam data yang
[00:06:27–00:06:41] ada berarti proporsinya 2/6 kalian log-2 2/6 Nah begini cara menghitung split information dan lagi-lagi sebagai information atribut2 yang nanti akan menjadi pembagi dari gen atribut2 untuk
[00:06:41–00:06:55] menghasilkan generasi o dari atribut nah tapi kemudian Bagaimana jika misalnya Saya punya sebuah atribut yang punya misalnya dua kemungkinan nilai tapi satu kemungkinan nilai itu
[00:06:55–00:07:09] munculnya sangat banyak hampir setiap instan saya nilainya adalah kemungkinan pertama jadi banyaknya Instance yang memiliki nilai kemungkinan pertama itu
[00:07:09–00:07:21] banyaknya hampir sama dengan es jadi proporsi banyaknya cyber banyaknya es itu mendekati nah jika demikian maka state

## Batasan dan pemilihan atribut

[00:07:21–00:07:33] information yang dihasilkan nanti itu nilainya bisa sangat kecil atau malah mungkin emol kalau misalnya banyaknya si sama dengan banyaknya es ya hanya satu
[00:07:33–00:07:44] kemungkinan Nilai saja untuk atribut tersebut maka kasusnya The Spot informasinya bisa loh hanya karena akibatkan bikin rasionya nilainya menjadi tidak terdefinisi ketika dibagi
[00:07:44–00:07:57] dengan nol atau justru sangat besar karena dibagi dengan nilai yang sangat kecil karena sebagai informasinya sangat kecil Nah untuk menghindari hal ini biasanya diterapkan suatu hari stick
[00:07:57–00:08:08] kita baru menerapkan genre Sio misalnya hanya untuk atribut-atribut yang nilai gamenya diatas rata-rata misalnya
[00:08:08–00:08:21] seperti itu karena sebetulnya pada saat kita membeli atribut terbaik untuk diletakkan pada pohon kita bisa pilih salah satu kita mau memperhitungkan game atau memperhitungkan game rasio gitu ya
[00:08:21–00:08:35] Nah mana yang lebih baik kita harus melihat lagi kasus per kasus mana yang kira-kira bisa memberikan hasil yang lebih baik dalam menghasilkan pohon keputusan yang sesederhana mungkin tapi
[00:08:35–00:08:49] memberikan akurasi yang baik ya Jadi kita tidak menggunakan dua-duanya sebetulnya tapi bisa dipilih salah satu mungkin saja ataupun rasio saja untuk menentukan atribut terbaik yang tertekan
[00:08:49–00:08:54] pada atlet kesimpulan pohon keputusan Dede udah salah satu alternatif dan

## Penutup

[00:08:55–00:09:06] ini digunakan pada algoritma sheafor point five ya untuk mengatasi atribut yang memiliki banyak sekali kemungkinan nilai
[00:09:06–00:09:18] demikianlah video mengenai alternatif pengukuran untuk memilih atribut terbaik yang akan diletakkan dalam simpul pohon keputusan Selamat
[00:09:18–00:09:25] belajar ya

---

# 09. Attributes with Differing Costs

Sumber: https://www.youtube.com/watch?v=GxH3xjtCFcY
Bahasa: Indonesia  |  Durasi video: 00:06:16  |  Metode: subtitle otomatis asli YouTube

> Catatan: Ini adalah transkrip dari subtitle otomatis, bukan hasil audit audio manual. Istilah yang tidak jelas mungkin perlu diperiksa ulang.

## Pengantar

[00:00:00–00:00:12] halo halo semuanya Masih bersama saya Ulfa dalam rangkaian video mengenai isu-isu dalam decision Tree learning
[00:00:12–00:00:25] kali ini kita akan mempelajari bagaimana jika atribut yang akan dibentuk pohon keputusannya memiliki biaya atau cost yang berbeda-beda
[00:00:25–00:00:37] porno dari issue-issue dalam decision Tree learning yang sudah kita pelajari sebelumnya isu Berikut ini adalah isu terakhir yang akan kita bahas yaitu
[00:00:37–00:00:49] Bagaimana jika atribut-atribut yang akan kita pelajari atau akan membentuk pohon keputusan memiliki cost atau biaya yang berbeda-beda sedangkan tujuan kita
[00:00:49–00:01:02] adalah untuk membentuk pohon keputusan dengan biaya seminimal mungkin jadi Adakalanya ketika kita akan membentuk pohon keputusan dari training examples

## Biaya atribut dalam klasifikasi

[00:01:02–00:01:15] yang dimiliki kita berharapnya pohon keputusan tersebut lebih mengutamakan atribut-atribut yang berbiaya rendah untuk bisa menentukan klasifikasi atau
[00:01:15–00:01:28] keputusan untuk data yang belum terlihat atau belum masuk dalam training examples nantinya ya contohnya misalnya ketika dalam rumah sakit akan ditentukan
[00:01:28–00:01:40] diagnosis penyebab penyakit seorang pasien dari trading sampel sel ada atributnya itu ada temperatur ada hasil biopsi ada denyut nadi juga ada hasil
[00:01:40–00:01:52] tes darah nah ingin ya di sini di kos yang diperlukan dalam penentuan diagnosis nya nanti itu serendah mungkin
[00:01:52–00:02:04] jadi kalau misalnya saya bisa menentukan diagnosis dari seorang pasien cukup dari temperatur denyut nadi dan hasil tes darah maka itu akan lebih baik karena
[00:02:04–00:02:07] apa kalau saya perlu biopsi itu

## Contoh pemeriksaan medis

[00:02:07–00:02:18] memerlukan biaya yang lebih besar biaya baik dari segi moneternya maupun dari kenyamanan pasiennya jadi harapannya Ketika nanti ada seorang pasien datang
[00:02:18–00:02:30] Saya cukup mengambil atribut-atribut yang kosnya rendah saja untuk yang berbiaya mahal itu diperlukan hanya ketika atribut-atribut dengan biaya
[00:02:30–00:02:43] rendah tadi sudah diperoleh namun hasilnya kurang meyakinkan sedangkan kita memerlukan hasil yang lebih reliable baru kemudian dilakukanlah Halo Pak perolehan atribut dengan biaya
[00:02:43–00:02:54] yang lebih mahal nah Oleh karena itu karena adanya perbedaan biaya dari atribut-atribut ini maka cost atau biaya itu juga
[00:02:54–00:03:05] diperhitungkan dalam kalkulasi game untuk setiap atribut karena dari sebelum-sebelumnya kita tidak memperhitungkan cost asumsinya

## Memasukkan biaya dalam pemilihan atribut

[00:03:05–00:03:18] setiap atribut memiliki kos yang sama sehingga ketika kita menghitung gamenya pun kita tidak mempertimbangkan Kosti ini terdapat beberapa penelitian yang
[00:03:18–00:03:29] sudah mengkaji Bagaimana melibatkan kos untuk menentukan atribut terbaik yang termasuk dalam pohon keputusan yang
[00:03:29–00:03:41] pertama ini ada Tan dan Slimmer than 90 dan call 93 dengan formulanya dia untuk memperbaiki formula game sebelumnya yang
[00:03:41–00:03:55] diusulkan dalam algoritma id3 perbaikannya adalah game kuadrat dibagi dengan kos dari atribut tersebut sehingga ketika semakin besar cost-nya maka kemungkinan dia akan terpilih bisa semakin kecil
[00:03:55–00:04:06] enggak penelitian lain dari nunez tahun 1988 dengan formula 2 ^ G dikurangi satu dibagi dengan kos dari atribut tersebut

## Rumus gain yang mempertimbangkan biaya

[00:04:06–00:04:18] plus satu lalu dipangkatkan dengan W gimana W adalah suatu konstanta antara 0-1 yang menunjukkan kepentingan relatif
[00:04:18–00:04:32] dari kos dibandingkan dengan information gamenya magazine 2 formula ini bisa dipilih salah satu ketika atributnya memiliki kos yang berbeda-beda dan kita
[00:04:32–00:04:45] mengetahui kos dari setiap atribut untuk kemudian dilibatkan dalam proses penghitungan game yang nantinya akan tetap kita pilih game terbaik untuk diletakkan pada pohon
[00:04:45–00:04:59] untuk mengakhiri rangkaian video terkait isu-isu dalam disentri learning Berikut ini adalah tihan yang bisa anda kerjakan yang pertama adalah coba dihitung genre untuk akibat oplok anda
[00:04:59–00:05:10] perhatikan terdapat sebuah Instance atau sampel yang missing value nya yang teka-teki topflow kemudian misalnya kalau out look sudah dipilih menjadi simpul atau atribut dalam pohon
[00:05:10–00:05:22] keputusan kira-kira pencabangan untuk waktu sama dengan Sunny isi datanya seperti apa Nah kalau misalnya Kemudian untuk data yang untuk sama dengan Sunny
[00:05:22–00:05:35] tersebut kita mau melakukan diskritisasi terhadap atribut humidity kira-kira berapa threshold nya dan bagaimana pencabangannya jika diasumsikan sudah tidak ada

## Penutup

[00:05:35–00:05:48] lagi proses pembelajaran atau pemilihan atribut yang lain kira-kira simpul daun untuk pencabangan humidity nanti seperti apa coba dikerjakan dan Saya harap anda bisa lebih paham mengenai materi isu-isu
[00:05:48–00:06:02] terkait itu center learning setelah mengerjakan latihan ini demikianlah video mengenai penanganan jika atribut-atribut yang akan dibentuk pohon keputusannya memiliki cost atau biaya
[00:06:02–00:06:09] yang berbeda-beda video ini juga sekaligus mengakhiri rangkaian video mengenai isu-isu dalam decision Tree
[00:06:09–00:06:17] learning Selamat belajar ya

---
