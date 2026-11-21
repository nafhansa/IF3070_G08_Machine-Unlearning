# Materi Kelas 09

Sumber: `1793176858056_2026_IF3070_Materi09-KNN-NaiveBayes.pdf`  
Jumlah halaman PDF: 23

Teks PDF di bawah disalin dari lapisan teks. Blok OCR adalah keluaran otomatis dari gambar halaman; ejaan, urutan, dan rumus di dalamnya perlu dicek terhadap PDF. Catatan visual yang ditambahkan akan selalu diberi penanda **[INTERPRETASI VISUAL]**.


## Halaman PDF 1

### Teks PDF

```text
IF3070 Dasar Inteligensi Artifisial
Institut Teknologi Bandung

KNN – Naïve Bayes

Semester I TA 2026/2027
```


<details><summary>OCR halaman (otomatis)</summary>


```text
IF3070 Dasar Inteligensi Artifisial

Institut Teknologi Bandung

KNN — Naive Bayes

Semester | TA 2026/2027

CF ith were terror torte GF wwwitdacie @nvi920 XX dt @itbomciat
```


</details>


## Halaman PDF 2

### Teks PDF

```text
                            Outline
• Review:
        • What is AI
        • Intelligent Agent: PEAS, Property of Task Environment
        • Problem Solving Agent:
            • Classical Search
            • Local Search
            • Adversarial Search
            • Constraints Satisfaction Problem (CSP)
        • Knowledge Based Agent:
            • Introduction to Knowledge Based Systems (KBS)
            • Rule Based Systems (RBS)
        • Learning Agent:
            • Introduction to Learning and Supervised Learning
            • Introduction to Data Science
• K-NN
• Naïve Bayes
                                                             2
```


<details><summary>OCR halaman (otomatis)</summary>


```text
e Outline

° Review:
°¢ Whatis Al
° Intelligent Agent: PEAS, Property of Task Environment

°* Problem Solving Agent:
° Classical Search
¢ Local Search

¢ Adversarial Search
* Constraints Satisfaction Problem (CSP)

* Knowledge Based Agent:
¢ Introduction to Knowledge Based Systems (KBS)

e Rule Based Systems (RBS)

¢ Learning Agent:
¢ Introduction to Learning and Supervised Learning

¢ Introduction to Data Science

° K-NN
°¢ Naive Bayes
2

CDF ith wrereterncre tortene GB wwwitorcie G) @nv1920 YX gf @itbometas
```


</details>


## Halaman PDF 3

### Teks PDF

```text
3
    01




         Modul : Supervised Learning



             k-Nearest Neighbor



                Inteligensi Buatan
              (Artificial Intelligence)
                     Sekolah Teknik Elektro dan Informatika ITB




                                                       EDUNEX ITB
```


<details><summary>OCR halaman (otomatis)</summary>


```text
ne

Modul : Supervised Learning

k-Nearest Neighbor

Inteligensi Buatan
(Artificial Intelligence)

See ODF ttt teretermien tantens GD wwrwitdncie @nbi920 XK gh entitles
```


</details>


## Halaman PDF 4

### Teks PDF

```text
02

                                  k-Nearest Neighbor


     Supervised Learning

                                                      No hypothesis

     Instance-Based Classifier
      (Store all training data)
                                          Unseen data prediction: Find class from
                                                   similar stored data

         Lazy learner

                                                                                    4
```


<details><summary>OCR halaman (otomatis)</summary>


```text
k-Nearest Neighbor

Supervised Learning

Instance-Based Classifier
(Store all training data)

Lazy learner

No hypothesis

Unseen data prediction: Find class from

similar stored data

EDF fit trerteetermien tantere GD wwwitdacse G) enn1920 XK gh e@itdomeiat
```


</details>


## Halaman PDF 5

### Teks PDF

```text
03

                       Classification (Predict unseen data)

     Measures ‘distance’ of query (unseen data) to all
               instance (in training data)


                     Find k ‘most similar’ instances
                          (k nearest neighbor)


                                Find the majority class from k
                                      nearest neighbor


                    Class/ Label Prediction: Majority Class of k
                                 nearest neighbor                  5
```


