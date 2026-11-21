# Materi Kelas 10

Sumber: `1793176888215_2026_IF3070_Materi10-Decision-Tree.pdf`  
Jumlah halaman PDF: 55

Teks PDF di bawah disalin dari lapisan teks. Blok OCR adalah keluaran otomatis dari gambar halaman; ejaan, urutan, dan rumus di dalamnya perlu dicek terhadap PDF. Catatan visual yang ditambahkan akan selalu diberi penanda **[INTERPRETASI VISUAL]**.


## Halaman PDF 1

### Teks PDF

```text
IF3170 Dasar Inteligensi Artifisial
Institut Teknologi Bandung

Decision Tree Learning
Semester I TA 2026/2027
```


<details><summary>OCR halaman (otomatis)</summary>


```text
meee ni \
C4 a C.YW),

i Artifisial

igens

IF3170 Dasar Intel

Institut Teknologi Bandung

Decis

ing

Tree Learn

ion

Semester | TA 2026/2027

@itb1920 XX gh @itbofficial

BF iin nstitut Teknotogi Bandung ® www.itb.ac.id
```


</details>


## Halaman PDF 2

### Teks PDF

```text
Variable (Attribute) Types

                         Modul : Decision Tree Learning
                         (DTL)

                             Variable (Attribute) Types
                           Source: DataMining Concepts and Techniques
                             by Jiawei Han, Micheline Kamber, Jian Pei

    Nur ULFA Maulidevi




                                                                         2
```


<details><summary>OCR halaman (otomatis)</summary>


```text
© Variable (Attribute) Types

Modul : Decision Tree Learning
(DTL)

Variable (Attribute) Types

Source: DataMining Concepts and Techniques
by Jiawei Han, Micheline Kamber, Jian Pei

CBF | fin tistitut teknotogi Bandung @ _ wowitbacia @itb1920  X gh @itbofficial
```


</details>


## Halaman PDF 3

### Teks PDF

```text
Numeric

                               Quantitative
                               (measurable
                            quantity) à Integer
                              or Real Values              Ratio-Scaled
                                                         (inherent zero
    Interval Scaled
                                                        point, a value can
   (equal-size units,
                                                         be multiple of
      have order)
                                                         another value)


                                         - Years of
              - Temperature                experience
              - Calendar dates           - Weight
                                         - Number of words
                                                                             3
```


<details><summary>OCR halaman (otomatis)</summary>


```text
Numeric

y Quantitative ~~ :
( (measurable \

\ quantity) > Integer

——_ ~~ orRealValues Ratio-Scaled _
“a N — / inherent zero
Interval Scaled ‘ | (
| ) | point, a value can
(equal-size units, \ :
\ / \ be multiple of
\ have order) y
\ y another value) _
y > 7
| - Years of
- Calendar dates - Weight
a D _- Number of words
NX

© FJ in trssituetexnotogi Bandung GQ) wwwitb.ac.id @itb1920  X gh @itbofficial

y

4
```


</details>


## Halaman PDF 4

### Teks PDF

```text
Nominal/ Categorical

                          Symbols or
                         Name of things


       Do not have                        Can represent names
       meaningful                         with numbers not to
          order                           be used quantitatively




                     - Occupation Type
                     - Zip Code
                     - Student_ID
                                                                   4
```


<details><summary>OCR halaman (otomatis)</summary>


```text
C8 | FI in institut Teknoiogi Bandung a) wwwitbacid (©) @itb1920 XX gh @itbofficial
```


</details>


## Halaman PDF 5

### Teks PDF

```text
Binary
                              Only two categories or
                                states (Boolean if
                              states: true and false)


         Symmetric: equally                              Asymmetric:
         valuable and carry                               not equally
          the same weight                                  important



                              - Gender
                              - HIV Positive/ negative




                                                                        5
```


<details><summary>OCR halaman (otomatis)</summary>


```text
i red, green,
Bi, Q,
3 @, 1,
4 Q, Q,

blue
)

0
(|
```


</details>


## Halaman PDF 6

### Teks PDF

```text
Ordinal
                                     Have meaningful
                                     order/ ranking of
                                      possible values

                                                                May be obtained from
magnitude between
                                                                  discretization of
successive values is                                             numeric quantities
    not known
                                useful for registering
                               subjective assessments
                                     of qualities


                       - Drink Size: small, medium, large
                       - Customer Satisfaction: 1, 2, 3, 4, 5
                       - Grades: E,D,C,BC,B,AB,A
                                                                                       6
```


<details><summary>OCR halaman (otomatis)</summary>


```text
Ordinal

magnitude between

not known

successive values is

Have meaningful
order/ ranking of
possible values

May be obtained from

useful for registering
subjective assessments
of qualities

vy

Drink Size: small, medium, large
Customer Satisfaction: 1, 2, 3, 4,5
Grades: E,D,C,BC,B,AB,A

wy

CBF | fin tistitut teknotogi Bandung @ _ wowitbacia @itb1920  X gh @itbofficial

discretization of
numeric quantities |

ON
```


</details>


## Halaman PDF 7

### Teks PDF

```text
  Discrete vs Continuous

has a finite set of values:
Drink size, Age, Medical
test,

                              Discrete   Continuous

has a countably infinite
set of values:
Customer ID, Zip code




                                                      7
```


<details><summary>OCR halaman (otomatis)</summary>


```text
® Discrete vs Continuous
```


</details>


## Halaman PDF 8

### Teks PDF

```text
What, Why, and When

                      Modul : Decision Tree Learning
                      (DTL)



                          What, Why, and When
                          Source: Machine Learning, Tom Mitchell




                                                                   8
```


<details><summary>OCR halaman (otomatis)</summary>


```text
® What, Why, and When

Modul : Decision Tree Learning
(DTL)

What, Why, and When

Source: Machine Learning, Tom Mitchell

CBF | fin tistitut teknotogi Bandung ® wowitdac.id @itb1920 XK gh @itbofficial
```


</details>


## Halaman PDF 9

### Teks PDF

```text
WHAT is DTL

         Method for
    approximating discrete-
    valued target functions
                              Represented by
                               Decision Tree

                                               Can be represented
                                                as set of if-then
                                                      rules




                                                                    9
```


<details><summary>OCR halaman (otomatis)</summary>


```text
WHAT is DTL

Outlook

Sunny Overcast

Humidity Yes
High Normal
No Yes

=
sone

Rain
Wind
Strong Weak
No Yes

© FJ im testiturternoiogi Bandung GQ) wwwitb.acid (©) @itbis20 X ¢h @itbofficial

=
=
```


</details>


## Halaman PDF 10

### Teks PDF

```text
DTL Representation
                     - Each internal node represents test of
                       an attributes
                     - Branch descending from the node
                       corresponds to one possible value
                     - Leaf/ terminal nodes represents
                       classification result
                     Represent a disjunction of
                     conjunctions of constraints
                     on the attribute values of instances
                     (outlook=sunny ∧ humidity=normal)
                     ∨ (outlook=overcast)
                     ∨ (outlook=rain ∧ wind=weak)

                                                               10
```


<details><summary>OCR halaman (otomatis)</summary>


