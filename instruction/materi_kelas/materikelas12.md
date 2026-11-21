# Materi Kelas 12

Sumber: `1794394765946_1_2026_IF3070_Materi12-Perceptron-ANN.pdf`  
Jumlah halaman PDF: 44

Teks PDF di bawah disalin dari lapisan teks. Blok OCR adalah keluaran otomatis dari gambar halaman; ejaan, urutan, dan rumus di dalamnya perlu dicek terhadap PDF. Catatan visual yang ditambahkan akan selalu diberi penanda **[INTERPRETASI VISUAL]**.


## Halaman PDF 1

### Teks PDF

```text
IF3070 Dasar Inteligensi Artifisial
Institut Teknologi Bandung

Perceptron & Artificial Neural Network (ANN)
Semester I TA 2026/2027
```


<details><summary>OCR halaman (otomatis)</summary>


```text
IF3070 Dasar Inteligensi Artifisial

Institut Teknologi Bandung

Perceptron & Artificial Neural Network (ANN)

Semester | TA 2026/2027

CF ith were terror torte GF wwwitdacie @nvi920 XX dt @itbomciat
```


</details>


## Halaman PDF 2

### Teks PDF

```text
                              Outline
• Review:
       • Learning Agent
       • Introduction to Data Science
       • CRISP-DM
       • Data Understanding
       • Data Preparation
       • K-Nearest Neighbor
       • Naive Bayes
       • Decision Tree Learning
       • Linear Regression
       • Logistic Regression
• Perceptron
• Artificial Neural Network (ANN)
                                        2
```


<details><summary>OCR halaman (otomatis)</summary>


```text
Outline

° Review:

Learning Agent
Introduction to Data Science
CRISP-DM

Data Understanding
Data Preparation
K-Nearest Neighbor
Naive Bayes

Decision Tree Learning
Linear Regression
Logistic Regression

°¢ Perceptron
° Artificial Neural Network (ANN)

@itdomcia!
```


</details>


## Halaman PDF 3

### Teks PDF

```text
Perceptron




             3
```


<details><summary>OCR halaman (otomatis)</summary>


```text
Perceptron

EF itn worreterncen tontens GD wowiti.acie G) ends920 XX gh eiidomeiat
```


</details>


## Halaman PDF 4

### Teks PDF

```text
What is Perceptron ?


                                                                                    𝑦 = 𝒔𝒊𝒈𝒏(𝒘𝑻𝒙) = s𝑖𝑔𝑛(𝑤0. 1 + 𝑤1𝑥1 + ⋯ + 𝑤𝑑 𝑥𝑑 )
                    Linear model
           Linearly separable dataset                                                       +1
                                                                                                      w0
                                                                                      x1
                                                                                            w1                                        sign        Discrete-value
     Simple Neural Network                                                                     w2
                                                                                                              ∑=wT.x function                     {-1, +1}
                                                                                      x2
                 ANN based on a unit
                                                                                                                                                        𝑻
                                                                                      ...                                                    𝑦 = +1 𝑖𝑓 𝒘 𝒙 > 𝟎
                                                                                                 wd
                                                                                                                                                 −1 𝑜𝑡ℎ𝑒𝑟𝑤𝑖𝑠𝑒
   Learning output: w  d+1
   Hypothesis space H={w | wd+1}                                                    xd

Mitchell, T. (1997). Machine learnig. McGraw-Hill. Chapter 4.4
Flach, P. (2012). Mac hine learning: the art and sc ience of algorithms that make sense of data. Cambridge University Press. Chapter 7.2.



                                                                                                                                                                   4
```


<details><summary>OCR halaman (otomatis)</summary>


```text
What is Perceptron ?

¥ =sign(w'x) = sign(wo.1 + wx, +++ + WaXxa)

Linear model
Linearly separable dataset

+1

Discrete-value

Simple Neural Network (1, +1}

ANN based on a unit

> —J+1 ifw'x>0
—1 otherwise

Learning output: w € Ro!
Hypothesis space H={w | weR**!} xj

E x<
De

Mitchell, T. (1997). Machine leamig. McGraw-Hill. Chapter 4.4
Flach, P. (2012). Machine leaming: the art and science of algorithms that make sense of data. Cambridge University Press. Chapter 7.2.

DF fit weeeterrciee tasters GB wrmitoacie @ e@nviv20 XK _t @itdomciat
```


</details>


## Halaman PDF 5

### Teks PDF

```text
Perceptron

  Represent hyperplane decision surface in the n-dimensional space of
  instances




  Sumber: http://images.slideplayer.com/5/1579281/slides/slide_32.jpg


                                                                        5
```


<details><summary>OCR halaman (otomatis)</summary>


```text
© Perceptron

Represent hyperplane decision surface in the n-dimensional space of

instanges . erolanein Risa line A hyperplanein al isa plan

A hyperplanein R"is an n-1 dimensional subspace
Sumber: http://images. slideplayer.com/5/1579281/slides/slide_32 jpg

OF fit weeeterreen torte GB wrrmitoacie G @nviv20 XK _t @itbomciat
```


</details>


## Halaman PDF 6

### Teks PDF

```text
Perceptron easily represent m-of-n
function
         m-of-n functions: functions where at least m of the n inputs must be true


                 m-of-n function                                                   Perceptron for m-of-n function
                                                                                           1. set all input weights to the same
                            AND m=n
                                                                                              value (e.g., 0.5)
                            OR m=1
                                                                                           2. setting the threshold w0.
                      Perceptron:
                                                                                                                    Show that perceptron with
                       Example                                                                                      w0=-0.8 and w1=w2=0.5,
               AND: sign(x1+x2-1)                                                                                   represent AND function.
               OR: sign(2x1+2x2-1)
Mitchell, T. (1997). Machine learnig. McGraw-Hill. Chapter 4.4
https://medium.com/@stanleydukor/neural-representation-of-and-or-not-xor-and-xnor-logic-gates-perceptron-algorithm-b0275375fea1



                                                                                                                                                6
```


<details><summary>OCR halaman (otomatis)</summary>


```text
© Perceptron easily represent m-of-n
function

m-of-n functions: functions where at least m of the n inputs must be true

set all input weights to the same

value (e.g., 0.5)
setting the threshold Wo.

Show that perceptron with
w0=-0.8 and w1=w2=0.5,
represent AND function.

AND: sign(x1+x2-1
OR ci

Mitchell, T. (1997). Machine leamig. McGraw-Hill. Chapter 4.4
https ://medium.com/@stanleydukor/neural-representation-of-and-or-not-xor-and-xnor-logic-gates-perceptron-algorithm-b0275375feat1
```


</details>


## Halaman PDF 7

### Teks PDF

```text
Perceptron: Example 1
•   Suppose we have 2 input attributes x1 and x2  {-1,1}, and 1
    output attribute o  {-1,1}. Given following training set:

                                           x1     x2        o(x1,x2)

                                           1      1         +1

                                           1      -1        -1

                                           -1     1         -1

                                           -1     -1        -1


         Then the learning problem is to find weight w1 and w2 and threshold (or bias) value such that
         the computed output of our network (which is given by the linear threshold function) is equal to
         the desired output for all examples.




                                                                                                            7
```


<details><summary>OCR halaman (otomatis)</summary>


```text
© Perceptron: Example 1

- Suppose we have 2 input attributes x1 and x2 « {-1,1}, and 1
output attribute o © {-1,1}. Given following training set:

po Pes Toei

1 4 +1
i |= 1
1 4 1
1 le 1

Then the learning problem is to find weight w1 and w2 and threshold (or bias) value such that
the computed output of our network (which is given by the linear threshold function) is equal to
the desired output for all examples.

OF fit weeeterreen torte GB wrrmitoacie G @nviv20 XK _t @itbomciat
```


