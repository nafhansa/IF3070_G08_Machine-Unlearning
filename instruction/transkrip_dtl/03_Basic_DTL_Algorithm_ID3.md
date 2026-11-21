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