```text
DTL Representation

Zo

Outlook

Humidity

High

/\

Normal

Overcast

Yes

Rain

™

Wind

/\

Strong

/

No

Each internal node represents test of
an attributes

Branch descending from the node
corresponds to one possible value
Leaf/ terminal nodes represents
classification result

Represent a disjunction of
conjunctions of constraints
on the attribute values of instances

(outlook=sunny A humidity=normal)
V (outlook=overcast)
V (outlook=rain A wind=weak)

10

© FJ in trssituetexnotogi Bandung GQ) wwwitb.ac.id @itb1920  X gh @itbofficial
```


</details>


## Halaman PDF 11

### Teks PDF

```text
WHY DTL
        Method for
       approximating
   discrete-valued target
         functions
                            - Popular of inductive inference
                                algorithms
      Represented by        -   Have been successfully
      Decision Tree or          applied to a broad range of
       If-Then Rules            tasks: learning to diagnose
                                medical cases, learning to
                                assess credit risk of loan
    Robust to Noisy Data        applicants


   Capable of learning
   disjunctive expression
                                                               11
```


<details><summary>OCR halaman (otomatis)</summary>


```text
® WHY DTL

Method for
approximating
discrete-valued target
functions

Represented by
Decision Tree or
If-Then Rules

~ d

~ Robust to Noisy Data

>

f
Capable of learning
disjunctive expression

d —

@ ft | IN institut Teknologi Bandung ® www.itb.ac.id @itb1920 X db Gitbofficial
```


</details>


## Halaman PDF 12

### Teks PDF

```text
When we use DTL à Appropriate Problems for DTL
     Instances are represented   For continuous attribute:
      by attribute-value pairs         discretization


      The target function has
      discrete output values

     Disjunctive descriptions
         may be required

      The training data may
          contain errors

      The training data may
     contain missing attribute
              values                                         12
```


<details><summary>OCR halaman (otomatis)</summary>


```text
© When we use DTL > mppropnen | Problems for DTL
```


</details>


## Halaman PDF 13

### Teks PDF

```text
Basic DTL Algorithm (ID3)




                             Basic DTL Algorithm
                                    (ID3)
                            Source: Machine Learning, Tom Mitchell




                                                                     13
```


<details><summary>OCR halaman (otomatis)</summary>


```text
© Basic DTL Algorithm (ID3)

Institut Teknologi Bandung

Basic DTL Algorithm
(ID3)

Source: Machine Learning, Tom Mitchell

as:
```


</details>


## Halaman PDF 14

### Teks PDF

```text
ID3 Algorithm
          Top Down ,                          Choose the
         Greedy Search                       best Attribute
                                                as ‘root’

                                Training
   1. A ß the ‘best‘     No                          4. Sort training
                               Examples
  Decision attribute            perfectly           examples to leaf
    for next node              classified?                nodes

                              Yes

    2. Assign A as                  Stop           3. For each value of
  Decision attribute                                  A, create new
       for node                                    descendent of node
```


<details><summary>OCR halaman (otomatis)</summary>


```text
® ID3 Algorithm

Top Down,
Greedy Search

Choose the

best Attribute
as ‘root’

Training
Examples
perfectly
classified?

1.A € the ‘best' No
Decision attribute — examples to leaf

for next node nodes

4. Sort training

| vo | |

2. Assign A as < Stop ) 3. For each value of
Decision attribute A, create new
for node ==» | descendent of node

CBF | fin tistitut teknotogi Bandung @ _ wowitbacia @itb1920  X gh @itbofficial
```


</details>


## Halaman PDF 15

### Teks PDF

```text
   Decision Tree Learning (Russel & Norvig, 2021)




                                                                                                  Information gain
                                                                                                  Gain ratio


                                                                                                 |A|=2: binary tree
                                                                                                 |A| min 2: n-ary tree




The function PLURALITY-VALUE selects the most common output value among a set of examples, breaking ties randomly.
```


<details><summary>OCR halaman (otomatis)</summary>


```text
® Decision Tree Learning (Russel & Norvig, 2021)

function DECISION-TREE-LEARNING(ezamples, attributes, parent_examples) returns
a tree

if examples is empty then return PLURALITY- VALUE(parent_examples)
else if all examples have the same classification then return the classification

else if attributes is empty then return PLURALITY- VALUE(ezamples) Information gain

else ek _ ee -- 7-77 Gain ratio
A (IMPORTANCE lesye
— aTgMaXy ¢ attributes IMPORTANCE(a, examples) ;
tree—a new decision tree with root test A
for each value vu; of A Yo. ------------------ eee eer |A|=2: binary tree
ers —{e : e€ examples and e.A = vx} |A| min 2: n-ary tree

subtree — DECISION-TREE-LEARNING(eas, attributes — A, examples)
add a branch to tree with label (A = v;) and subtree subtree
return tree

The function PLURALITY-VALUE selects the most common output value among a set of examples, breaking ties randomly.

CB | F | Gin institut teknotogi Bandung ® wowitdacid () e@itb1920 XK gi eitbotficial
```


</details>


## Halaman PDF 16

### Teks PDF

```text
Best Attribute

        “Ideally” can classify
       the training examples     Information
      into subsets, which has        Gain
           the same class




                                               17
```


<details><summary>OCR halaman (otomatis)</summary>


```text
Best Attribute

ee

000000 000000
000000 ©00000
Patrons? Type?
none _ poet fa \ ral aru
C000 80 fe) e@ 00 eo
oo e000 ° @ eco ee

© F) Gin wsstuetecnotogitanaune J wwwitdacid (6) @itb1920 X gh @itbotfcial
```


</details>


## Halaman PDF 17

### Teks PDF

```text
Information Gain




                       Information Gain
                   Source: Machine Learning, Tom Mitchell




                                                            18
```


<details><summary>OCR halaman (otomatis)</summary>


```text
Information Gain

Institut Teknologi Bandung

Information Gain

Source: Machine Learning, Tom Mitchell

® wowitdacid () e@itb1920 XK gi eitbotficial

18
```


</details>


## Halaman PDF 18

### Teks PDF

```text
     Entropy (Information Content)
                                                             S = set of training examples
                 Measurement in
                                                                     Entropy: the
               Information Theory
                                                              minimum number of bits of
                 à impurity of an
                                                            information needed to encode
               arbitrary collection of
                                                                the classification of an
                      samples
                                                                arbitrary member of S

A completely                                        $
homogeneous sample              𝐸𝑛𝑡𝑟𝑜𝑝𝑦 𝑆 = , −𝑝! log % 𝑝!
has entropy of 0.
                                                  !"#

An equally divided
sample has entropy of 1   - S: set of training examples
                          - c: number of classes
                          - pi: proportion of S belonging to class i
                                                                                            19
```


<details><summary>OCR halaman (otomatis)</summary>


```text
S = set of training examples
Entropy: the
minimum number of bits of
information needed to encode
the classification of an
arbitrary member of S

Measurement in
Information Theory
> impurity of an
arbitrary collection of
samples

A completely

Cc
homogeneous sample Entropy(S) = ». —p; logs pj
has entropy of 0. =

An equally divided
sample has entropy of 1

S: set of training examples
c: number of classes
p;: proportion of S belonging to class i

CB FJ i institut Teknotogi Bandung @ wwiitbac.id @itb1920  X gh Citbofficial
```