</details>


## Halaman PDF 8

### Teks PDF

```text
AND Perceptron: m-of-n function

          X0=1                                            AND: m=n=2
                   -0.8
     x1                                                   x0        x1        x2         sign
            0.5
                                                          1         1         1    0.2    +1
                           |
                          sign                            1         1         -1   -0.8   -1

             0.5                                          1         -1        1    -0.8   -1
     x2
                                                          1         -1        -1   -1.8   -1

                       1, 𝑛𝑒𝑡 > 0
          𝑠𝑖𝑔𝑛 𝑛𝑒𝑡 = {
                      −1, 𝑜𝑡ℎ𝑒𝑟𝑤𝑖𝑠𝑒

     set all input weights to the same value and then setting the threshold wo.
     e.g., w1=w2=0.5 → w0=-0.8


                                                                                                 8
```


<details><summary>OCR halaman (otomatis)</summary>


```text
© AND Perceptron: m-of-n function

X0=1 AND: m=n=2
po pt fe fz sion
1 1 1 0.2 +1
1 1 A 08 -1
1 = 1 4 | =
1 A -1 18 -1

={ 1,net > 0
~ '_1 otherwise

sign(net)

set all input weights to the same value and then setting the threshold wo.
e.g., W1=w2=0.5 > w0=-0.8

0 EF ith Wworreternicn tances GB wwmitd.scie G) @ndie20 XK gh eitdociat
```


</details>


## Halaman PDF 9

### Teks PDF

```text
AND Perceptron
   x0      x1          x2               sign             0.5x1+0.5x2=0.8

   1       1           1          0.2    +1

   1       1           -1         -0.8   -1

   1       -1          1          -0.8   -1

   1       -1          -1         -1.8   -1
                                                     x1
        X0=1

                -0.8
   x1
         0.5
                                                                      x2
                            |
                           sign
          0.5
                                                              1, 0.5𝑥1 + 0.5𝑥2 > 0.8
                                                o(x1, x2) = {
   x2                                                        −1, 𝑜𝑡ℎ𝑒𝑟𝑤𝑖𝑠𝑒

                                                                                       9
```


<details><summary>OCR halaman (otomatis)</summary>


```text
® AND Perceptron

xo xt [xz fz | sion | 0.5x1+0.5x2=0.8
1 1 1 02 +1 T
1 1 <i 08 A “Ss
1 4 1 78 4 O —
1 4 4 48 | :

x1 ON
X0=1

O O

1, 0.5x1 + 0.5x2 > 0.8

0(x1, x2) = {_y otherwise

8 EF ity Wvrrecternsier tanters GD wwmito.acie G) @nns920 XK gh eitdotmciat
```


</details>


## Halaman PDF 10

### Teks PDF

```text
Perceptron: Learning algorithm

                Perceptron Training Rule
     proven to be converged if training data is linearly separable
     and learning rate (𝜂) sufficiently small.


                 Batch Gradient Descent


             Stochastic Gradient Descent



                                                                     10
```


<details><summary>OCR halaman (otomatis)</summary>


```text
© Perceptron: Learning algorithm

proven to be converged if training data is linearly separable
and learning rate (7) sufficiently small.

Batch Gradient Descent

CDF ith wrreternren torte GB wwwitdacse @ enviv20 XK dt eitdomcias

10
```


</details>


## Halaman PDF 11

### Teks PDF

```text
Perceptron Training rule
input: Training data D={<x 1,y 1>…<xn,y n>}; learning rate 𝜂

      Initialize randomly for w                                        D: {<[1,0,1],-1>,<[0,-1,-1],+1>}; 𝜂 =0.1

      repeat                                                           w=[0,0,0,0] #w0=0; w1=0; w2=0, w3=0

         E0                                                           epoch 1: E=0

         For each example <xi,yi>:

               oi=prediction for xi using the current coefficients w      <[1,0,1],-1>:
                                                                          oi=sign(0)=-1 → do nothing
               If oi==yi then do nothing                                  <[0,-1,-1],+1>:
               else #update                                               oi=sign(0)=-1
                           wjwj+wj dgn wj = (yi-oi)xij                w0=0+0.1(1-(-1))*1=0.2
                                                                          w1=0+0.1(1-(-1))*0=0
               EE+(yi-oi)2/2 #update error                               w2=0+0.1(1-(-1))*-1= -0.2
                                                                          w3=0+0.1(1-(-1))*-1= -0.2
                                                                          E=2
      Until E==0

      Return w                                                         epoch 2: E=0




                                                                                                                  11
```


<details><summary>OCR halaman (otomatis)</summary>


```text
Perceptron Training rule

= input: Training data D={<x,,y1>...<X,,Y,>}; learning rate

D: {<[1,0,1],-1>,<[0,-1,-1],+1>}; 9=0.1
w=[0,0,0,0] #w0=0; w1=0; w2=0, w3=0

epoch 1: E=0

<[1,0,1],-Le:
oi=sign(0)=-1 > do nothing

do nothing €[Op-Le-1), HS:
oi=sign (0)=-1
dgn Aw, = 7 (yi-oi1) x;, w0=0+0.1(1-(-1)) *1=0.2

wl=0+0.1(1-(-1)) *0=0
w2=0+0.1(1-(-1)) *-1l= -0.2
w3=0+0..14ta=a=—))*-1= -0.2
E=2

Return " | epoch 2: E=0

fet

OF fit weeeterreen torte GB wrrmitoacie G @nviv20 XK _t @itbomciat
```


</details>


## Halaman PDF 12

### Teks PDF

```text
Perceptron: Example
•   Suppose we have 3 input attributes x1, x2, x3  , and 1 output
    attribute o  {-1,1}. Given following training set:


                                          x1   x2     x3   o(x1,x2)

                                          1    0      1    -1

                                          0    -1     -1   +1

                                          -1   -0.5   -1   +1


      Then the learning problem is to find weight w0, w1, w2, w3 values such
      that the computed output of our network (which is given by the sign
      function) is equal to the desired output for all examples.


                                                                               12
```


<details><summary>OCR halaman (otomatis)</summary>


```text
© Perceptron: Example

* Suppose we have 3 input attributes x1, x2, x3 © 8, and 1 output
attribute o <€ {-1,1}. Given following training set:

1 0 1 -1
0) -1 of +1
-1 -0.5 -1 +1
Then the learning problem is to find weight wO, w1, w2, w3 values such

that the computed output of our network (which is given by the sign
function) is equal to the desired output for all examples.

ee

CDF ith wrreternren torte GB wwwitdacse @ enviv20 XK dt eitbomciar
```


</details>


## Halaman PDF 13

> **[INTERPRETASI VISUAL]** Lembar kerja menampilkan perceptron learning rate 0.1 dan fungsi aktivasi sign. Pada iterasi 1 masih ada baris dengan Err 2; pada iterasi 2 nilai Err terakhir menjadi 0 dan ditandai terminate.

### Teks PDF

```text
Perceptron Learning Rule




                           terminate




                                   13
```


<details><summary>OCR halaman (otomatis)</summary>


