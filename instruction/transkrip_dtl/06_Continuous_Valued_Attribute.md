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