</details>


## Halaman PDF 19

### Teks PDF

```text
Entropy (Information Content)
                            )

              𝐸𝑛𝑡𝑟𝑜𝑝𝑦 𝑆 = 1 −𝑝& log " 𝑝&
                           &'(


     Data   Class(Y/N)
                                𝐸𝑛𝑡𝑟𝑜𝑝𝑦 𝑆 = −𝑝! log " 𝑝! − 𝑝# log " 𝑝#
      1         Y
      2         Y                               $      $     %       %
                                           = − log "       − log "
      3         Y                               $      $     $       $

      4         Y                          =0

     Data   Class(Y/N)
                                𝐸𝑛𝑡𝑟𝑜𝑝𝑦 𝑆 = −𝑝! log " 𝑝! − 𝑝# log " 𝑝#
      1         Y
      2         N                               "      "     "       "
                                           = − log "       − log "
      3         Y                               $      $     $       $

      4         N                          =1


                                                                         20
```


<details><summary>OCR halaman (otomatis)</summary>


```text
® Entropy (Information Content)

Entropy(S) = ». —p; log, pj

Cc

i=1

Data Class(Y/N)
1 Y
2 Y
3 Y
4 Y
Data Class(Y/N)
1 Y
2 N
3 Y
4 N

Entropy(S) = —py log2 py — Pn log2 Pn

= ~ jlogs (7) ~ jloea (7)

= 0

Entropy(S) = —Py log» Py —Pn log, Pn

= ~ jlogs (5) — joes (7)

20
```


</details>


## Halaman PDF 20

### Teks PDF

```text
Entropy for S with 2 values/ classes
      S contains positive examples
         and negative examples
     Entropy 0: all examples belong to a                                                                           Entropy 1: p+ = p-
       class (no surprises, no message                                                                (1 bit is required to indicate the class of
                need be sent)                                                                                     the drawn example)
                                          I(5/10,5/10) = 1




I(3/6,3/6) = 1 I(2/4,2/4) = 1 I(3/4,1/4)=0.81              I(5/5,0/5)=0 I(0/5,5/5)=0
                                           I(2/6,4/6)=0.92                                                                                      21
 https://www.researchgate.net/publication/320384121_Textklassification_-_Decision_Trees_Random_Forests/figures?lo=1
```


<details><summary>OCR halaman (otomatis)</summary>


```text
Entropy for S with 2 values/ classes

Entropy(S) = —pe logs ps — po logy po

I(5/10,5/10) =1

@°e @ ® Pn)
® @98 @. @2® i oo a
@ e (@) =
e°? e*? °°? S
Oo ° fe) Fe
x a a Ne a Na
- re °° . @ o “.
e e @
*o e Pi e ‘i - —
1(3/6,3/6) =1 1(2/4,2/4) =2 1(3/4,2/4)=0.812 (5/5,0/5)=0  I(o/5,5/5)=0
1(2/6,4/6)=0.92 Fp 21
https://www.researchgate.net/publication/320384121_Texéitlasfifi¢rtionin Decision r4}_Randonid Fof@steffiqpares Nog eitboticial
```


</details>


## Halaman PDF 21

### Teks PDF

```text
Entropy for S with n values/ classes
      Target attribute has n values: entropy can be as large as
                              log2 n




                                                                  22
```


<details><summary>OCR halaman (otomatis)</summary>


```text
© Entropy for S with n values/ classes

Maximum Entropy

w

N

rary

0.75

0.5

0.25

+r O

4 6 8 10 12 14 16
Number of classes

—H max entropy —@—p

probability (equal for all clases)

© FJ im testiturternoiogi Bandung GQ) wwwitb.acid (©) @itbis20 X ¢h @itbofficial

22
```


</details>


## Halaman PDF 22

### Teks PDF

```text
Information Gain

    Gain(S,A) = expected reduction of entropy due to sorting A
    S: set of training examples; A: an attribute



                                                   Find A which has maximum Gain(S,A)




                                                                                        23
```


<details><summary>OCR halaman (otomatis)</summary>


```text
© Information Gain

Gain(S, A) = Entropy(S)- ¥ |

——Entropy(S.
ve€Values(A ) [S| Py r)

C8 | FI in institut Teknoiogi Bandung a) wwwitbacid (©) @itb1920 XX gh @itbofficial

23
```


</details>


## Halaman PDF 23

### Teks PDF

```text
Example
      Find the ‘best’ Attribute:
      max(Gain(S,Outlook),
         Gain(S,Temperature),
         Gain(S,Humidity),
         Gain(S,Wind))




                                   24
```


<details><summary>OCR halaman (otomatis)</summary>


```text
Day Outlook Temperature Humidity Wind PlayTennis
= X a mM p | e D1 Sunny Hot High Weak No
D2 Sunny Hot High Strong No
D3 Overcast Hot High Weak Yes
Find the ‘best’ Attribute: D4 Rain Mild High Weak Yes
. D5 Rain Cool Normal Weak Yes
max(Gain(S, Outlook), D6 Rain Cool Normal Strong No
Gain(S,Temperatu re), D7 Overcast Cool Normal Strong Yes
. — D& Sunny Mild High Weak No
Gain (S 1 Humid ity) 1 D9 Sunny Cool Normal Weak Yes
; i Dio Rain Mild Normal Weak Yes
Gain(S,Wind)) Dll Sunny Mild Normal Strong Yes
9 9 5 5 D12 Overcast Mild High Strong Yes
Entropy(S) a 14 log2 14 —_ 14 log2 14 = 0.940 D13 Overcast Hot Normal Weak Yes
Dl4_sRain Mild High Strong No
Gain(S, Outlook) = Entropy(S) — ». ~ Entropy (Sy)

vevalue of Outlook

4 5
= 0.940 — = Entropy(Sunny) + qq Entropy (Overcast) + qq Entropy (Rain)]

2 3 4 0 3

2
= 0.940 — eo (=e 5 0925 = 5 092 =) tp os eery 7 loge =F logz D ve & a = =logs=~ = a nF =)

= 0.246

24

© FJ in trssituetexnotogi Bandung GQ) wwwitb.ac.id @itb1920 XK gh @itbofficial
```


</details>


## Halaman PDF 24

### Teks PDF

```text
Example
      Find the ‘best’ Attribute:
      max(Gain(S,Outlook),
         Gain(S,Temperature),
         Gain(S,Humidity),
         Gain(S,Wind))




                                   25
```


<details><summary>OCR halaman (otomatis)</summary>