```text
Perceptron Learning Rule

‘learning rate 01 | |

|Fungsi aktivasi sign

| Perhitungan error sepanjang iterasi

xi|x2 |x3/Target|wO wl jw2 w3 |sigma|sign|Err

a[1[ oj 1 -1} 0.00} 0.00] 0.00] 0.00] 0.00} -1] oO

/8| o| -1/-1] 1] 0.00] 0.00] 0.00] 0.00] 0.00] -1| 2

|| -1] -0.5] -1 1|[0.20/ 0.00] -0.20/-0.20/ oSoy 1] 2

| [xL[x2__ [x3 |Target |wO wil |w2 w3 |sigma|sign|Err

‘w{ 1} Oo} 1 -1} 0.20} 0.00] -0.20]-0.20] 0.00} -1] 0

8| of -1[-1] 1] 0.20] 0.00] -0.20|-0.20] 0.60] 1] 0

2[-1[-05[-1] 1] 0.20] 0.00] -0.20]-0.20] 050 4 terminate
0.20] 0.00] -0.20]-0.20

0B Fin wnrcrnsesinacnne GB wwwitnacie G envsv20 XK et endemes
```


</details>


## Halaman PDF 14

### Teks PDF

```text
Summary


   Perceptron as          Perceptron easily
  linear classifier   represent m-of-n function
   Hyperplane            Perceptron Training
 decision surface               Rule




                                                  14
```


<details><summary>OCR halaman (otomatis)</summary>


```text
® Summary

Perceptron as Perceptron easily
linear classifier represent m-of-n function

Hyperplane Perceptron Training
decision surface Rule

DF fit weeeterrciee tasters GB wrmitoacie @ e@nviv20 XK _t @itdomciat

14
```


</details>


## Halaman PDF 15

### Teks PDF

```text
References
•   Flach, P. (2012). Machine learning: the art and science of
    algorithms that make sense of data. Cambridge University
    Press. Chapter 7.2.
•   Mitchell, T. (1997). Machine learnig. McGraw-Hill. Chapter 4.




                                                                    15
```


<details><summary>OCR halaman (otomatis)</summary>


```text
© References

Flach, P. (2012). Machine learning: the art and science of
algorithms that make sense of data. Cambridge University
Press. Chapter 7.2.

Mitchell, T. (1997). Machine learnig. McGraw-Hill. Chapter 4.

15

CDF ith wrreternren torte GB wwwitdacse @ enviv20 XK dt eitbomciar
```


</details>


## Halaman PDF 16

### Teks PDF

```text
Latihan Perceptron Training Rule
Learning Rate = 0.1, initial bobot semua = 0, error dengan half
squared error, batas konvergen Error = 0

         Atribut1 Atribut2   Atribut3   Atribut4   Kelas
         1         -1        -1         -1         1
         1         1         -1         -1         1
         -1        1         -1         1          -1
         1         1         -1         1          1




                                                                  16
```


<details><summary>OCR halaman (otomatis)</summary>


```text
©) Latihan Perceptron Training Rule

Learning Rate = 0.1, initial bobot semua = 0, error dengan half
squared error, batas konvergen Error = 0

Atribut] |Atribut2 Atribut3 /Atribut4 (Kelas
1 -1 -1 -1 1

1 1 -1 -1 1

-1 1 -1 1 -1

1 1 -1 1 1

CDF ith wrereterncre tortene GB wwwitorcie G) @nv1920 YX gf @itbometas
```


</details>


## Halaman PDF 17

> **[INTERPRETASI VISUAL]** Slide ini adalah pembatas bagian ANN: Feed Forward Neural Network (FFNN); selain judul ada ilustrasi maskot dengan laptop, tanpa diagram konsep tambahan.

### Teks PDF

```text
ANN: Feed Forward Neural Network
(FFNN)




                                   17
```


<details><summary>OCR halaman (otomatis)</summary>


```text
ANN: Feed Forward Neural Network
(FFNN) =

0 EF fith Wworreeternien tantere GB wwmito.scie G) @ndie20 XK gt eitdomciat
```


</details>


## Halaman PDF 18

### Teks PDF

```text
     Artificial neural network: Why

      ANN apps to diverse sectors,                                                              Rapid increase in ANN architectural
           and perform well                                                                     innovations and application




Abiodun, O. I., Jantan, A., Omolara, A. E., Dada, K. V., Mohamed, N. A., & Arshad, H. (2018).   Sakib, S., Ashrafi, Z., Siddique, M., & Bakr, A. (2019). Implementation of Fruits Recognition
State-of-the-art in artificial neural network applications: A survey. Heliyon, 4(11), e00938.   Classifier using Convolutional Neural Network Algorithm for Observation of Accuracies for
                                                                                                Various Hidden Layers. https://arxiv.org/ftp/arxiv/papers/1904/1904.00783.pdf


                                                                                                                                                                                                18
```


<details><summary>OCR halaman (otomatis)</summary>


```text
) Artificial neural network: Why

ANNs applications to diverse sector

60
50
40
30
20
| at !
ma | Fa | a | FPP |r) ee At || eT ll

S ££ & £ SF ££ SF FS a ge oe SF & w

S FFF SF EF FE S & CEE EE SF FX

@ FF SF RS oS SF we KS

“ $ s we
ys s € s
s Comvahtion= Rell? MaxPooing Convoltion+ Rell! Max Pooling
@ Prediction Pattern recognition ™ Classification Fines Ra - Degen

Abiodun, O. |., Jantan, A., Omolara, A. E., Dada, K. V., Mohamed, N. A., & Arshad, H. (2018). Sakib, S., Ashrafi, Z., Siddique, M., & Bakr, A. (2019). Implementation of Fruits Recognition
State-of-the-art in artificial neural network applications: A survey. Heliyon, 4(11), e00938. Classifier using Convolutional Neural Network Algorithm for Observation of Accuracies for

Various Hidden Layers. https://arxiv.org/ftp/arxiv/papers/1904/1904.00783.pdf

18

OF fit weeeterreen torte GB wrrmitoacie G @nviv20 XK _t @itbomciat
```


</details>


## Halaman PDF 19

### Teks PDF

```text
Artificial neural network: What

                                                                 +1
  Perceptron (incl. Adaline)                                               w0
                                                                                                  Activation
  single unit/neuron, estimation function (hypothesis)                                    ∑=w.x                output
                                                           x1                                      function
                                                                      w1


                                                           x2         w2           H
            Artificial Neural                                                   hidden       o1
  many computational units become intelligent only         ...
                                                                           wd    layer      ...
  via their interactions with each other is inspired by
                 the brain (neuroscience)

                                                           xd
                                                                                            om

                   Network                                Input layer
                                                                                 Hidden   Output layer has
    composing together many different functions           has d input
                                                                                  layer     m neurons
                                                           neurons


                                                                                                                 19
```


<details><summary>OCR halaman (otomatis)</summary>


```text
© Artificial neural network: What

Perceptron (incl. Adaline)

many computational units become intelligent only
via their interactions with each other is inspired by
the brain (neuroscience)

nig meat Hidden Output layer has
neurons layer m neurons

Ae

CDF ith wrrreterncren torte § GF wwwitdrcse G) enviv20 XK gh @itdomcias
```


</details>


## Halaman PDF 20

### Teks PDF

```text
     Artificial Neural Network: Architecture
                                  depth

                 x0=+1   n10=+     n..0=+1     nh0=+
           x1            1                     1
                            n11     ...       nh1       o1
   width   x2
                          ...       ...      ...       ...
           ...
                           n1j      ...       nhk       om
           xi

                                H hidden layer
Input layer has i                                         Output layer
                           Hidden layer 1: j neurons
 input neurons                                           has m neurons
                           Hidden layer h: k neurons
                                                                         20
```