<details><summary>OCR halaman (otomatis)</summary>


```text
Classification (Predict unseen data)

Measures ‘distance’ of query (unseen data) to all
instance (in training data)

Find k ‘most similar’ instances
lal .
(k nearest neighbor)

Find the majority class from k
nearest neighbor

Class/ Label Prediction: Majority Class of k
nearest neighbor
```


</details>


## Halaman PDF 6

> **[INTERPRETASI VISUAL]** Dua tabel berdampingan merupakan satu dataset Play Tennis dengan 14 baris. Kolomnya outlook, temp., humidity, windy, dan play; tujuh baris pertama berada di kiri dan tujuh berikutnya di kanan.

**[TRANSKRIPSI MANUAL TABEL GAMBAR]**

| outlook | temp. | humidity | windy | play |
| --- | --- | --- | --- | --- |
| sunny | hot | high | false | no |
| sunny | hot | high | true | no |
| overcast | hot | high | false | yes |
| rainy | mild | high | false | yes |
| rainy | cool | normal | false | yes |
| rainy | cool | normal | true | no |
| overcast | cool | normal | true | yes |
| sunny | mild | high | false | no |
| sunny | cool | normal | false | yes |
| rainy | mild | normal | false | yes |
| sunny | mild | normal | true | yes |
| overcast | mild | high | true | yes |
| overcast | hot | normal | false | yes |
| rainy | mild | high | true | no |

### Teks PDF

```text
04

     Example: Play Tennis Dataset




                                    6
```


<details><summary>OCR halaman (otomatis)</summary>


```text
Example: Play Tennis Dataset

overcast hot normal false

sunny hot high false no sunny mild high false no
sunny hot high true no sunny cool normal false yes
overcast hot high false yes rainy mild normal false yes
rainy mild high false yes sunny mild normal true yes
rainy normal false yes overcast mild high true _-yes
no yes
yes no

cool
rainy cool normal true
cool

normal _— true rainy mild high true

CDF ith weeneternren torte GF wwwitorcie G) @nviv20 X gh @itbometa
```


</details>


## Halaman PDF 7

### Teks PDF

```text
05   Classify New Instance: <Sunny, Cool, High,
                        True>
                Distance

                2          k=1         D-2        Play: No
                1

                3

                3          k=2       D-1, D-2,    Play: No
                3

                2
                                     D-1, D-2,
                2
                           k=3                    Play: No
                2
                                       D-6
                2

                4

                2

                4

                2                                            7
```


<details><summary>OCR halaman (otomatis)</summary>


```text
assity New Instance: <ounny, Cool, High,

~ True>

[senses]
false no

sunny hot high true
overcast hot high false yes
rainy mild — high false
rainy cool normal false

PO ©O WO Ww

33 3

k=2 Tee D-1,D-2, MM Play: No
rainy cool normal true
overcast cool normal true

D-1, D-2,
| k=3 | See Play: No
sunny mild high false ta) D-6

E:

ro]
ie)

sunny cool normal false yes 5

rainy mild normal false yes Fi

sunny mild normal true yes

overcast mild high true yes 2

overcast hot normal false yes °

rainy = mild—sihigh tue no 2 7
```


</details>


## Halaman PDF 8

### Teks PDF

```text
06
                     Notes on k-Nearest Neigbbor


     Advantages                     Disadvantages


                                                    Cost of classifying new
       Approximation can be less
       complex for complex target                       instance high
                function

                                                    Consider all features →
                                                    target function depends
                                                     only on a few features


                                                                              8
```


<details><summary>OCR halaman (otomatis)</summary>


```text
Approximation can be less

wee complex for complex target
function

EDF fit trerteetermien tantere GD wwwitdacse G) enn1920 XK gh e@itdomeiat

sama target function depends

6 Notes on k-Nearest Neigbbor

Cost of classifying new
instance high

Consider all features >

only on a few features
```


</details>


## Halaman PDF 9

### Teks PDF