```text
Day Outlook Temperature Humidity Wind PlayTennis
= X a mM p | e D1 Sunny Hot High Weak No
D2 Sunny Hot High Strong No
D3 Overcast Hot High Weak Yes
Find the ‘best’ Attribute: D4 Rain Mild High Weak Yes
. D5 Rain Cool Normal Weak Yes
max(Gain(S, Outlook), D6 Rain Cool Normal Strong No
Gain(S,Temperatu re), D7 Overcast Cool Normal Strong Yes
. — D& Sunny Mild High Weak No
Gain (S 1 Humid ity) 1 D9 Sunny Cool Normal Weak Yes
A F Dio Rain Mild Normal Weak Yes
Gain(S,Wind)) Dll Sunny Mild Normal Strong Yes
9 9 5 5 D12 Overcast Mild High Strong Yes
Entropy(S) a 14 log2 14 —_ 14 log2 14 = 0.940 D13 Overcast Hot Normal Weak Yes
Dl4_sRain Mild High Strong No
Gain(S, Humidity) = Entropy(S) — ». ~ Entropy(S,)

vevalue of Humidity

7 7
= 0.940 — a Entropy(High) + — Entropy(Normal)|]

14
= 0.940 7 3 ; 3 4 ; 4 a 7 6 ; 6 1 ; 1
= 0. [Ga 6 7 l0g25 — 5 logs 5) rat 7 l0g25— 5 logs WI

= 0.151

25

© FJ in trssituetexnotogi Bandung GQ) wwwitb.ac.id @itb1920 XK gh @itbofficial
```


</details>


## Halaman PDF 25

### Teks PDF

```text
Example
      Find the ‘best’ Attribute:
      max(Gain(S,Outlook),
         Gain(S,Temperature),
         Gain(S,Humidity),
         Gain(S,Wind))




                                           Outlook


                                   Sunny              Rain
                                           Overcast



                                             Yes
                                                             26
```


<details><summary>OCR halaman (otomatis)</summary>


```text
Example

Find the ‘best’ Attribute:

max(Gain(S, Outlook),
Gain(S,Temperature),
Gain(S,Humidity),
Gain(S,Wind))

Gain(S, Outlook) = 0.246
Gain(S, Humidity) = 0.151
Gain(S, Temperature) = 0.029

Gain(S, Wind) = 0.048

Sunn

@

Day Outlook Temperature Humidity Wind PlayTennis
Dl Sunny Hot High Weak No
D2 Sunny Hot High Strong No
D3 Overcast Hot High Weak Yes
D4 Rain Mild High Weak Yes
D5 Rain Cool Normal Weak Yes
D6 Rain Cool Normal Strong No
D7 Overcast Cool Normal Strong Yes
D& Sunny Mild High Weak No
D9 Sunny Cool Normal Weak Yes
D10-~— Rain Mild Normal Weak Yes
Dill Sunny Mild Normal Strong Yes
D12 Overcast Mild High Strong Yes
D13 Overcast Hot Normal Weak Yes
Dl4_sRain Mild High Strong No
Overcast Rain
Yes
26

CBF | fin tistitut teknotogi Bandung ® wowitdac.id @itb1920 XX gh @itbofficial
```


</details>


## Halaman PDF 26

### Teks PDF

```text
Example
      Find the ‘best’ Attribute:
      max(Gain(S,Temperature),
           Gain(S,Humidity),
           Gain(S,Wind))
                                              Outlook


                                    Sunny                Rain
                                              Overcast

                                   Humidity
                                                Yes




                                                            27
```


<details><summary>OCR halaman (otomatis)</summary>


```text
Day Outlook Temperature Humidity Wind PlayTennis

D1 Sunny Hot High Weak No
Exa m p | e D2 Hot High No

Sunny Strong
. . D8 Sunny Mild High Weak. No
Find the ‘best’ Attribute: D9 Sunny Cool Normal _ Weak Yes
max(Gain(S,Temperature), Dil Sunny Mild Normal Strong Yes
Gain(S,Humidity),
Gain(S,Wind))
2 2 3 3
Entropy(S) = —<log2= — ~logz == 0.971
Sunn Overcast Rain

S.
Gain(S, Humidity) = Entropy(S) — >. — Entropy(Sy)

S
vevalue of Humidity

= —_ i _ 2 Yes
0.971 5 Entropy (High) 5 Entropy(Normal)
3. 0 0 3 3 2 2 2 0 0 . am |
= —~f(i(-—— a a a f_e _ Gain(S, Humidity) = 0.971
= 0.971 Gain(S, Temperature) = 0.571
Gain(S, Wind) = 0.020

2/7

© FJ in trssituetexnotogi Bandung GQ) wwwitb.ac.id @itb1920  X gh @itbofficial
```


</details>


## Halaman PDF 27

### Teks PDF

```text
Berdasarkan pseudo-code DTL dari buku Russel AIMA, jawablah pertanyaan berikut ini.

Tersedia training data D 100 instances dengan 3 kelas yaitu c1 (40 instances), c2 (30 instances), c3
(30 instances). D memiliki 6 atribut (atr1..atr6), dan setiap instances hanya dapat diassign satu
kelas. Didapatkan bahwa atribut atr4 paling penting berdasarkan split kriteria information gain, dan
atribut atr4 memiliki 3 value yaitu a1, a2, dan a3. Terdapat 70 instances dengan atr4=a1, 30 instances
dengan atr4=a2, 0 instances dengan atr4=a3. Untuk atr4=a1, 40 instances berlabel c1 dan 30
instances berlabel c2. Untuk atr4=a2, 30 instances sudah berlabel sama yaitu c3.
     a. Hitung Entropy(D): ………………………
     b. Hitung Gain (D,atr4): ………………………..




                                                                                                     28
```


<details><summary>OCR halaman (otomatis)</summary>


```text
faydasarkan pseudo-code DTL dari buku Russel AIMA, jawablah pertanyaan berikut ini.

Tersedia training data D 100 instances dengan 3 kelas yaitu c1 (40 instances), c2 (30 instances), c3
(30 instances). D memiliki 6 atribut (atr1..atr6), dan setiap instances hanya dapat diassign satu
kelas. Didapatkan bahwa atribut atr4 paling penting berdasarkan split kriteria information gain, dan
atribut atr4 memiliki 3 value yaitu a1, a2, dan a3. Terdapat 70 instances dengan atr4=a1, 30 instances
dengan atr4=a2, O instances dengan atr4=a3. Untuk atr4=ai1, 40 instances berlabel c1 dan 30
instances berlabel c2. Untuk atr4=a2, 30 instances sudah berlabel sama yaitu c3.

a. Hitung Entropy(D): ..................:ceeee eee

b. Hitung Gain (D,atr4): ........ eee

28

CBF | fin tistitut teknotogi Bandung @ _ wowitbacia @itb1920  X gh @itbofficial
```


</details>


## Halaman PDF 28

### Teks PDF

```text
Exercise (Class: Activity)
      No   Deadline?   Ada        Malas?   Aktivitas
                       Hangout?

      1    Urgent      ya         Ya       Kumpul-kumpul
      2    Urgent      Tidak      Ya       Belajar

      3    Dekat       ya         Ya       Kumpul-kumpul
      4    Tidak ada   Ya         Tidak    Kumpul-kumpul

      5    Tidak ada   Tidak      Ya       Jalan-jalan ke mall

      6    Tidak ada   Ya         Tidak    Kumpul-kumpul

      7    Dekat       Tidak      Tidak    Belajar

      8    Dekat       Tidak      Ya       Nonton TV

      9    Dekat       Ya         Ya       Kumpul-kumpul
      10   Urgent      Tidak      Tidak    Belajar

                                                                 29
```


<details><summary>OCR halaman (otomatis)</summary>