<details><summary>OCR halaman (otomatis)</summary>


```text
Artificial Neural Network: Architecture

depth

H hidden layer
Hidden layer 1: j neurons
Hidden layer h: k neurons

Input layer has i

input neurons

Output layer
atctomaamalsielcelats
20

CO EF fit weeterren tortre GD wrmitoacie @nb1920 XK gh @itdotciat
```


</details>


## Halaman PDF 21

### Teks PDF

```text
  Artificial Neural Network

                 Explicit style           Compact style

                                    om       𝑦 (𝑚)        Output
           o1           ...                                layer
                                          whhy

           nh1          ...         nhk           ℎℎ
nh0=+1                                            (k)
                                           Wh…hh             H
           ...          ...         ...                   hidden   depth
 n..0=+1                                          …
                                           wh1h…           layer

 n10=+1    n11          ...         n1j       ℎ1 (𝑗)
                                           wxh1           Input
                   x2                                     layer
    x0=+1 x1                  ...   xi            𝑥 (i)
                                                                           21
```


<details><summary>OCR halaman (otomatis)</summary>


```text
© Artificial Neural Network

Explicit style Compact style

x (i)

CO EF fit weeterren tortre GD wrmitoacie enni920 XK ¢h @itbomciat

ee (U9) 0 ee

21
```


</details>


## Halaman PDF 22

### Teks PDF

```text
     Artificial Neural Network: Inference

                                                                             +1
                                                                                       w0
                                                                      x1
                                                                              w1                 Activatio

                                                                              w2
                                                                                            ∑=w.x n          output
                                                                      x2                         function

                                                                       ...
                                                                                  wn


                                                                      xn


                                                                       Input x=(1, x1, x2, …, xn)
                                                                       Model w=(w0, w1, w2, …, wn)
 Forward propagation: Information flows through the function being     ∑=w.x=w0+w1x1+..+wnxn
 evaluated from vector x, through intermediate computations used to
 define f, and finally to the output y.                                Output = f (∑)
https://kookycoder.com/blog/deep -learning-and-its-functioning/
                                                                                                                 22
```


<details><summary>OCR halaman (otomatis)</summary>


```text
HIDDEN LAYERS

= _ @—@

Ss

a

Forward propagation: Information flows through the function being
evaluated from vector x, through intermediate computations used to

define f, and finally to the output y.

Artificial Neural Network: Inference

+1

= Activatio

y =w.x n output
XQ function
Xn

Input x=(1, x4, Xo, .--, Xp)
Model w=(Wo, Wi, Wa, ---; Wr)
> =W.X=Wotw1X7+..+W,X,

Output = f (>)
02D.

https :/k ooky coder.com/blog/deep-leaming-and-its-functioning/ gy jy sre fernou tortor ® womitdarcse @nv1920 XK gt @itbotciat
```


</details>


## Halaman PDF 23

### Teks PDF

```text
  Example: XOR (Sigmoid Model)
    𝛔 (net): 1/(1+e-net)

       𝑦 (1)                                         h1= 𝛔(-10+20*x1+20*x2)
                                                     h2= 𝛔(30-20*x1-20*x2)
                                                     y = 𝛔(-30+20*h1+20*h2)
 why


       ℎ (2)                                         x1    x2    y

                                                     0     0     0
 wxh                                                 0     1     1

                                                     1     0     1

       𝑥 (2)                                         1     1     0



Target function classifies two input into predefined classes {0, 1}.
                                                                              23
```


<details><summary>OCR halaman (otomatis)</summary>


```text
© Example: XOR (Sigmoid Model)

o (net): 1/(1+e"**)

h1= o(-10+20*x1+20*x2)
h2= 0(30-20*x1-20*x2)
y = 0(-30+20*h1+20*h2)

Why -30 20 20

i
+1
20

0

Wyn Sal 0

Zs 30 -20 ;

1

20 =
x (2) +1 xl x2

3 —en = Re
°o ks -

Target function classifies two input into predefined classes {0, 1}.

OF fit weeeterreen torte GB wrrmitoacie G @nviv20 XK _t @itbomciat

JES
```


</details>


## Halaman PDF 24

> **[INTERPRETASI VISUAL]** Jaringan XOR memiliki dua input x1/x2, dua neuron tersembunyi h1/h2, dan keluaran y. Persamaan pada slide: h1=σ(-10+20*x1+20*x2), h2=σ(30-20*x1-20*x2), y=σ(-30+20*h1+20*h2). Tabel memperlihatkan keluaran 0,1,1,0 untuk input 00,01,10,11.

### Teks PDF

```text
FFNN: XOR (Sigmoid Model)
               h1= 𝛔(-10+20*x1+20*x2)
               h2= 𝛔(30-20*x1-20*x2)
               y = 𝛔(-30+20*h1+20*h2)




               𝛔 (net): 1/(1+e-net)

                                        24
```


<details><summary>OCR halaman (otomatis)</summary>


```text
@ FFNN: XOR (Sigmoid Model)

h1= o(-10+20*x1+20*x2)

h2= 6(30-20*x1-20*x2)
y = o(-30+20*h1+20*h2)

xO |x1/x2| f | ht hi | yh2| h2 | Sy y
110/0/0f -10 lo.00 [ 30 |1.00 [-10.00 |0.00
4101/11/11 10 [1.00 1 10 |1.00 [10.00 |1.00
414/011 10 [1.00 [ 10 |1.00 [10.00 |1.00
114/4]0f7 30 [1.00 [ -10 [0.00 [-10.00 |0.00

o (net): 1/(1+e**)

24

CO EF fit weeterren tortre GD wrmitoacie @rv1920 YK ft @itbomciar
```


</details>


## Halaman PDF 25

### Teks PDF

```text
             FFNN: XOR (RELU & LINEAR)
           Compact style
                                                                                            Input vector x:
                                                                                            f(x;wxh,c,why,b)= whyT.(max{0,wxhT.x+c})+b
                 𝑦 (1)
                                                                         0                  Input mini-batch X:
                                   𝒘𝒉𝒚 =
                                               1               y=hwhy+b= 1                  f(X;wxh,c,why,b)=(max{0, Xwxh+c})why+b
                                                                         1
                                              −2
           why                    b=0                                    0

                                                                                                                        ReLU(z)=max{0,z}
                 ℎ (2)
                                                                                                            𝟎   𝟎
                                            𝟏 𝟏                      0          h=ReLU(Xwxh+c)=max{0,XW+c}= 1   0
                                 𝒘𝒙𝒉 =                        𝒄=                                            1   0
          wxh                               𝟏 𝟏                      −1
                                                                                                            2   1

                                      0        0
                  𝑥 (2)            𝑿= 0
                                      1
                                               1
                                               0                                h1= ReLU(0+x1+x2)
                                      1        1
                                                                                h2= ReLU(-1+x1+x2)
                                                                                y = (0+h1-2*h2)                                          25
Goodfellow, I., Bengio, Y., & Courville, A. (2016). Deep learning. MIT press.
```


<details><summary>OCR halaman (otomatis)</summary>


