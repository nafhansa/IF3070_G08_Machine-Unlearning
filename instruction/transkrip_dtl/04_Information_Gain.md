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