```text
id     hobi     umur                       pendidikan          kelas       Id   Jarak thd data baru
      1Game     remaja                     sma                         1   1    1+1+1=3
      2Game     dewasa                     s1                          2   2    1+0+0=1
      3Game     dewasa                     diploma                     3   3    1+0+1=2
      4Baca     dewasa                     s1                          3   4    1+0+0=1
      5Olahraga dewasa-muda                s1                          2   5    0+1+0=1
      6Olahraga dewasa-muda                diploma                     3   6    0+1+1=2
      7Game     dewasa-muda                sma                         1   7    1+1+1=3
      8Olahraga dewasa-muda                sma                         1   8    0+1+1=2
      9Baca     dewasa-muda                sma                         1
                                                                           9    1+1+1=3
     10Game     dewasa-muda                s1                          3
                                                                           10   1+1+0=2
     11Baca     Remaja                     diploma                     1
                                                                           11   1+1+1=3
     12Game     remaja                     diploma                     2
     13game     dewasa                     sma                         3   12   1+1+1=3
                                                                           13   1+0+1=2
1. Hitung Jarak setiap instance data latih untuk data uji berikut:
              hobi = olahraga; umur = dewasa; pendidikan = s1
2. Untuk k=5, maka kelas dari data uji di atas adalah: …
                                                                                                      9
```


<details><summary>OCR halaman (otomatis)</summary>


```text
a

Jarak thd data baru

14+14+1=3

1+0+0=1

1+0+1=2

1+0+0=1

0+1+0=1

0+14+1=2

14+14+1=3

COINISO/aA! R)/WIN)] =

0+14+1=2

o

14+14+1=3

_
(oo)

1+1+0=2

—
_—

14+1+1=3

. id |hobi umur pendidikan kelas
1|Game __|remaja sma 1
2IGame __|dewasa St 2
3iIGame__|dewasa diploma 3
4\Baca dewasa St 3
5|Olahraga|dewasa-muda St 2
6|Olahraga|dewasa-muda diploma 3
7iGame_ __|dewasa-muda sma 1
8iOlahraga|dewasa-muda sma 1
giBaca dewasa-muda sma 1

10IGame _|dewasa-muda St 3
11|Baca Remaja diploma 1
12Game _ |remaja diploma 2
13igame dewasa sma 3

=
ye)

14+1+1=3

1. Hitung Jarak setiap instance data latih untuk data uji berikut:
hobi = olahraga; umur = dewasa; pendidikan = s1
2. Untuk k=5, maka kelas dari data uji di atas adalah: ...

CD EF ith wrteternren torte GF wwmitdacie

=
ow

1+0+1=2
```


</details>


## Halaman PDF 10

### Teks PDF

```text
Distance Measurement on Numeric
Attributes



                       Minkowski distance




  Manhattan distance                        Euclidean distance


                                                                 10
```


<details><summary>OCR halaman (otomatis)</summary>


```text
istance vieasurement on Numeric

- Attributes

n 1/p
i=1

Minkowski distance

n 1/2
- D= >. (p.- q,)?
D 2, IP; |! e 2 tt

Manhattan distance Euclidean distance

3

10

CO EF fit weeterren tortre GD wrmitoacie @ni920 XK dt @itbomciat
```


</details>


## Halaman PDF 11

> **[INTERPRETASI VISUAL]** Contoh KNN membandingkan titik baru (brightness 20, saturation 35) dengan titik berlabel Red/Blue memakai jarak Euclidean. Dua perhitungan yang ditunjukkan menghasilkan d1=25 dan d2=33.54.

### Teks PDF

```text
Euclidean distance




                     11
```


<details><summary>OCR halaman (otomatis)</summary>


