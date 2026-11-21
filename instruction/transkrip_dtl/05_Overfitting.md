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
