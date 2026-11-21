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