```text
Exercise (Class: Activity)

No Deadline? Ada Malas? Aktivitas
Hangout?

1 Urgent ya Ya Kumpul-kumpul
2 Urgent Tidak Ya Belajar
3 Dekat ya Ya Kumpul-kumpul
4 Tidak ada Ya Tidak Kumpul-kumpul
5 Tidak ada Tidak Ya Jalan-jalan ke mall
6 Tidak ada Ya Tidak Kumpul-kumpul
7 Dekat Tidak Tidak Belajar
8 Dekat Tidak Ya Nonton TV
9 Dekat Ya Ya Kumpul-kumpul
10 Urgent Tidak Tidak Belajar

BF iin nstitut Teknotogi Bandung @ _ wowitbacia @itb1920 XX gh @itbofficial

29
```


</details>


## Halaman PDF 29

### Teks PDF

```text
Issues in DTL
                            Overfitting
                             training
                               data

                                                     Handling
       Continuous
                                                    attributes
         -valued
                                                   with differing
        attribute
                                                       costs


                Handling                  Alternative
                 missing                  measures for
                attribute                  selecting
                  value                    attributes
                                                                    30
```


<details><summary>OCR halaman (otomatis)</summary>


```text
CSUR

(ie 2,
S| Y

Ne Ss)
ere,

Issues in DTL

CDF) in tstiuetesnotogi Bandung ) wwwitb.acid (©) e@itb1920 X gt Giteotficial

30
```


</details>


## Halaman PDF 30

### Teks PDF

```text
Issues in DTL
                            Overfitting
                             training
                               data

                                                     Handling
       Continuous
                                                    attributes
         -valued
                                                   with differing
        attribute
                                                       costs


                Handling                  Alternative
                 missing                  measures for
                attribute                  selecting
                  value                    attributes
                                                                    31
```


<details><summary>OCR halaman (otomatis)</summary>


```text
SOREN

K
>
Ey 2
3 5
ie ‘x

Issues in DTL

© FJ in testiuetetnotogi Bandung GQ) wwweitb.ac.id @itb1920 X gh @itbotficial

31
```


</details>


## Halaman PDF 31

### Teks PDF

```text
What is Overfit
                         H: Hypothesis space
         A hypothesis: h ∈ H; Alternative hypothesis: h’ ∈ H
       train: training examples; D: entire distribution of data


                      errortrain(h) < errortrain(h’)




                                Overfit




                        errorD(h) > errorD(h’)
                                                                  32
```


<details><summary>OCR halaman (otomatis)</summary>


```text
What is Overfit

[> | INN institut Teknologi Bandung www.itb.ac.id (0) @itb1920 X gf Gitbofficial

32
```


</details>


## Halaman PDF 32

### Teks PDF

```text
       Illustration
D15 (noisy training examples):
Outlook = Sunny;
Temperature = Hot;
Humidity = Normal;
Wind = Strong;
PlayTennis = No




                      Overfitting can happen even training examples is noise-free
                      (when small numbers of examples are associated with leaf
                      Nodes) à decrease accuracy 10 – 25% on most problems          33
```


<details><summary>OCR halaman (otomatis)</summary>


```text
© Illustration

Outlook

Sunny Overcast Rain

Humidity Yes Wind

High Normal

/\ /\

Yes No

C8 | FJ in institut Teknoiogi Bandung a) wwwitbacid (©) @itb1920 XX gh @itbofficial

Strong Weak

\ / \

Day Outlook Temperature Humidity Wind PlayTenni

Yes

D1 Sunny Hot High Weak No
D2 Sunny Hot High Strong = No
D3 Overcast Hot High Weak Yes

D4 Rain Mild High Weak — Yes
D5 Rain Cool Normal Weak Yes
D6 Rain Cool Normal Strong No
D7 Overcast — Cool Normal Strong Yes
D8 Sunny Mild High Weak No
D9 Sunny Cool Normal Weak Yes
D1O Rain Mild Normal Weak Yes
Dil Sunny Mild Normal Strong — Yes

D12 Overcast Mild High Strong = Yes

D13 Overcast Hot Normal Weak Yes

Did Rain Mild High Strong No
33
```


</details>


## Halaman PDF 33

### Teks PDF

```text
Solution Approaches
                                            Pros                Cons
  1. Stop growing the tree                More Direct      Difficulty of
  earlier, before it reaches the                           estimating precisely
  point where it perfectly                                 when to stop growing
  classifies the training data                             the tree


  2. allow the tree to overfit the     More Successfull    Requires more steps
  data, and then post-prune the          in practice       (grow until fit, then
  tree                                                     prune)


                            what criterion is to be used
                            to determine the
                            correct final tree size
                                                                                   34
```


<details><summary>OCR halaman (otomatis)</summary>


```text
© Solution Approaches

Pros Cons

a, Stop growing the tree . More Direct Difficulty of
earlier, before it reaches the estimating precisely
point where it perfectly when to stop growing
classifies the training data the tree

ee e y L 4
>. allow the tree to overfit the More Successfull . Requires more steps
data, and then post-prune the in practice (grow until fit, then
tree prune) y

34
```


</details>


## Halaman PDF 34

> **[INTERPRETASI VISUAL]** Dua pohon dibandingkan. Pre-Pruned Tree berhenti lebih awal pada simpul Humidity dan Windy; Fully Grown Tree meneruskan cabang Humidity ke High/Normal dan Windy ke False/True. Teks bawah menyebut pohon pertama lebih sederhana dan pohon kedua lebih kompleks.

### Teks PDF

```text
35
```


<details><summary>OCR halaman (otomatis)</summary>


```text
Pre-Pruned Tree

Outlook Pre-Pruning

Fully Grown Tree

Outlook

decision to stop growing the tree early.

Sunny Overcast Rainy a 2 Sunny Overcast Rainy

Humidity Windy

Fewer nodes, simpler tree

BF iin nstitut Teknotogi Bandung & www.itb.ac.id

More nodes, complex tree

@itb1920  X gh @itbofficial

3
```


</details>


## Halaman PDF 35

### Teks PDF

```text
Approaches to Determine the Correct Final Tree Size

                                                                 2/3 Training set
  1. Use separate examples distinct from
  training to evaluate the pruning tree
                                                               1/3 Validation set
  2. Use all available data for training, then
  conduct a statistical test to check whether
  expanding (or pruning) a node will produce
  improvement , example: chi square test

  3. Use explicit measure of the complexity for
                                                  Source:
  encoding the training examples and decision     Machine Learning by Tom Mitchell chapter 6.6
  tree à Minimum Description Length Principle


                                                                                                 36
```


<details><summary>OCR halaman (otomatis)</summary>


```text
Approaches to Determine the Correct Final Tree Size

a =
(- 5 2/3 Training set
1. Use separate examples distinct from | L J
training to evaluate the pruning tree 4 )
X d ay 1/3 Validation set
(2. Use all available data for training, then > ’ ‘
conduct a statistical test to check whether
expanding (or pruning) a node will produce
improvement , example: chi square test yy
3- Use explicit measure of the complexity for
encoding the training examples and decision vachin ee Niche chanregell
_tree > Minimum Description Length Principle Z
hup. = argmin Le, (h) + Leo, (Dh) Lc, (h): Length (number of bits) of hypothesis encoding
heH Lc, D|h): Length of data D given hypothesis h encoding

CBF | fin tistitut teknotogi Bandung @ _ wowitbacia @itb1920  X gh @itbofficial
```