```text
1/
Brightness Saturatio Class
ightnes aturation D=|>. @,-4)°
5 5 i=1
Brightness Saturation Class 20 35 ? ,
Euclidean distance
40 20 Red
d1 = \(20 - 40)? + (35 - 20)?
50 50 Blue = 400+225 V(X2-X1)?+(Y2-¥1)?
= 625
60 90 Blue =25 ¢ X2=Newentry's brightness (20).
¢ X= Existing entry's brightness.
| = 2 2
10 25 Red d2 = v(20 - 50)? + (35 - 50)
= V900 + 225 ¢ Y2=Newentry's saturation (35).
70 70 Blue = 1125 e Y:=Existing entry's saturation.
= 33.54
60 10 Red
25 80 Blue

CO EF fit weeterren tortre GD wrmitoacie @nb1920 XK gh @itdotciat
```


</details>


## Halaman PDF 12

> **[INTERPRETASI VISUAL]** Tabel kanan menambahkan jarak ke titik (20,35) untuk tujuh contoh: 25, 33.54, 68.01, 10, 61.03, 47.17, dan 45, sesuai urutan baris pada tabel kiri.

**[TRANSKRIPSI MANUAL TABEL GAMBAR]**

| Brightness | Saturation | Class | Distance |
| --- | --- | --- | --- |
| 40 | 20 | Red | 25 |
| 50 | 50 | Blue | 33.54 |
| 60 | 90 | Blue | 68.01 |
| 10 | 25 | Red | 10 |
| 70 | 70 | Blue | 61.03 |
| 60 | 10 | Red | 47.17 |
| 25 | 80 | Blue | 45 |

### Teks PDF

```text
12
```


<details><summary>OCR halaman (otomatis)</summary>


```text
e@ Brightness
40
50
60
10
70
60

25

Brightness

20

Saturation

20

50

90

25

70

10

80

Saturation

39

Class

Red

Blue

Blue

Red

Blue

Red

Blue

Class

Brightness
40
50
60
10
70
60

25

Saturation

20

50

90

25

70

10

80

Fit ween terncien testers GD wwmitdacse @nd1920 XK gh @itbomciat

Class

Red

Blue

Blue

Red

Blue

Red

Blue

Distance

25

33.54

68.01

10

61.03

47.17

45
12
```


</details>


## Halaman PDF 13

### Teks PDF

```text
  Hyperparameters

• What is the best distance to use?
• What is the best value of k to use?
How?
• Very problem-dependent.
• Must try them all out and see what
  works best.
• Use train set and validation set to
  avoid overfitting
                                        Myth: K value should be an odd-number

                                        Instead, test on K-NN Hyperparameter
                                        Observation

                                                                                13
```


<details><summary>OCR halaman (otomatis)</summary>


```text
© Hyperparameters

* What is the best distance to use? 012 A
¢ What is the best value of k to use? on NA |
/

fication Error
°
=]
J

How?
¢ Very problem-dependent.

¢ Must try them all out and see what sos Ay
works best. aos ales |
¢ Use train set and validation set to ooal 5 = 5 “ 3,
avoid overfitting rel sme

Miscla:
r-}
o
Ss
ae

Myth: K value should be an odd-number

Instead, test on K-NN Hyperparameter
Observation

ibs

CDF ith wrrreterncren torte § GF wwwitdrcse G) enviv20 XK gh @itdomcias
```


</details>


## Halaman PDF 14

### Teks PDF

```text
4. Modeling : Mengembangkan Model (Pengetahuan)
Membangun Skenario Pemodelan
Membuat strategi pencarian model terbaik


      C. Menentukan Langkah Eksperimen:
      Untuk mendapatkan model terbaik secara efisien dan efektif




                   Best Guess      One Factor at A Time   Grid Search
                                                                        14
```


<details><summary>OCR halaman (otomatis)</summary>


```text
Oo

Membangun Skenario Pemodelan
Membuat strategi pencarian model terbaik

C. Menentukan Langkah Eksperimen:
Untuk mendapatkan model terbaik secara efisien dan efektif

Best Guess

| 4. Modeling : Mengembangkan Model (Pengetahuan)

i ct ea 1@-@-@-@-@
tot] |G OO-¢-@
©-6-0-6-6 |0 0-6-6
i tot! |e@-6-6-6.

One Factor at A Time

Grid Search
14

CO EF fit weeterren tortre GD wrmitoacie @nb1920 XK gh @itdotciat
```


</details>


## Halaman PDF 15