```text
@® FFNN: XOR (RELU & LINEAR)

Compact style
Input vector x:
£ (7 Wyn Cy Whyr ) = Why". (max{0,Wyy’.xtc}) +b

0 Input mini-batch X:
Why = 1 y=hwyy+b= i £ (XFWyhr C, Why, ©) = (max{0, XWy,tC}) Whytb
—2 ia
Why b=0 0
ReLU(z)=max{0, z}
0 0 a
1 0 Fi
Wyn = 19 1 é= [ 0 | h=ReLU(Xw,,,+-c)=max{0,XW+c}= 10 i
Wxh 1p ad z 1 :

h1= ReLU(0+x1+x2)

0
‘ h2= ReLU(-1+x1+x2)
y = (0+h1-2*h2) 25

Goodfellow, |., Bengio, Y., & Courville, A. (2016). Deep learning. MIT press.
CO EF fit weeterren tortre GD wrmitoacie @rv1920 YK ft @itbomciar
```


</details>


## Halaman PDF 26

### Teks PDF

```text
           Forward Propagation
                                                                                                               𝑦 (𝑚)
                                                                                                            whhy
                                                                                                                    ℎℎ
                                                                                                                    (k)
                                                                                                            Wh…hh

                                                                                                                    …
                                                                                f(a): activation function   wh1h…
                                                                                𝐿 𝑦, 𝑦 : loss function
                                                                                : all parameters (W,b)        ℎ1 (𝑗)
                                                                                (): regularizer            wxh1

                                                                                                                    𝑥 (i)


Goodfellow, I., Bengio, Y., & Courville, A. (2016). Deep learning. MIT press.



                                                                                                                            26
```


<details><summary>OCR halaman (otomatis)</summary>


```text
® Forward Propagation

Require: Network depth, 1

Require: Wie {1,...,l}, the weight matrices of the model
Require: BO i € {1,...,/}, the bias parameters of the model

Require: x, the input to process
Require: u. the target output
hO =a
for k= 1,...,6a0
al’) = b) 4 wh ple-))
h\ = f(a’)
end for
g = hh)
J = Ly, y) + AX(9)

Goodfellow, |., Bengio, Y., & Courville, A. (2016). Deep learning. MIT press.

f(a): activation function
L(J, y): loss function

0: all parameters (W,b)
QQ(0): regularizer

CO EF fit weeterren tortre GD wrmitoacie @nb1920 XK gh @itdotciat

26
```


</details>


## Halaman PDF 27

### Teks PDF

```text
Forward Propagation: Example
(from http://mattmazur.com/2015/03/17/a-step-by-step-backpropagation-example/)




                                                                                       Compact style: sigmoid model

                                                                                       𝑜 (2)

                                                                                                      𝟎. 𝟒𝟎 𝟎. 𝟒𝟓             0.60
                                                                                               𝑾𝟐𝑻=                  𝒃(𝟐) =
                                                                                 who                  𝟎. 𝟓𝟎 𝟎. 𝟓𝟓             0.60



                                                                                       ℎ (2)
                                                                                                       𝟎. 𝟏𝟓 𝟎. 𝟐𝟎            0.35
                                                                                               𝑾𝟏𝑻=                  𝒃(𝟏) =
                                                                                                       𝟎. 𝟐𝟓 𝟎. 𝟑𝟎            0.35
                                                                                 wih
                                                                                                      0.05
                                                                                                𝒙=
                                                                                         𝑖            0.10
                                                                                        (2)

                                                                                                                                     27
```


<details><summary>OCR halaman (otomatis)</summary>


```text
© Forward Propagation: Example

(from http://mattmazur.com/2015/03/17/a-step-by-step-backpropagation-example/)

(2)T _ 0.40
Ww 0.50

yr _ [0.15
wor = [ied
Win
b1.35 b2 .60 ve
1 4 _ 0.
rf x= load
(2)

OF fit weeeterreen torte GB wrrmitoacie G @nviv20 XK _t @itbomciat

Compact style: sigmoid model

veel PO =[585

0.2 a) — 0.35
0.3 b= lage

oe
```


</details>


## Halaman PDF 28

### Teks PDF

```text
             Forward Propagation
           Compact style
                                                                                         k          a               h

               𝑜 (2)                                                                     0    -                   0.05
                                                                                                                  0.10
                                           𝟎. 𝟒𝟎 𝟎. 𝟒𝟓                            0.60
                             𝑾𝟐𝑻=                                        𝒃(𝟐) =          1        0.3775         0.5933
         who                               𝟎. 𝟓𝟎 𝟎. 𝟓𝟓                            0.60
                                                                                                  0.3925         0.5969
                                                                                         2        1.1059         0.7514
               ℎ (2)
                                                                                                  1.2249         0.7729
                                           𝟎. 𝟏𝟓 𝟎. 𝟐𝟎                            0.35
                              𝑾𝟏𝑻=                                      𝒃(𝟏) =
        wih
                                           𝟎. 𝟐𝟓 𝟎. 𝟑𝟎                            0.35       0.7514
                                                                                         y=
                                                                                             0.7729
                                                                                            1
                                          0.05                                           J= 2 0.01 − 0.7514 𝟐 + 0.99 − 0.7729 𝟐
                                   𝒙=
                                          0.10
                𝑖 (2)                                                                    𝐉 = 𝟎. 𝟐𝟗𝟖𝟒


Goodfellow, I., Bengio, Y., & Courville, A. (2016). Deep learning. MIT press.                                                     28
```


<details><summary>OCR halaman (otomatis)</summary>


```text
© Forward Propagation

Compact style

ec 05
lo 10
=[oso oss) = ®=[o60 1 este [0.5933
0.3925 0.5969
2 ube (ee
1.2249 0.7729
0.15 0.20 0.35
Wir Wor = [025 0.30 be = lo 35 _ Orel)
~ 10.7729
c= [095 J=;[(0.01 — 0.7514)? + (0.99 — 0.7729)?]
i (2) mr J = 0.2984

Goodfellow, |., Bengio, Y., & Courville, A. (2016). Deep learning. MIT press. 28
OF fit weeeterreen torte GB wrrmitoacie G @nviv20 XK _t @itbomciat
```


</details>


## Halaman PDF 29

### Teks PDF

```text
   Implementing FFNN on Keras
Compact
style          from keras.models import Sequential
               from keras.layers import Dense
    𝑦 (1)
wh2y           # define the keras model
               model = Sequential()
    ℎ2 (8)
               model.add(Dense(12, input_dim=8, activation='relu'))
wh1h2          model.add(Dense(8, activation='relu'))
               model.add(Dense(1, activation='sigmoid'))
  ℎ1 (12)      # compile the keras model
               model.compile(loss='binary_crossentropy', optimizer='adam',
wxh1           metrics=['accuracy'])
               # fit the keras model on the dataset
       𝑥 (8)   model.fit(X, y, epochs=150, batch_size=10)


                                                                         29
```


<details><summary>OCR halaman (otomatis)</summary>


```text
® Implementing FFNN on Keras

Compact

style from keras.models import Sequential
from keras.layers import Dense

# define the keras model

model = Sequential ()

model.add(Dense(12, input _dim=8, activation='relu') )
model.add(Dense(8, activation='relu') )

model.add(Dense(1, activation='sigmoid') )

# compile the keras model

model.compile(loss='binary crossentropy', optimizer='adam',
metrics=['accuracy'])

# fit the keras model on the dataset

model.fit(X, y, epochs=150, batch _size=10)

78

CO EF fit weeterren tortre GD wrmitoacie @nvi920 XK gh @itbomciat
```


</details>


## Halaman PDF 30

### Teks PDF

```text
Number of Parameter
                                                      Compact
                                                      style
                                                          𝑦 (1)
                                                      wh2y
                                                          ℎ2 (8)
                                                      wh1h2
                                                        ℎ1 (12)
                                                      wxh1
                                                             𝑥 (8)
    Total parameter = (8+1)*12+(12+1)*8+(8+1)*1=221

                                                                     30
```


