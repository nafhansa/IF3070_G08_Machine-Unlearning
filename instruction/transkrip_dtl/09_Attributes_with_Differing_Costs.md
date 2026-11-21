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
