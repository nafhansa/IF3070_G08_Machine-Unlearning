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