<details><summary>OCR halaman (otomatis)</summary>


```text
© Number of Parameter

model . summary ()|

Model: “sequential”

Layer (type) Output Shape Param #
dense_1 (Dense) (None, 8) 104
dense _2 (Dense) (None, 1) 9

Total params: 221

Trainable params: ae

Total parameter = (8+1)*12+(12+1)*8+(8+1)*1=221

CO EF fit weeterren tortre GD wrmitoacie @nvi920 XK gh @itbomciat

30
```


</details>


## Halaman PDF 31

### Teks PDF

```text
Summary


Architecture:
                   Forward          Number of
  explicit vs
                 propagation        parameter
compact style



                Next: Backpropagation


                                                31
```


<details><summary>OCR halaman (otomatis)</summary>


```text
© Summary

Architecture:

explicit vs
compact style

Forward Number of
propagation parameter

Next: Backpropagation

CD EF fit wre termien tontere GB wwmitacie G) @nvi920 XK gh @itdotciar

a
```


</details>


## Halaman PDF 32

### Teks PDF

```text
References
•   Mitchell, T. (1997). Machine learnig. McGraw-Hill. Chapter 4.
•   Russell, S., & Norvig, P. (2010). Artificial intelligence: a
    modern approach. 3rd edition. Chapter 4.2.
•   Goodfellow, I., Bengio, Y., Courville, A., & Bengio, Y.
    (2016). Deep learning (Vol. 1, No. 2). Cambridge: MIT press.




                                                                    32
```


<details><summary>OCR halaman (otomatis)</summary>


```text
© References

Mitchell, T. (1997). Machine learnig. McGraw-Hill. Chapter 4.

Russell, S., & Norvig, P. (2010). Artificial intelligence: a
modem approach. 3 edition. Chapter 4.2.

Goodfellow, I., Bengio, Y., Courville, A., & Bengio, Y.
(2016). Deep learning (Vol. 1, No. 2). Cambridge: MIT press.

Sv

CDF ith wrreternren torte GB wwwitdacse @ enviv20 XK dt eitbomciar
```


</details>


## Halaman PDF 33

> **[INTERPRETASI VISUAL]** Slide ini adalah pembatas bagian Backpropagation; selain judul ada ilustrasi maskot dengan laptop, tanpa diagram konsep tambahan.

### Teks PDF

```text
Backpropagation




                  33
```


<details><summary>OCR halaman (otomatis)</summary>


```text
Backpropagation
```


</details>


## Halaman PDF 34

### Teks PDF

```text
02
       ANN Learning: Backpropagation
                                                       Goal: set weights to minimize
                                                       error

                                                       Forward propagation:
                                                       compute output y for input
                                                       instance x

                                                       Backward propagation:
                                                       compute error term 𝛅 for
                                                       each neuron


                                                       Update every weights

                                                                                       34
https://giphy.com/gifs/neural-networks-4LiMmbAcvgTQs
```


<details><summary>OCR halaman (otomatis)</summary>


```text
ANN Learning: Backpropagation

Goal: set weights to minimize
error

Forward propagation:
compute output y for input
instance x

Backward propagation:
compute error term 6 for
each neuron

Update every weights

{
oS

https://giphy.com/gifs/neural-networks-4LiMMbACVg EQS jp weiner sore GD wowwitoreie G) envsv20 NK gh enivewere
```


</details>


## Halaman PDF 35

### Teks PDF

```text
03   Gradient Descent:
     Steepest Descent along Error Surface
     Gradient descent: a strategy for searching through a large or infinite
     hypothesis space that can be applied whenever (1) the hypothesis space
     contains continuously parameterized hypotheses (e.g., the weights in a
     linear unit), and (2) the error can be differentiated with respect to these
     hypothesis parameters.




              https://medium.com/data-science-group-iitr/loss-functions-and-optimiz ation-
              algorithms-demys tified-bb92daff331c


                                                                                             35
```


<details><summary>OCR halaman (otomatis)</summary>


```text
@ Gradient Descent:

Steepest Descent along Error Surface

Gradient descent: a strategy for searching through a large or infinite
hypothesis space that can be applied whenever (1) the hypothesis space
contains continuously parameterized hypotheses (e.g., the weights in a
linear unit), and (2) the error can be differentiated with respect to these
hypothesis parameters.

J(w) — Gradient

Gradient

V Eli]

pe OF OL
Owy Ow’ Ow,

Global cost minimum w << w + Aw

Jenin W)

= : Aw = —nVE(@)

https://medium.com/data-science-group-iitr/loss-functions-and-optimization-
algorithms-demys tified-bb9 2 daff33 1c

oe

CO EF fit weeterren tortre GD wrmitoacie @1920 XK gt @itbomciar
```


</details>


## Halaman PDF 36

### Teks PDF

```text
04
      Backpropagation for MLP
                                                      Hidden                                                   output
                                                       layer                                                    layer

       Input                  H1:                                                Hn:                       Out:                       Output
         X                              f1               …                                     fn                         f
                              net1                                               netn                      net                          O


                        𝑛𝑒𝑡1 = 𝑋𝑊1                                           𝑛𝑒𝑡𝑛 = 𝐻𝑛−1𝑊𝑛                𝑛𝑒𝑡𝑛 = 𝐻𝑛 𝑊                1
Forward                                                                      𝐻𝑛 = 𝑓𝑛 (𝑛𝑒𝑡𝑛 )                                    𝐸=                   (𝑡𝑘 −𝑜𝑘 )2
                       𝐻1 = 𝑓1(𝑛𝑒𝑡1)                                                                       𝑂 = 𝑓(𝑛𝑒𝑡)                2
Propagation                                                                                                                              𝑘∈𝑜𝑢𝑡𝑝𝑢𝑡𝑠




Backward                                                   𝜕𝑛𝑒𝑡𝑗     𝜕𝐸𝑑                                  𝜕𝑛𝑒𝑡𝑗       𝜕𝑜𝑗     𝜕𝐸𝑑         𝝏𝑬𝒅
Propagation                                                𝜕𝑤𝑗𝑖     𝜕𝑛𝑒𝑡𝑗
                                                                                                          𝜕𝑤𝑗𝑖
                                                                                                                     𝜕𝑛𝑒𝑡𝑗
                                                                                                                              𝜕𝑜𝑗
                                                                                                                                      =
                                                                                                                                          𝝏𝒘𝒋𝒊

                              𝜕𝐸𝑑                                                                                  𝜕𝐸𝑑
               𝑤𝑗𝑖 = 𝑤𝑗𝑖 −𝜂                                                                         𝑤𝑗𝑖 = 𝑤𝑗𝑖 −𝜂
                              𝜕𝑤𝑗𝑖                                                                                 𝜕𝑤𝑗𝑖

               = 𝑤𝑗𝑖 − 𝜂[−𝑜𝑗 1 − 𝑜𝑗                   −𝛿𝑘 𝑤𝑘𝑗 𝑥𝑗𝑖 ] = 𝑤𝑗𝑖 + 𝜂𝛿𝑗 𝑥𝑗𝑖                       = 𝑤𝑗𝑖 − 𝜂[−(𝑡𝑗 −𝑜𝑗 ) 𝑜𝑗 1 − 𝑜𝑗 𝑥𝑗𝑖 ]
                                       𝑘∈𝑜𝑢𝑡𝑝𝑢𝑡𝑠(𝑗)                                                       = 𝑤𝑗𝑖 + 𝜂𝛿𝑗 𝑥𝑗𝑖

                                                                                                                                                                  36
```