</details>


## Halaman PDF 36

### Teks PDF

```text
Reduced Error Pruning
   Consider decision (attribute) node as
   candidates for pruning à assign the
                                                    Grow until fit then prune
   most common classification affiliated
             with that node

             Split data into training and validation set
             Do until further pruning is harmful:
             1. Evaluate impact on validation set of pruning each
                 possible node (plus those below it)
             2. Greedily remove the one (node) that most improves
                 validation set accuracy


                  an effective approach provided a large amount of
                  data is available                                             37
```


<details><summary>OCR halaman (otomatis)</summary>


```text
ESOS
.)
2)
\ y e
irs

uced Error Pruning

4

q

Consider decision (attribute) node as

candidates for pruning > assign the _
most common classification affiliated = Grow until fit then prune
- G)

with that node

a

D Split data into training and validation set

Do until further pruning is harmful:

1. Evaluate impact on validation set of pruning each
possible node (plus those below it)

2. Greedily remove the one (node) that most improves
validation set accuracy

CBF | fin tistitut teknotogi Bandung @ _ wowitbacia @itb1920  X gh @itbofficial

37
```


</details>


## Halaman PDF 37

### Teks PDF

```text
Source: https://techz.vcet.edu.in/2024/05/04/introductory-guide-to-decision-trees-solving-classification-problems/
                                                                                                                     38
```


<details><summary>OCR halaman (otomatis)</summary>


```text
An Unpruned
Decision Tree

A Pruned
Decision Tree

Source: https://techz.vcet.edu.in/2024/05/04/introductory-guide-to-decision-trees-solving-classification-problems/

C8 | FI in institut Teknoiogi Bandung a) wwwitbacid (©) @itb1920 XX gh @itbofficial

38
```


</details>


## Halaman PDF 38

### Teks PDF

```text
Rule Post-Pruning                        Improvement of ID3             Suitable for
                                           Algorithm: C4.5              limited data




  1. Growing the tree from training set, until the training data is fit as well as
  possible and allowing overfitting to occur.
  2. Convert the learned tree into an equivalent set of rules by creating one rule
  for each path from the root node to a leaf node.
  3. Prune (generalize) each rule by removing any preconditions that result in
  improving its estimated accuracy.
  4. Sort the pruned rules by their estimated accuracy, and consider them in this
  sequence when classifying subsequent instances.




                                                                                       39
```


<details><summary>OCR halaman (otomatis)</summary>


```text
Rule Post-Pruning [eames aes)

Algorithm: C4.5

(p

1. Growing the tree from training set, until the training data is fit as well as
possible and allowing overfitting to occur.

2. Convert the learned tree into an equivalent set of rules by creating one rule
for each path from the root node to a leaf node.

3. Prune (generalize) each rule by removing any preconditions that result in
improving its estimated accuracy.

4. Sort the pruned rules by their estimated accuracy, and consider them in this
sequence when classifying subsequent instances.

CBF | fin tistitut teknotogi Bandung @ _ wowitbacia @itb1920  X gh @itbofficial
```


</details>


## Halaman PDF 39

### Teks PDF

```text
Example
  Decision Rules:
  If Outlook = Sunny and Humidity=High
  then No

  Pruning:
  If Outlook = Sunny then No
  OR
  If Humidity=High then No
                                         Why Decision Tree à Decision Rule ?
                                           1. Distinct path ~ distinct rule:
                                           independent pruning
  Increase/ Reduce Accuracy?               2. No distinction between
                                           attribute tests
                                           3. Improves readability
      Over validation set/
       training set (C4.5)                                                     40
```


<details><summary>OCR halaman (otomatis)</summary>


```text
Outlook
© Example
_. Sunny Overcast Rain
Decision Rules:
If Outlook = Sunny and Humidity=High Humidity Yes Wind
then No /\ /\
High Normal Strong Weak

. f ‘ / \

Pruning: No Yes No Yes

If Outlook = Sunny then No
OR
If Humidity=High then No

40

TI institut Teknologi Bandung (GQ) wwwitb.acid (©) @itb1920 XX gh @itbotficial
```


</details>


## Halaman PDF 40

> **[INTERPRETASI VISUAL]** Infografik kiri menjelaskan Reduced-Error Pruning: bangun pohon penuh, sisihkan validation set, coba ganti subtree dengan satu daun, lalu pertahankan pemangkasan jika validation error tidak naik. Infografik kanan menjelaskan Rule Post-Pruning: ubah tiap jalur akar-ke-daun menjadi aturan, hapus kondisi, taksir galat aturan, lalu pertahankan aturan sederhana jika galatnya tidak lebih buruk.

### Teks PDF

```text
Generated using scispace   41
```


<details><summary>OCR halaman (otomatis)</summary>


```text
Decision-Tree Pruning: Reduce Overfitting

Simplify the trained model using validation data, while preserving generalization.

1. Reduced-Error Pruning (REP) 2. Rule Post-Pruning

0 )

Start with a ie Grow the tree, then

fully grown tree cganeett aachiroot= IF Outlook = Sunny
to-leaf path into a rule m= | AND Humidity = High

[ Humicity? } THEN Play = No
High \hila = a
{ Play="No } [ ee Yes } Te No } [ Play = SS fmt Dm = ¥

Simplify each rule Before (original rule) After (simplified rule)
by deleting

Hold out a ol inaaen SenmyAND => Humidity = High > m|

Validationset =) = Humidity = High > No

training tree validation examples gg
+ 3 ] Estimate rule error eis
6. replacing a poate een using training/ = rors

subtree with senait) validation examples a d

one leaf High Normal — [ Ptay= Yes] i covered cases

Keep the prune if Keep the simpler

validation error Vg Waication error rule when its YES ~~ Simpler rule No

does not i cn in batabed estimated error} Keep performs atleast 2>—>

be attcbeaad unchanged? is soieares simplified as well?

cn rule
-
F ae Prunes conditions inside individual rules,
( ) Directly tests generalization on held-out data. oy. then orders/Zelects the rules.
ni Goal: REP: prune subtrees ‘ Rule post-pruning: simplify
@ lower overfitting using a validation set “o extracted rules and compare
- estimated error Generated using scispace 41

Both methods trade a little training fit for a simpler model that may generalize better.
```


</details>


## Halaman PDF 41

### Teks PDF

```text
Issues in DTL
                            Overfitting
                             training
                               data

                                                     Handling
       Continuous
                                                    attributes
         -valued
                                                   with differing
        attribute
                                                       costs


                Handling                  Alternative
                 missing                  measures for
                attribute                  selecting
                  value                    attributes
                                                                    42
```


<details><summary>OCR halaman (otomatis)</summary>


```text
SOREN

K
>
Ey 2
3 5
ie ‘x

Issues in DTL

© FJ in testiuetetnotogi Bandung GQ) wwweitb.ac.id @itb1920 X gh @itbotficial

42
```


</details>


## Halaman PDF 42