### Teks PDF

```text
01




     Modul : Supervised Learning



             Naive Bayes



           Inteligensi Buatan
          (Artificial Intelligence)
                 Sekolah Teknik Elektro dan Informatika ITB




                                                              15
```


<details><summary>OCR halaman (otomatis)</summary>


```text
Modul : Supervised Learning

Naive Bayes

Inteligensi Buatan
(Artificial Intelligence)

15

CDF ith wereterncrey tontene GD wwmitdrcie G) @u1920 XX gh @itbomctar
```


</details>


## Halaman PDF 16

### Teks PDF

```text
02

                                Naive Bayes


         Supervised
          Learning
                                    Hypothesis: Probability Model of P(vj)
                                                and P(ai|vj)

     Probabilistic Classifier

                                      Unseen data prediction: Find the
                                        maximum P(vj | a1, a2, ..., an)
       Target function:
     class from finite set
              V
                                                                             16
```


<details><summary>OCR halaman (otomatis)</summary>


```text
Supervised
Hypothesis: Probability Model of P(v;)
and P(a;|v;)

|

Probabilistic Classifier

Unseen data prediction: Find the
maximum P(v; | a1, a, «-, An)

Target function:

class from finite set
Vj
```


</details>


## Halaman PDF 17

### Teks PDF

```text
03

                               Learning Algorithm

     Measures the frequency of every attribute value for
      certain class, and the frequency of every class


                Determine the probability of P(ai|vj)



                           Determine the probability of P(vj)



                           Hypothesis: Probability Model
                                                                17
```


<details><summary>OCR halaman (otomatis)</summary>


```text
: Learning Algorithm

Measures the frequency of every attribute value for
certain class, and the frequency of every class

Determine the probability of P(a;|v;)

q@ Determine the probability of P(v,)

| Hypothesis: Probability Model

a
```


</details>


## Halaman PDF 18

### Teks PDF

```text
04

                   Classification (Predict Unseen Data)


     Compute the projection of attribute probability of query
         (unseen data) for every class -> ∏i P(ai | vj)


                Multiply the result with probability of each class to get ->
                            P(vj | a1, a2, ..., an) = P(vj) . ∏i P(ai | vj)




               Prediction: Class with the maximum P(vj | a1, a2, ..., an)


                                                                               18
```


<details><summary>OCR halaman (otomatis)</summary>


```text
Classification (Predict Unseen Data)

Compute the projection of attribute probability of query
(unseen data) for every class -> J]; P(a; | v;)

Multiply the result with probability of each class to get ->
P(v; | ay, a2, ..., Aq) = P(v;) - TT Pla; | v;)
```


</details>


## Halaman PDF 19

### Teks PDF

```text
05

                          Example: Play Tennis Dataset




       Frequency of        Frequency of       Frequency of           Frequency of
     (sunny|yes) -> 2   (overcast|yes) -> 4   (hot|yes) -> 2   ...   class ‘yes’-> 9

      Frequency of        Frequency of        Frequency of           Frequency of
     (sunny|no) -> 3    (overcast|no) -> 0    (hot|no) -> 2          class ‘no’ -> 5
                                                                                       19
```


<details><summary>OCR halaman (otomatis)</summary>


```text
Example: Play Tennis Dataset

outlook ~=«temp. humidity windy play outlook =6temp. humidity windy play

sunny hot high false no sunny mild high false no

sunny hot high true no sunny cool normal false yes

overcast hot high false yes rainy mild normal false yes

rainy mild — high false yes sunny mild normal true yes

rainy cool normal false yes overcast mild high true yes

rainy cool normal true no overcast hot normal false yes

overcast cool normal true yes rainy mild high true no
Frequency of Frequency of Frequency of Frequency of
sunnylyes) -> 2 overcast|yes) -> 4 hotlyes) -> 2 aa Class ‘yes’-> 9
Frequency of Frequency of Frequency of Frequency of

no) -> 2 Class ‘no’ -> 5

ot eitdome

(Sunny|no) -> 3 (overcast|no)

GO f in

-> 0 (hot|
```