<details><summary>OCR halaman (otomatis)</summary>


```text
® Backpropagation for MLP

Hidden mes OUtput
layer layer

(</> WEO> > ao > ies am /*"/

Foren 1 A n n-1""n netn = Ese » Cra 2
‘ = oS t, k~ 9
Propagation Hy Filnehs) n= In(netn) a (net) on
Backward Ea Onet; 09S OEg ~=_OF qa
Propagation Onet; One; aA ™
_ aE aEq
Wii = Wii —1 OW; Wyi = Wi —7 Owji
= wy — n[-9;(1 — 9)) » —OWayj Xi] = Wy + NOX = wile re) (1 — oye
keoutputs(j) = Wii + NOj;Xji

36

OF fit weeeterreen torte GB wrrmitoacie G @nviv20 XK _t @itbomciat
```


</details>


## Halaman PDF 37

### Teks PDF

```text
 05
       Backpropagation for MLP with Sigmoid Unit

 •    Steepest gradient descent proposes new weight with negative gradient
      and Sum of Squared Error (SSE).

                                            𝜕𝐸𝑑
                  𝑤𝑗𝑖 = 𝑤𝑗𝑖 + ∆𝑤𝑗𝑖 = 𝑤𝑗𝑖 −𝜂      = 𝑤𝑗𝑖 + 𝜂𝛿𝑗 𝑥𝑗𝑖
                                            𝜕𝑤𝑗𝑖


Error term for each output unit j:
                            𝛿𝑗 = 𝑜𝑗 (1 − 𝑜𝑗 )(𝑡𝑗 − 𝑜𝑗 )
Error term for each hidden unit k:
                                                                    https://medium.com/data-science-group-iitr/loss-functions-
                           𝛿ℎ = 𝑜ℎ (1 − 𝑜ℎ )               𝑤𝑘ℎ 𝛿𝑘   and-optimization-algorithms-demystified-bb92daff331c


                                               𝑘∈𝑜𝑢𝑡𝑝𝑢𝑡𝑠

                                                                                                                            38
```


<details><summary>OCR halaman (otomatis)</summary>


```text
© Backpropagation for MLP with Sigmoid Unit

¢ Steepest gradient descent proposes new weight with negative gradient
and Sum of Squared Error (SSE).

OEg
jl
sw) wien \ / Gradient
Error term for each output unit j: j
6; = oj(1 — 0;)(tj — 9;) al _ acca
Error term for each hidden unit k: =
Sn =On(1- On) > Wend lot ee
keoutputs

38

CDF ith wrreternren torte GB wwwitdacse @ enviv20 XK di eitdomciar
```


</details>


## Halaman PDF 38

### Teks PDF

```text
06
     Computing Gradient for Output Unit Weights
 Chain rule to compute gradient:
                      𝜕𝐸𝑑 𝜕𝐸𝑑 𝜕𝑜𝑗 𝜕𝑛𝑒𝑡𝑗                            Out:
                                                                             f           Output
                           =                                       net                     O
                      𝜕𝑤𝑗𝑖   𝜕𝑜𝑗 𝜕𝑛𝑒𝑡𝑗 𝜕𝑤𝑗𝑖

                                                     𝜕𝑛𝑒𝑡𝑗
                                                           = 𝑥𝑗𝑖 ; 𝑛𝑒𝑡𝑗 =                𝑥𝑗𝑖 𝑤𝑗𝑖
                                                     𝜕𝑤𝑗𝑖
                                                                             𝑖∈[0..𝑛𝑗]

                                    𝜕𝑜𝑗    𝜕𝜎(𝑛𝑒𝑡𝑗 )
                                         =           = 𝑜𝑗 1 − 𝑜𝑗
                                   𝜕𝑛𝑒𝑡𝑗    𝜕𝑛𝑒𝑡𝑗

     𝜕𝐸𝑑    𝜕 1                        2
                                          1
         =                     (𝑡𝑘 −𝑜𝑘 ) = . 2. (𝑡𝑗 −𝑜𝑗 ). −1 = −(𝑡𝑗 −𝑜𝑗 )
     𝜕𝑜𝑗   𝜕𝑜𝑗 2                          2
                   𝑘∈𝑜𝑢𝑡𝑝𝑢𝑡𝑠
                                       𝐽𝑎𝑑𝑖 = −(𝑡𝑗 −𝑜𝑗 ) 𝑜𝑗 1 − 𝑜𝑗 𝑥𝑗𝑖                             39
```


<details><summary>OCR halaman (otomatis)</summary>


```text
© Computing Gradient for Output Unit Weights

Chain rule to compute gradient:

OEq OEq do; Onet; > Bema: /° /

Onet;
I ie[0.nj]

00; _ da(net;) _ (1 7 ad

dnet; net; J j
OEq 01 1
—=—- ty—Ox)* = =.2.(t;—-0,).-1 = —(t;—-0;
56 G2 Dy (HO = 5-2-9). 1 = “-9)

keoutputs

Jadi = —(t;—0;) o,(1 — 9) xi 39

CO EF fit weeterren tartere GD wrmitnacie @nb1920 XK gh @itdotciat
```


</details>


## Halaman PDF 39

### Teks PDF

```text
07
     Computing Gradient for Output Unit Weights
                                                              Out:        Output
     Chain rule to compute gradient:                                 f
                                                              net           O


               𝜕𝐸𝑑    𝜕𝐸𝑑 𝜕𝑜𝑗 𝜕𝑛𝑒𝑡𝑗
                    =                = −(𝑡𝑗 −𝑜𝑗 ) 𝑜𝑗         1 − 𝑜𝑗 𝑥𝑗𝑖
               𝜕𝑤𝑗𝑖   𝜕𝑜𝑗 𝜕𝑛𝑒𝑡𝑗 𝜕𝑤𝑗𝑖




                               𝛿𝑗 = 𝑜𝑗 (1 − 𝑜𝑗 )(𝑡𝑗 − 𝑜𝑗 )


              𝜕𝐸𝑑   𝜕𝐸𝑑 𝜕𝑛𝑒𝑡𝑗
                  =           = −𝛿𝑗 𝑥𝑗𝑖
              𝜕𝑤𝑗𝑖 𝜕𝑛𝑒𝑡𝑗 𝜕𝑤𝑗𝑖


                                                                                   40
```


<details><summary>OCR halaman (otomatis)</summary>


```text
© Computing Gradient for Output Unit Weights
Chain rule to compute gradient: >iat o/s /

OEq OEq Oo; Onet;
= Den = TW (ti 99) 0j(1 — 95) 25

Ow ji do; Onet; Ow ji

xii

40

CO EF fit weeterren tortre GD wrmitoacie enni920 XK ¢h @itbomciat
```


</details>


## Halaman PDF 40

### Teks PDF