### Teks PDF

```text
Discretization
                                                  True: A < c
     Continuous valued attributesà new
      discrete valued (boolean) attribute
                       Ac                         False: A < c



                                                 What is Best Value
                                                  for threshold c?
               Potential optimal breakpoints



         C = (48+60)/2 = 54
                                                Use Information Gain for
         Or
                                               each potential breakproint
         C = (80+90)/2 = 85
                                                                            43
```


<details><summary>OCR halaman (otomatis)</summary>


```text
Discretization

Temperature: 40 48 |60 72 80/ 90
PlayTennis: No No}Yes Yes Yes} No

Potential optimal breakpoints

C = (48+60)/2 = 54
Or
C = (80+90)/2 = 85

© F) Gin wsstuetecnotogitanaune J wwwitdacid (6) @itb1920 X gh @itbotfcial
```


</details>


## Halaman PDF 43

### Teks PDF

```text
Illustration                                         Day     Outlook
                                                                     Temperatur
                                                                         e      Humidity Wind
                                                                                                             Play
                                                                                                            Tennis
                                                     D1                       72                              Yes
                                                     D2                       40                               No
                                                     D3                       90                               No
      1. Sort The Continuous-valued                  D4                       60                              Yes
      attribute                                      D5                       48                               No
                                                     D6                       80                              Yes
Temperatur
    e         40   48     60      72        80     90             2. Identify Adjacent examples that
Play Tennis   No   No     Yes     Yes       Yes    No             differ in their target class


                                                  For C: 54
  3. Candidates: midway between                   Temperature < 54: 2 examples à yes/0, no/2
  corresponding values à C : 54 or C : 85         Temperature ≥ 54: 4 examples à yes/3, no/1
                                                  Gain(S,T54) = Entropi(S) – [(2/6*Entropi(0,2))+(4/6*Entropi(3,1)]

  4. Find the greatest Gain from the              For C: 85
  candidates, and other discrete-valued           Temperature < 85: 5 examples yes/3, no/2
  attributes                                      Temperature ≥ 85: 1 examples yes/0, no/1
                                                  Gain(S,T85) = Entropi(S) – [(5/6*Entropi(3,2))+(1/6*Entropi(0,1)]
                                                                                                                      44
```


<details><summary>OCR halaman (otomatis)</summary>


```text
2 Temperatur Pla
Illustration Day _| Outlook ‘ Humidity! Wind Tennis
D1 72 Yes
D2 40 No
D3 90 No
1. Sort The Continuous-valued D4 60 Yes
attribute D5 48 No
D6 80 Yes
_—__ AO 48 60 72 80 90 2. Identify Adjacent examples that
Play Tennis| No Yes differ in their target class

No |

Se No

3. Candidates: midway between
corresponding values > C: 54 0rC: 85

4. Find the greatest Gain from the
candidates, and other discrete-valued
attributes

Institut Teknologi Bandung

@ wowiitbacia @itb1920 XX gh @itboffcial
```


</details>


## Halaman PDF 44

### Teks PDF

```text
Issues in DTL
                            Overfitting
                             training
                               data

                                                     Handling
       Continuous
                                                    attributes
         -valued
                                                   with differing
        attribute
                                                       costs


                Handling                  Alternative
                 missing                  measures for
                attribute                  selecting
                  value                    attributes
                                                                    45
```


<details><summary>OCR halaman (otomatis)</summary>


```text
SOREN

K
>
Ey 2
3 5
ie ‘x

Issues in DTL

© FJ in testiuetetnotogi Bandung GQ) wwweitb.ac.id @itb1920 X gh @itbotficial

45
```


</details>


## Halaman PDF 45

### Teks PDF

```text
Alternative Strategies                                                                The
                                                                                  probability
         Assign it with the most common value at node n                             Can be
                      among other examples                                         used for
                                                                                  classifying
                                                                                     a new
         Assign it with the most common value at node n                            instance
                    that have classification c(x)                                     with
                                                                                    missing
        Assign probability pi to each possible value vi of A                         value
                          (used in C4.5)


            Gain(S,A) only consider the fraction of training examples with known value
            Gain(S,A) = 10/11 * (Entropy(S) – [Σproportion*entropy_of_known_value])



     v1 = 1, 6 known examples; v2 = 0, 4 known examples, 1 example with missing value of attr A
     pi = 6/10 added to v1 ; p2 = 4/10 added to v2 -> for splitting
                                                                                                  46
```


<details><summary>OCR halaman (otomatis)</summary>


```text
® Alternative Strategies

y

4a

Assign it with the most common value at node n
among other examples

™

faa

Assign it with the most common value at node n
that have classification c(x)

™~

Assign probability p; to each possible value v, of A
(used in C4.5)

{

{

CDF) in tstiuetesnotogi Bandung ) wwwitb.acid (©) e@itb1920 X gt Giteotficial

46
```


</details>


## Halaman PDF 46

### Teks PDF

```text
Missing Value as Separate Value
     Denoted “?” à Null Value                       Not
                                                 Appropriate
             In C4.X
                                                   when:



                              Values are missing due to different reasons

             blood sugar value could be missing when it is very
                             high or very low

            field IsPregnant missing for a male patient should be
             treated differently (no) than for a female patient of
                              age 25 (unknown)


                                                                            47
```


<details><summary>OCR halaman (otomatis)</summary>


```text
© Missing Value as Separate Value

{

“Values are missing due to different reasons

S

blood sugar value could be missing when it is very ) J

high or very low J

field IsPregnant missing for a male patient should be |
treated differently (no) than for a female patient of

age 25 (unknown) )

47
```


</details>


## Halaman PDF 47

### Teks PDF

```text
Issues in DTL
                            Overfitting
                             training
                               data

                                                     Handling
       Continuous
                                                    attributes
         -valued
                                                   with differing
        attribute
                                                       costs


                Handling                  Alternative
                 missing                  measures for
                attribute                  selecting
                  value                    attributes
                                                                    48
```


<details><summary>OCR halaman (otomatis)</summary>


```text
CSR

6
2

Ey 2)

A Ss)

Issues in DTL

© FJ in testiuetetnotogi Bandung GQ) wwweitb.ac.id @itb1920 X gh @itbotficial

48
```


</details>


## Halaman PDF 48

### Teks PDF

```text
      Attribute with many values (C4.5)
                         Gain will always select it à example Date=2021_Jan_31

                             Date will perfectly classify training examples,
                               but very poor predictor for unseen data


                                              GAIN RATIO

Gain Ratio can
reduce bias because
it takes the number
and size of branches
into account when
choosing an attribute.

                                                                                 49
```


<details><summary>OCR halaman (otomatis)</summary>


```text
Gain Ratio can
reduce bias because
it takes the number
and size of branches
into account when

choosing an attribute.

© Attribute with many values (C4.5)

Gain(S, A)
SplitIn formation(S, A)

c [Sif Sil
log
=1 [S| |S|

where 5S; is subset of S for which A has value v;

GainRatio(S, A) =

SplitIn formation(S, A) =

49
```


</details>


## Halaman PDF 49

### Teks PDF