</details>


## Halaman PDF 20

> **[INTERPRETASI VISUAL]** Tabel bawah menghitung frekuensi play=yes/no untuk tiap nilai outlook, temperature, humidity, dan windy dari dataset Play Tennis di atasnya; total kelas adalah 9 yes dan 5 no.

### Teks PDF

```text
05

     Example: Play Tennis Dataset




                                    20
```


<details><summary>OCR halaman (otomatis)</summary>


```text
no
no yes
yes false yes
rainy mild high false = yes sunny mild normal true yes
rainy cool normal false = yes overcast mild high true yes
rainy cool normal true no overcast hot normal false yes
overcast cool normal true yes rainy mild high true no
outlook temperature humidity windy play
yes no yes no yes no yesno yes no
sunny 2 3 hot 2 2 high 3 4 false 6 2 9 5
overcast 4 0 mild 4 2 normal 6 1 true 3 3

rainy 3 2

cool 3 1

UDF ih wenpinens Gp wewibacte (o) envivz

OF Sitbomcrs

20
```


</details>


## Halaman PDF 21

### Teks PDF

```text
06

                            Example: Play Tennis Dataset



     Frequency




                 P(ai|vj)                      P(vj)



                                                           Probability
                                                             Model

                                                                         21
```


<details><summary>OCR halaman (otomatis)</summary>


```text
Example: Play Tennis Dataset

outlook temperature humidity windy play

' yes no yes no yes no yes no yes no
Frequency — sunny 2 3 hot 2 2 high 3 4 false 6 2 9 §

overcast 4 0 mid 4 2 normal 6 1 tue 3 3

rainy 3 2 cool 3 1

PP) |

outlook temperature humidity windy
yes no yes no yes no yes no yes no \ fk
sunny 29 3/5 hot 29 25 high 3/9 4/5 false 6/9 216 9/14 5/14 Probability

overcast 4/9 0/5 ____—-Model_J

3/9 2/5

mild 4/9 2/5
cool 3/9 1/5

normal 6/9 1/5 true 3/9 3/5

rainy 4
```


</details>


## Halaman PDF 22

### Teks PDF

```text
07
                  Classify New Instance: <Sunny, Cool, High, True>

                                          P(ai|vj)                                          P(vj)




                                          P(vj | a1, a2, ..., an) = P(vj) . ∏i P(ai | vj)


P(yes|sunny, cool, high, true)                                   P(no |sunny, cool, high, true)
= P(yes). P(sunny|yes).P(cool|yes).P(high|yes).P(true|yes) = P(no). P(sunny|no).P(cool| no).P(high| no).P(true| no)
= 9/14 . 2/9 . 3/9 . 3/9 . 3/9 = 0.0053                          = 5/14 . 3/5 . 1/5 . 4/5 . 3/5 = 0.0206
                                                                                                               22
```


<details><summary>OCR halaman (otomatis)</summary>


```text
F Pal) |

outlook temperature humidity windy

yes no yes no yes no yes no
sunny 2 ]36 hot 2/9 2/5 high} 3/9)#/5 | false 6/9 2/5
overcast 4/9 0/5  mild_4/9 2/6 ~— normal 6/9 1/5 — true} 3/4 B/5
rainy 3/9 2/5

P(yes|sunny, cool, high, true) P(no |sunny, cool, high, true)
= P(yes). P(sunny |yes).P(cool | yes).P(high|yes).P(true| yes) = P(no). P(sunny|no).P(cool| no).P(high| no).P(true| no)
= 9/14 .2/9 .3/9 . 3/9. 3/9 = 0.0053 = 5/14 .3/5.1/5. 4/5. 3/5 =0.0206

O f in wm Teanatog! Bonderg ® wemitdrcse G en1v20 YX gh eitdometas

2:
```


</details>


## Halaman PDF 23

### Teks PDF

```text
Thank You




            23
```


<details><summary>OCR halaman (otomatis)</summary>


```text
Thank You

EF itn worreterncen tontens GD wowiti.acie G) ends920 XX gh eiidomeiat
```


</details>