```text
08
     Computing Gradient for Hidden Unit Weights
                                                    Hn:                 Out:                   Output
                                                             fn                 f
Chain rule to compute gradient:                     netn                net                      O


                       𝜕𝐸𝑑      𝜕𝐸𝑑 𝜕𝑛𝑒𝑡𝑗
                            =
                       𝜕𝑤𝑗𝑖 𝜕𝑛𝑒𝑡𝑗 𝜕𝑤𝑗𝑖
                            = −𝑜𝑗 1 − 𝑜𝑗                   𝑘∈𝑜𝑢𝑡𝑝𝑢𝑡𝑠(𝑗) −𝛿𝑘 𝑤𝑘𝑗 𝑥𝑗𝑖

                                                 𝜕𝑛𝑒𝑡𝑗
                                                       = 𝑥𝑗𝑖 ; 𝑛𝑒𝑡𝑗 =                𝑥𝑗𝑖 𝑤𝑗𝑖
                                                 𝜕𝑤𝑗𝑖
                                                                         𝑖∈[0..𝑛𝑗]

       𝜕𝐸𝑑                      𝜕𝐸𝑑 𝜕𝑛𝑒𝑡𝑘 𝜕𝑜𝑗
            =                                  =                  −𝛿𝑘 𝑤𝑘𝑗 𝑜𝑗 1 − 𝑜𝑗
      𝜕𝑛𝑒𝑡𝑗                    𝜕𝑛𝑒𝑡𝑘 𝜕𝑜𝑗 𝜕𝑛𝑒𝑡𝑗
                𝑘∈𝑜𝑢𝑡𝑝𝑢𝑡𝑠(𝑗)                       𝑘∈𝑜𝑢𝑡𝑝𝑢𝑡𝑠(𝑗)


                                    𝜕𝐸𝑑
                                         = −𝛿𝑗
                                   𝜕𝑛𝑒𝑡𝑗
                                                                                                        41
```


<details><summary>OCR halaman (otomatis)</summary>


```text
© Computing Gradient for Hidden Unit Weights

Chain rule to compute gradient: ad | > ino >/ os /

= —-o9(1— 0;) vikeoutputs(j) ~OKWKj Xji

™

Onet;
ap, ey = >. xjiWji
# ie€[0.nj]
~ = —5, wo;
Onet; » .Onet, Go; Anet; x. . 1c Wiej j( oj)
ke€outputs(j) \ ke€outputs(j)
OEq ——
Onet; a

41

CO EF fit weeterren tortre GD wrmitoacie @ni920 XK dt @itbomciat
```


</details>


## Halaman PDF 41

### Teks PDF

```text
09
       Computing Gradient for Hidden Unit Weights
                                                   Hn:                Out:          Outpu
                                                             fn              f        t
                                                   netn               net            O
     Chain rule to compute gradient:
           𝜕𝐸𝑑        𝜕𝐸𝑑 𝜕𝑛𝑒𝑡𝑗
                  =                = −𝑜𝑗 1 − 𝑜𝑗           𝑘∈𝑜𝑢𝑡𝑝𝑢𝑡𝑠(𝑗) 𝛿𝑘 𝑤𝑘𝑗 𝑥𝑗𝑖
           𝜕𝑤𝑗𝑖       𝜕𝑛𝑒𝑡𝑗 𝜕𝑤𝑗𝑖


                               𝛿ℎ = 𝑜ℎ (1 − 𝑜ℎ )                  𝛿𝑘 𝑤𝑘ℎ
                                                   𝑘∈𝑜𝑢𝑡𝑝𝑢𝑡𝑠(ℎ)


                      𝜕𝐸𝑑
                           = −𝛿ℎ 𝑥𝑗𝑖
                      𝜕𝑤𝑗𝑖

                                                                                            42
```


<details><summary>OCR halaman (otomatis)</summary>


```text
© Computing Gradient for Hidden Unit Weights
Chain rule to compute gradient:

Abe Out: Outpu
>HaG > ieao>/""/
OEq _ OEq Onetj _

Awji  Onet; Awji —o;(1 — 9) Lkeoutputs({) OkWej Xi

iL On = On(1 — On) ». OkWkn
keEoutputs(h)

AE 4

= —OnXji

42

CO EF fit weeterren tortre GD wrmitoacie @ni920 XK dt @itbomciat
```


</details>


## Halaman PDF 42

> **[INTERPRETASI VISUAL]** Algoritma pada gambar mengalir dari inisialisasi jaringan dan bobot, propagasi input ke depan, perhitungan galat unit keluaran, perhitungan galat unit tersembunyi, lalu pembaruan bobot. Rumus galat dan pembaruan bobot berada pada gambar asli; hasil OCR rumus perlu diperiksa terhadap slide.

**[TRANSKRIPSI MANUAL GAMBAR]**

```text
BACKPROPAGATION(training_examples, η, n_in, n_out, n_hidden)
δk ← ok(1 − ok)(tk − ok)                                  (T4.3)
δh ← oh(1 − oh) Σ[k∈outputs] wkh δk                     (T4.4)
wji ← wji + Δwji
Δwji = η δj xji                                          (T4.5)
```

### Teks PDF

```text
11



     Backpropagation
     Algorithm
     (Mitchell, 1996)




                    44
```


<details><summary>OCR halaman (otomatis)</summary>


```text
ee —
_ BACKPROPAGATION( training examples, n, Nin, Mout, "hidden)
re Each training example is a pair of the form (x,i ), where x is the vector of network input
values, and ft is the vector of target network output values.
n is the learning rate (e.g., .05). nin is the number of network inputs, nhiaden the number of
units in the hidden layer, and noy: the number of output units.
The input from unit i into unit j is denoted x;;, and the weight from unit i to unit j is denoted
Wji-
@ Create a feed-forward network with nj, inputs, maiggen hidden units, and no,, output units.
@ Initialize all network weights to small random numbers (e.g., between —.05 and .05).
@ Until the termination condition is met, Do
@ For each (Z,7 ) in training-examples, Do

Propagate the input forward through the network:

1. Input the instance ¥ to the network and compute the output 0, of every unit u in
the network.

Propagate the errors backward through the network:
2. For each network output unit k, calculate its error term 5;

5k — OK(1 — OK) (tk — O%) (74.3)
3. For each hidden unit h, calculate its error term 5,
bh on on) D> wende (744)
k€outputs

4. Update each network weight wy;
wi <— wii + Aw;

where
Awyi =Nn 5 Xi (T4.5)

GO EF ith weeeterrcr tarts GD wrmitnacie @nvi920 XK gh @itbomciat

Backpropagation

Algorithm
(Mitchell, 1996)

44
```


</details>


## Halaman PDF 43

### Teks PDF

```text
12
     Mini-batch Stochastic Gradient Descent

Epoch                                                  Training data
Iterasi pada backpropagation untuk semua training
data atau semua mini-batch.                               dimention
Batch size                                             atr_1 ...   atr_di   target_   ...   target_t
parameter ukuran mini-batch (hasil split training                  m        1
data).
Jika batch size = 1, proses incremental/true SGD
Jika batch size = |training data|, proses batch SGD
                                                                     mini-batch_1
Jika 1<batch size<|training data|, proses mini-batch
SGD                                                                  mini-batch_2

Step                                                                        ...
Pemrosesan satu mini batch diakhiri dengan update
bobot                                                                mini-batch_n
                                                                                                   45
```


<details><summary>OCR halaman (otomatis)</summary>


```text
® Mini-batch

Epoch

Iterasi pada backpropagation untuk semua training
data atau semua mini-batch.

Batch size

parameter ukuran mini-batch (hasil split training
data).

Jika batch size = 1, proses incremental/true SGD
Jika batch size = |training data], proses batch SGD
Jika 1<batch size<|training data|, proses mini-batch
SIE}B)

Gradient Descent

Training data

dimention
target_ target_t
1
mini-batch_1
mini-batch_2
mini-batch_n
@ ow ¢ *
```


</details>


## Halaman PDF 44

### Teks PDF

```text
Thank You




            46
```


<details><summary>OCR halaman (otomatis)</summary>


```text
Thank You

EF itn worreterncen tontens GD wowiti.acie G) ends920 XX gh eiidomeiat
```


</details>