```text
  Illustration                                 Date
                                            2021_Jan_0
                                                         Atr2      Atr3   Class

                                                1        v1                No
                                            2021_Jan_0
                                                2        v1                No
                                            2021_Jan_0
                                                3        v2               Yes
                                            2021_Jan_0
                                                4        v2               Yes
                                            2021_Jan_0
                                                5        v1               Yes
                                            2021_Jan_0
                                                6        v1                No




What if SplitInformation is      Heuristic: Apply GainRatio test
very small or zero (|Si|≈ |S|)    only for Attribute with above
à GainRatio undefined or                   average Gain
        very large
                                                                                  50
```


<details><summary>OCR halaman (otomatis)</summary>


```text
Illustration

What if SplitInformation is

very small or zero (|Si|= |S])

> GainRatio undefined or
very large

@ fiin

Institut Teknologi Bandung

Date Atr2 Atr3 Class

2021_Jan_0O

1 v1 No
2021_Jan_0O

2 v1 No
2021_Jan_0

a v2 Yes
2021_Jan_0

4 v2 Yes
2021_Jan_0

5 v1 Yes
2021_Jan_0

6 v1 No

Heuristic: Apply GainRatio test
only for Attribute with above
average Gain

® www.itb.ac.id

@itb1920  X gh @itbofficial

50
```


</details>


## Halaman PDF 50

### Teks PDF

```text
ID3 vs C4.5
• C4.5 is an extension of ID3 algorithm that uses Gain Ratio (which is a
  normalized Gain) to reduce bias and overfitting.
• C4.5 can handle non-categorical input (continuous variables).


Algorithm of C4.5 to handle non-categorical input:
   •STEP 1: Sort the different values for Attr in the ascending order.
   •STEP 2: For each value p (in the Attr), make a partition scheme
   where the data is partition into two groups: first group with Attr less
   than and equal to p, second group with Attr values greater than p.
   •STEP 3: For each of these partitions scheme in Step 2, compute the
   gain ratio.
   •STEP 4: Choose the partition that maximizes the gain ratio.
```


<details><summary>OCR halaman (otomatis)</summary>


```text
© |D3 vs C4.5

¢ (4.5 is an extension of ID3 algorithm that uses Gain Ratio (which is a
normalized Gain) to reduce bias and overfitting.
¢ C4.5 can handle non-categorical input (continuous variables).

Algorithm of C4.5 to handle non-categorical input:
*STEP 1: Sort the different values for Attr in the ascending order.
eSTEP 2: For each value p (in the Attr), make a partition scheme
where the data is partition into two groups: first group with Attr less
than and equal to p, second group with Attr values greater than p.
eSTEP 3: For each of these partitions scheme in Step 2, compute the
gain ratio.
*STEP 4: Choose the partition that maximizes the gain ratio.
```


</details>


## Halaman PDF 51

### Teks PDF

```text
Issues in DTL
                            Overfitting
                             training
                               data

                                                     Handling
       Continuous
                                                    attributes
         -valued
                                                   with differing
        attribute
                                                       costs


                Handling                  Alternative
                 missing                  measures for
                attribute                  selecting
                  value                    attributes
                                                                    52
```


<details><summary>OCR halaman (otomatis)</summary>


```text
CSR

6
2

Ey 2)

A Ss)

Issues in DTL

© FJ in testiuetetnotogi Bandung GQ) wwweitb.ac.id @itb1920 X gh @itbotficial

52
```


</details>


## Halaman PDF 52

### Teks PDF

```text
Attribute with Different Cost
         Attributes: Temperature, BiopsyResult, Pulse, BloodTestResults


              Have Different Cost (monetary and patient comfort)



           Use low cost attribute where possible, high cost only when
                   required to produce reliable classification


             Cost is considered in calculating Gain of each attribute




                                                                          53
```


<details><summary>OCR halaman (otomatis)</summary>


```text
® Attribute with Different Cost

Attributes: Temperature, BiopsyResult, Pulse, BloodTestResults

Have Different Cost (monetary and patient comfort)

53
```


</details>


## Halaman PDF 53

> **[INTERPRETASI VISUAL]** Dua rumus pendekatan biaya atribut dibandingkan: Tan dan Schlimmer/Tan memakai Gain²(S,A)/Cost(A); Nunez memakai (2^Gain(S,A) − 1)/(Cost(A)+1)^w. Di bawahnya tertulis w∈[0,1] menentukan pentingnya biaya.

**[TRANSKRIPSI MANUAL GAMBAR]**

```text
Tan and Schlimmer (1990) and Tan (1993):
Gain²(S, A) / Cost(A)

Nunez (1988):
(2^Gain(S,A) − 1) / (Cost(A) + 1)^w
Where w∈[0,1] determine importance of cost
```

### Teks PDF

```text
Approaches




             54
```


<details><summary>OCR halaman (otomatis)</summary>


```text
Approaches

C8 | FI in institut Teknoiogi Bandung a) wwwitbacid (©) @itb1920 XX gh @itbofficial

54
```


</details>


## Halaman PDF 54

### Teks PDF

```text
Exercise
    Outlook Temp    Humidity Windy Class
    sunny        75      70 TRUE Play
    sunny        80      90 TRUE Don't Play    1. What is GainRatio for Outlook?
    sunny        85      85 FALSE Don't Play
    sunny        72      95 FALSE Don't Play   2. What are Examples (instances) for
    sunny        69      70 FALSE Play         Outlook = sunny and
    ?            72      90 TRUE Play          what is the weight for instance with outlook=?
    overcast     83      78 FALSE Play         related with outlook=sunny
    overcast     64      65 TRUE Play
    overcast     81      75 FALSE Play         3. Based on the result of question (2), define
                                                  the threshold in “Humidity” discretization,
    rain         71      80 TRUE Don't Play
                                                  and the leaf node for each branch.
    rain         65      70 TRUE Don't Play
    rain         75      80 FALSE Play
    rain         68      80 FALSE Play
    rain         70      96 FALSE Play




                                                                                                55
```


<details><summary>OCR halaman (otomatis)</summary>


```text
© Exercise

sunny

sunny 90} TRUE |Don't Play
sunny 85| FALSE |Don't Play
sunny 95| FALSE |Don't Play
sunny 70} FALSE |Play
? 72 90} TRUE |Play
overcast 83 78| FALSE |Play
overcast 64 65| TRUE Play
overcast 81 75| FALSE |Play
rain 11 80} TRUE |Don't Play
rain 65 70} TRUE |Don't Play
rain 75 80] FALSE |Play
rain 68 80] FALSE |Play
rain 70 96] FALSE |Play
C8 FI in teste Ternotog’ Bandung

1. What is GainRatio for Outlook?

2. What are Examples (instances) for

Outlook = sunny and

what is the weight for instance with outlook=?
related with outlook=sunny

3. Based on the result of question (2), define
the threshold in “Humidity” discretization,
and the leaf node for each branch.

@ _ wowitbacia @itb1920 X gh @itbofficial

55
```


</details>


## Halaman PDF 55

### Teks PDF

```text
07




     THANK YOU
```


<details><summary>OCR halaman (otomatis)</summary>


```text
THANK YOU

CBF | fin tistitut teknotogi Bandung ® wowitdac.id @itb1920 XX gh @itbofficial
```


</details>
