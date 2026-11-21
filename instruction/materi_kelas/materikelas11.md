# Materi Kelas 11

Sumber: `1793828353558_2026_IF3070_Materi11-LinearLogisticRegression.pdf`  
Jumlah halaman PDF: 33

Teks PDF di bawah disalin dari lapisan teks. Blok OCR adalah keluaran otomatis dari gambar halaman; ejaan, urutan, dan rumus di dalamnya perlu dicek terhadap PDF. Catatan visual yang ditambahkan akan selalu diberi penanda **[INTERPRETASI VISUAL]**.


## Halaman PDF 1

### Teks PDF

```text
IF3070 Dasar Inteligensi Artifisial
Institut Teknologi Bandung

Linear Regression & Logistic Regression
Semester I TA 2026/2027
```


<details><summary>OCR halaman (otomatis)</summary>


```text
IF3070 Dasar Inteligensi Artifisial

Institut Teknologi Bandung

Linear Regression & Logistic Regression

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


                                        2
```


<details><summary>OCR halaman (otomatis)</summary>


```text
° Outline
° Review:
¢ Learning Agent
¢ Introduction to Data Science
¢ CRISP-DM
* Data Understanding
* Data Preparation
¢ K-Nearest Neighbor
° Naive Bayes

Decision Tree Learning

¢ Linear Regression
° Logistic Regression

CDF ith wrreternren torte GB wwwitdacse @ enviv20

XK dh @itdomcias
```


</details>


## Halaman PDF 3

### Teks PDF

```text
Linear Regression




                    3
```


<details><summary>OCR halaman (otomatis)</summary>


```text
Linear Regression
```


</details>


## Halaman PDF 4

### Teks PDF

```text
Regression: Introduction
As an example, we are a real estate agent, and in charge of selling a new house. We don’t
know the price, and we want to infer it by comparing it with other houses. We look at
features of the house which could influence the house, i.e. number of rooms. At the end of
the day, what we want is a formula on the feature which gives us the price of the house, or
at least an estimate for it.




                                                               train




https://livebook.manning.com/book/grokking-machine-learning/3-1-the-problem-we-need-to-predict-the-price-of-a-house/v-4/44   4
```


<details><summary>OCR halaman (otomatis)</summary>


```text
Regression: Introduction

As an example, we are a real estate agent, and in charge of selling anew house. We don’t
know the price, and we want to infer it by comparing it with other houses. We look at
features of the house which could influence the house, i.e. number of rooms. At the end of
the day, what we want is a formula on the feature which gives us the price of the house, or
at least an estimate for it.

z * train

https:/Aivebook.manning.com/book/grokking-machine-learning/3-1-the-problem-we-need-to-predict-the-price-of-a-house/v-4/44
CDF ith werreterncren tortor GF wwwitdacse G@ enviv20 XK gh @itdomcias
```


</details>


## Halaman PDF 5

### Teks PDF

```text
Linear Relationship
 ● The price of the house is dependent variable or response, and
   number of rooms is independent variable or regressor or predictor.
 ● A reasonable form of a relationship between the response Y and the
   regressor x is the linear relationship: Y = β0 +β1x




                                      β0 is the intercept and
                                      β1 is the slope



https://livebook.manning.com/book/grokking-machine-learning/3-1-the-problem-we-need-to-predict-the-price-of-a-house/v-4/44   5
```


<details><summary>OCR halaman (otomatis)</summary>


```text
Inear Relationship

e The price of the house is dependent variable or response, and
number of rooms is independent variable or regressor or predictor.

e A reasonable form of a relationship between the response Y and the
regressor x is the linear relationship: Y = By +B ,x

Y

ig Gee 400

g 8
2
%
g
As
4
¢
3
A %
oq
5

By is the intercept and =
} Bo B, is the slope

x

Number of roorns
Figure 11.1: A linear relationship; $9: intercept; 3): slope.

https:/Aivebook.manning.com/book/grokking-machine-learning/3-1-the-problem-we-need-to-predict-the-price-of-a-house/v-4/44
CDF ith werreterncren torte GF wwwitdrcse G) enviv20 XK gh @itdomcias
```


</details>


## Halaman PDF 6

### Teks PDF

```text
Regression: Predict Response Y based on Regressor x




                                                                       price=100+50*4=300



https://livebook.manning.com/book/grokking-machine-learning/3-1-the-problem-we-need-to-predict-the-price-of-a-house/v-4/44   6
```


<details><summary>OCR halaman (otomatis)</summary>


```text
Regression: Predict Response Y based on Regressor x

Figure 6. Our task is now to predict the price of the house with 4 rooms. Using the model (line), we deduce that the predicted price of this
house is $300.

Price

1 2 3 4 s 6 7

https:/Aivebook.manning.com/book/grokking-machine-learning/3-1-the- roblem-we-need-to-predict- -the-price-of-a-house/v-4/44
DE fit enter Ferrer tasters. wow it ache @rv1920 KX ft @itbomciar
```


</details>


## Halaman PDF 7

### Teks PDF

```text
     Regression Modeling: Example




Sumber: DTS - Thematic Academy 2021 - Regresi

                                                7
```


<details><summary>OCR halaman (otomatis)</summary>


```text
1 d#[["ENGINESIZE", ‘COZEMISSIONS')].sample(S)

Regression Modeling: Example

ENGINESIZE CO2EMISSIONS

697
872
614
351

450

New Car

350

Emission

BER ss

1 df.shape

(1067, 13)
Sumber: DTS - Thematic Academy 2021 - Regresi

CO EF fit weeterren tortre GD wrmitoacie @nb1920 XK gh @itdotciat

2.0
38
24
5.4
35

BREE s

a
tain
test

1 2 4 5 8
Engine size
```


</details>


## Halaman PDF 8

### Teks PDF

```text
Simple Linear Regression: Training




                         y=125.49+39.14x


                                           8
```


<details><summary>OCR halaman (otomatis)</summary>


```text
© Simple Linear Regression: Training

On auvbh WN

from sklearn import linear_model

regr = linear_model.LinearRegression()

train_x = np.asanyarray(train[['ENGINESIZE']])
train_y = np.asanyarray(train[['CO2ZEMISSIONS']])
regr.fit (train_x, train_y)

# The coefficients

print ('Coefficients: ', regr.coef_)

print (‘Intercept: ',regr.intercept_)

Coefficients: [[39.43522758]]
Intercept: [124.41641136]

Emission
Bees Bs

g

Engine size

y=125.49+39.14x

CO EF fit weeterren tortre GD wrmitoacie @nvi920 XK dt @itbomciat
```


</details>


## Halaman PDF 9

> **[INTERPRETASI VISUAL]** Kode di kiri melatih LinearRegression dengan ENGINESIZE, CYLINDERS, dan FUELCONSUMPTION_COMB untuk memprediksi CO2EMISSIONS. Tabel menampilkan lima baris data contoh; heatmap kanan menunjukkan korelasi antarempat variabel, termasuk CO2EMISSIONS dengan tiga fitur tersebut.

### Teks PDF

```text
Multivariate Linear Regression:
Training & Testing




                                  9
```


<details><summary>OCR halaman (otomatis)</summary>


```text
» Multivariate Linear Regression:
- Training & Testing

from sklearn import linear_model

regr2 = linear_model.LinearRegression()

train_x = np.asanyarray(train[['ENGINESIZE’, 'CYLINDERS', 'FUELCONSUMPTION_COMB']])
train_y = np.asanyarray(train[['CO2EMISSIONS']])

regr2.fit (train_x, train_y)

print ('Coefficients: ', regr2.coef_)

print (‘Intercept: ',regr2.intercept_)

Ne

Now fw

Coefficients: [[11.36694334 7.26349823 9.58219844]] -1.000
Intercept: [64.98474243] ENGINESIZE { 0975
0950
CYUNDERS ass
ENGINESIZE CYLINDERS FUELCONSUMPTION_COMB CO2EMISSIONS 0.900
0o875
0 2.0 4 8.5 196 FUELCONSUMPTION_COMB
0850
1 2.4 4 9.6 221 ome
3 3.5 6 11.1 255 8 ¥ 2
% §
4 3.5 6 10.6 244 § : z
Zs 8

FUELCONSUMPTION_COMB

OF fit weeeterreen torte GB wrrmitoacie G @nviv20 XK _t @itbomciat
```


</details>


## Halaman PDF 10

### Teks PDF

```text
Estimating Parameters: Least Square Estimator
● Objective function: minimize sum of the squares of the residuals/errors (SSE)




                                                                                  =σXY/σ 2X


                                                                                       10
```


<details><summary>OCR halaman (otomatis)</summary>


```text
Estimating Parameters: Least Square Estimator

e@ Objective function: minimize sum of the squares of the residuals/errors (SSE)

SSE =) = (0 — 0)" = Slr — bo — bre,
a i=l i=1
ASSE)__ yy pp pe. — ,
dbo 2D bo — bizi) = = ~2 (ui ~ bo ~ braid

n n
nby + by er = You
i=l i=l

e n nSayw-(Sa)(Sv) LSei-awi-g)
> Yi — by +? Z; Be me i=l - (= ‘) ( ) — i=! 7 =0yy/02,
bo = 4—1 i=1 — 7 _ bz n bp zy? - (2 ) PA - £)?
n =] i=1

10
```


</details>


## Halaman PDF 11

> **[INTERPRETASI VISUAL]** Tiga panel gambar memuat definisi matematis variance, covariance, dan correlation coefficient, masing-masing untuk kasus diskret/kontinu yang relevan. Rumus korelasi di panel bawah adalah ρxy = σxy/(σxσy).

**[TRANSKRIPSI MANUAL GAMBAR]**

```text
Let X be a random variable with probability distribution f(x) and mean μ. The variance of X is
σ² = E[(X − μ)²] = Σₓ (x − μ)² f(x), if X is discrete, and
σ² = E[(X − μ)²] = ∫₋∞^∞ (x − μ)² f(x) dx, if X is continuous.
The positive square root of the variance, σ, is called the standard deviation of X.

Let X and Y be random variables with joint probability distribution f(x,y). The covariance of X and Y is
σxy = E[(X − μx)(Y − μy)] = Σₓ Σᵧ (x − μx)(y − μy) f(x,y), if X and Y are discrete, and
σxy = E[(X − μx)(Y − μy)] = ∫₋∞^∞ ∫₋∞^∞ (x − μx)(y − μy) f(x,y) dx dy, if X and Y are continuous.

Let X and Y be random variables with covariance σxy and standard deviations σx and σy, respectively. The correlation coefficient of X and Y is
ρxy = σxy / (σx σy).
```

### Teks PDF

```text
11
```


<details><summary>OCR halaman (otomatis)</summary>


```text
Let X be a random variable with probability distribution f(«) and mean p. The
variance of X is

o? = E[(X — p)*] = XG —p)* f(z), if X is discrete, and

=z

oo
o? = E|(X — p)*] = / (x — p)? f(a) dex, if X is continuous.
-oo

The positive square root of the variance, o, is called the standard deviation of
Pe

covariance of X and Y is

Oxy = El(X — wx)(¥ -— py) = 0 So (e- wx) (y — my) fey)
= uy
if X and Y are discrete, and

oxy = BUX — ux)(¥ -y)]= f © [= nsdn) fee) de dy

if X and Y are continuous.

Let X and Y be random variables with joint probability distribution f(x,y). The

Let X and Y be random variables with covariance o,, and standard deviations
ox and oy, respectively. The correlation coefficient of X and Y is

Oxy
OxOy .

Cy

DF fit weeeterrciee tasters GB wrmitoacie @ e@nviv20 XK _t @itdomciat

11
```


</details>


## Halaman PDF 12

> **[INTERPRETASI VISUAL]** Dua panel membandingkan perhitungan koefisien dan intercept regresi linear sederhana dari rumus covariance/variance dengan hasil sklearn LinearRegression; keduanya menampilkan koefisien sekitar 39.435 dan intercept sekitar 124.416.

### Teks PDF

```text
Implement From Scratch: Simple Linear
Regression




                                        12
```


<details><summary>OCR halaman (otomatis)</summary>


```text
e
Regression

From Scratch

b1=covariance(X, Y)/variance(X)
b0=mean(Y)-b1"*mean(X)

1 # Coefficients: [[39.43522758]]

2 # Intercept: [124.41641136]

3 print('cov(X,Y)=",train.COZEMISSIONS.cov(train.ENGINESIZE) )

4 print('var(X)=', train. ENGINESIZE.var())

5 bi=train.CO2ZEMISSIONS.cov(train. ENGINESIZE)/train. ENGINESIZE.var()
6 b@=train.CO2ZEMISSIONS.mean()-b1i*train.ENGINESIZE.mean()

7 print('Coefficient=',b1)

8 print('Intercept=',be)

cov(X,Y)= 78.95604822766e53
var(X)= 2.0021704722919877
Coefficient= 39.43522757943557
Intercept= 124.41641136306387

On Au PWN eB

Implement From Scratch: Simple Linear

from sklearn import linear_model

regr = linear_model.LinearRegression()

train_x = np.asanyarray(train[['ENGINESIZE']])
train_y = np.asanyarray(train[['CO2ZEMISSIONS']])
regr.fit (train_x, train_y)

# The coefficients

print ('Coefficients: ', regr.coef_)

print (‘Intercept: ',regr.intercept_)

Coefficients: [[39.43522758]]
Intercept: [124.41641136]

ee

DF fit weeeterrciee tasters GB wrmitoacie @ e@nviv20 XK _t @itdomciat
```


</details>


## Halaman PDF 13

### Teks PDF

```text
Linear Regression: Supervised Learning
Learning a (possibly incorrect) general function from specific input-output pairs

    I/O pairs
   Training set                 Least Square                        Hypothesis h    y=64.98+11.37x1
                                                                                    +7.26x2+9.58x3
  <data, label>                  Estimation                            h≈f




                                          Unseen
                                           data
                                                                   Predict                 label

                                                                 y=64.98+11.37x1
                                                                 +7.26x2+9.58x3




                                                                                                   13
```


<details><summary>OCR halaman (otomatis)</summary>


```text
Linear Regression: Supervised Learning

Learning a (possibly incorrect) general function from specific input-output pairs

SS

ENGINESIZE CYLINDERS FUELCONSUMPTION COMB CO2EMISSIONS

a wneo

20
24
18
38
35

oon & &

85
96
59
Wd
10.6

196
221
136
255
244

Least Square

Estimation

ENGINESIZE CYLINDERS FUELCONSUMPTION COMB

2.0 4 85
24 4 96
15 4 59
1 test_y[@:3]
array([[196),
(221),

{136)1, ‘Py tesstee tehnteg Banteng ® wowsdscie © enviv20 XK _t eitdomeiar

ae
¥
a CS a

y=64.98+11.37x1
+7.26x2+9.58x3

y=64.98+1 37x 1 s#test_y_ = regr2.predict(test_x)
+7.26x2+9.58x3 testy less]

array([[198.22130673],
[213.3e8se235],
[167.62411912}])

is}
```


</details>


## Halaman PDF 14

> **[INTERPRETASI VISUAL]** Bagian atas membandingkan hasil uji regresi univariat; bagian bawah multivariat. Di kanan terdapat rumus MAE, MSE, dan R². Angka pada slide menunjukkan MAE 22.50, MSE 840.97, R² 0.73 untuk univariat; MAE 15.20, MSE 443.90, R² 0.87 untuk multivariat.

### Teks PDF

```text
 Linear Regression: Testing
                             Univariate:
                             y=125.49+39.14x




Multivariate: y=64.98+11.37x1+7.26x2+9.58x3




                                               14
```


<details><summary>OCR halaman (otomatis)</summary>


```text
Linear Regression: Testing

1 from sklearn.metrics import r2_score . . Recto doer

2 . peatnen gah oes
3 test_x = np.asanyarray(test[[ ‘ENGINESIZE']]) Univariate: Acca mtn wt

4 test_y = np.asanyarray(test[['COZEMISSIONS']]) = oe

5S test_y_ = regr.predict(test_x) y 1 25.49 39. 1 4x MAE = AE [D1 jag —|y |
6 n

7 print("Mean absolute error: %.2f" % np.mean(np.absolute(test_y_ - test_y)))

8 print("Residual sum of squares (MSE): %.2f" % np.mean((test_y_ - test_y) ** 2)) Pema ag

9 print("R2-score: %.2~" % r2_score(test_y_ , test_y) )

Mean absolute error: 22.58
Residual sum of squares (MSE): 840.97
R2-score: @.73

Multivariate: y=64.98+11.37x1+7.26x2+9.58x3 “

1 from sklearn.metrics import r2_score

2

3 test_x = np.asanyarray(test[['ENGINESIZE', ‘CYLINDERS’, 'FUELCONSUMPTION_COMB*]])

4 test_y_ = regr2.predict(test_x)

5

6 print("Mean absolute error: %.2*" % np.mean(np.absolute(test_y_ - test_y))) NO% _ ¥,)?
7 print("Residual sum of squares (MSE): %.2f" % np.mean((test_y_ - test_y) ** 2)) R2 = if — <=N
8 print("R2-score: %.2f" % r2_score(test_y_ , test_y) ) YL10% os y)

Mean absolute error: 15.20
Residual sum of squares (MSE): 443.90
R2-score: @.87

14

CO EF fit weeterren tortre GD wrmitoacie @nb1920 XK gh @itdotciat
```


</details>


## Halaman PDF 15

### Teks PDF

```text
   Linear Regression - LSE: Summary
Target function is estimated by             Cost function J(𝞱) assigns a large cost
hypothesis as a linear function of X:       to bad predictions h(x) and small cost
h𝞱(x)=𝞱0+𝞱1x1+...+𝞱nxn=𝜮𝞱ixi, i in [0..n]   to good predictions h(x). For LSE, we
→ h𝞱(x) = 𝞱T.x                              used sum of squares errors (SSE).


Find good 𝞱 (parameters or weights): 𝞱*=argmin J(𝞱)
Analytical solution: find 𝞱 that solve 𝛁J(𝞱)=0.

If 𝛁J(𝞱)=0 is unable to solve, use iterative numerical methods. The simplest
method is gradient descent.


                                                                                      15
```


<details><summary>OCR halaman (otomatis)</summary>


```text
© Linear Regression - LSE: Summary

Target function is estimated by
hypothesis as a linear function of X:
ho(X)=O9tO4X1+...+0,X,=2 0X, iin [0..n]
— h(x) = 6'.x

Cost function J(@) assigns a large cost
to bad predictions h(x) and small cost
to good predictions h(x). For LSE, we
used sum of squares errors (SSE).

Find good @ (parameters or weights): 8*=argmin J(@)
Analytical solution: find @ that solve V,(@)=0.

BE! fan totter teense nantens

15
```


</details>


## Halaman PDF 16

### Teks PDF

```text
Logistic Regression




                      16
```


<details><summary>OCR halaman (otomatis)</summary>


```text
Logistic Regression
```


</details>


## Halaman PDF 17

### Teks PDF

```text
    Regression Analysis

                                                                                              Finding the best relationship between
                                                                                              Y and x: not deterministic, random error

                                                                                              Quantifying the strength of that
                                                                                              relationship. Random error with
                                                                                              E(error)=0 and homoscedasticity.
                                                                                              Least Squared Estimation (LSE)

                                                                                              Predicting of the response value y
Walpole, R. E., Myers, R. H., Myers, S. L., & Ye, K. (2012). Probability and Statistics for
                                                                                              given values of the regressor x.
engineering and sciences. Pearson Education, 430-435.




                                                                                                                                         17
```


<details><summary>OCR halaman (otomatis)</summary>


```text
Finding the best relationship between
Y and x: not deterministic, random error

Quantifying the strength of that
relationship. Random error with
E(error)=0 and homoscedasticity.
Least Squared Estimation (LSE

n

PEER rEL EL eee | ecicting of the response value y
Walpole, R. E., Myers, R. H., Myers, S. L., & Ye, K. (2012). Probability and Statistics for g Iven values of the regressor x.

engineering and sciences. Pearson Education, 430-435.

sch

CDF ith wereterncrey tontene GD wwmitdrcie G) @u1920 XX gh @itbomctar
```


</details>


## Halaman PDF 18

### Teks PDF

```text
 Classification Using Linear Regression
Example: Dataset has 200 observations (5 attributes), and the target
attribute is hon, indicating if a student is in an honors class or not.
                                                   We are able to predict the value
                                                   along the Y-axis. If Y is greater than
                                                   0.5 (above the green line), predict
                                                   that the student is in honor class
                                                   otherwise not in honor class.



                                                            Linear Model or
                                                      Linear Discriminant Function
                                                           or Linear Classifier


                                                                                            18
```


<details><summary>OCR halaman (otomatis)</summary>


```text
® Classification Using Linear Regression

Example: Dataset has 200 observations (5 attributes), and the target
attribute is hon, indicating if a student is in an honors class or not.

10

os

06

o4

02

00

55

We are able to predict the value
along the Y-axis. If Y is greater than
0.5 (above the green line), predict
that the student is in honor class
otherwise not in honor class.

Linear Model or

Linear Discriminant Function
or Linear Classifier

18

CO EF fit weeterren tortre GD wrmitoacie @nb1920 XK gh @itdotciat
```


</details>


## Halaman PDF 19

### Teks PDF

```text
          Linear Discriminant Function
          Linear Combination + Decision Rule



    Decision rule
                                                                                                    Discriminant function:
                                                                                                 a linear combination of the
                                                                                                       components of x
                                                                                                g(x)=w0x0 + w1x1 + · · · + wdxd = wTx

     Linear combination: w0x0 + w1x1 + · · · + wdxd = wTx




RO Duda, PE Hart, and DG Stork, Pattern Classification, 2nd edition, John Wiley & Sons , 2001
https://www.cs.toronto.edu/~rgrosse/courses/csc321_2018/readings/L03% 20Linear%20Classifiers.
pdf
                                                                                                                                        19
```


<details><summary>OCR halaman (otomatis)</summary>


```text
© Linear Discriminant Function

Linear Combination + Decision Rule

a

Discriminant function:
a linear combination of the

components of x
Q(X)=WoX + W4X4 + + + WgXq = WIX

l Linear combination: WoXg + W1X1 + * «+ + WgXq = WX y

we

RO Duda, PE Hart, and DG Stork, Pattern Classification, 2nd edition, John Wiley & Sons, 2001
https :/www.cs.toronto.edu/~rgrosse/courses/csc321_2018/readings/L03% 20Linear%20Classifiers.

es 19

CO EF fit weeterren tortre GD wrmitoacie @ni920 XK dt @itbomciat
```


</details>


## Halaman PDF 20

### Teks PDF

```text
        Hyperplane Decision Surface

 Decision rule




                                                                                                       Decision rule:
                                                                                                Decide ω1 if g(x)>0 and ω2 if g(x)<0
   Linear combination: w0x0 + w1x1 + · · · + wdxd = wTx                                              g(x)=0: decision surface
                                                                                                   ω1 and ω2 are target classes




RO Duda, PE Hart, and DG Stork, Pattern Classification, 2nd edition, J ohn Wiley & Sons, 2001
                                                                                                                                       20
```


<details><summary>OCR halaman (otomatis)</summary>


```text
Hyperplane Decision Surface

Tal Ye az mz Te Pt Le P| ay 7
| Decision rule J
== = = = mea = ol =i

Decision rule:

Decide w, if g(x)>0 and wz if g(x)<0
g(x)=0: decision surface
W, and Ws are target classes

‘\

RO Duda, PE Hart, and DG Stork, Pattern Classification, 2nd edition, John Wiley & Sons, 2001

DE itn bevrreerermrog tortor GY wwwitdacse G envrv20 XK gt eitdotciat

20
```


</details>


## Halaman PDF 21

### Teks PDF

```text
         Hyperplane Decision Surface

                                                                                                Discriminant function:
                                                                                                      g(x)=wTx


                                                                                                      Decision rule:
                                                                                               Decide ω1 if g(x)>0 and ω2 if g(x)<0
                                                                                                    g(x)=0: decision surface
                                                                                                  ω1 and ω2 are target classes


RO Duda, PE Hart, and DG Stork, Pattern Classification, 2nd edition, John Wiley & Sons, 2001



                                                                                                                                      21
```


<details><summary>OCR halaman (otomatis)</summary>


```text
© Hyperplane Decision Surface

Discriminant function:
g(x)=w'x

Decision rule:
Decide w, if g(x)>0 and wa if g(x)<0
g(x)=0: decision surface
W, and W, are target classes

Figure 5.2: The linear decision boundary H, where g(x) = w'x + wp = 0, separates
the feature space into two half-spaces R, (where g(x) > 0) and R2 (where g(x) < 0).

RO Duda, PE Hart, and DG Stork, Pattern Classification, 2nd edition, John Wiley & Sons, 2001

21

CD EF fit wre termien tontere GB wwmitacie G) @nvi920 XK gh @itdotciar
```


</details>


## Halaman PDF 22

### Teks PDF

```text
                      Linear                                             Logistic
                    Regression                                          Regression




                                                                                                                                 http://www.saedsayad.com/logistic _regression.htm




                                                                                                                                         Logistic (sigmoid) function



Walpole, R. E., Myers , R. H., Myers, S. L., & Ye, K. (2012). Probability and Statistics for engineering and sciences. Pearson Education, 430-435.

                                                                                                                                                                                     22
```


<details><summary>OCR halaman (otomatis)</summary>


```text
Estimate the y Y = dy + D,X 4 Linear Mode!

ape Pra
= , a probability of classes p Logistic Model
east s :
quares Maximum likelihood pt
~ 1+ en@othsx)

Constant variance Non-constant
variance 0

Response Variable

is normal Response variable is

binary

http://www.saedsayad.com/logistic_regression.htm

Logistic (sigmoid) function

1

ak rr

Walpole, R. E., Myers, R. H., Myers, S. L., & Ye, K. (2012). Probability and Statistics for engineering and sciences. Pearson Education, 430-435.

dd

DF tity Wvrrcetermiog tanters GY wwwitdacse G envrv20 NK gh eibomeiat
```


</details>


## Halaman PDF 23

### Teks PDF

```text
Logistic Regression

                                       Walpole et al. (2012):
                                       Odds of success = p/(1-p)
                    y_hat=0.03x-1.33   Logistic regression estimates
                                       the probability of classes:


 y_hat=0.08x-5.46
                                       Coefficients in logistic
                                       regression are in terms of the
                                       log odds, that is, the
                                       coefficient 0.08 implies that a
                                       one unit change in “write”
                                       results in a 0.08 unit change in
                                       the log of the odds.
                                       https://stats.idre.ucla.edu/stata/faq/how-do-i-interpret-

                                       odds-ratios-in-logistic-regression/

                                                                                                   23
```


<details><summary>OCR halaman (otomatis)</summary>


```text
© Logistic Regression

j= e( 2) = BT x = by. 1 + byx, to + bara

1-p
10 @ Actual wee
@ Logistic
os @ Linear
y_hat=0.03x-1.33
06 ait e
- 04 : : eesee
= a2} y_hat=0.08x-5.46 3 ec!
eT TT ee :
00 3 $ er ee ee80e 8 @e
ooo”
-0.2 ao"
-0.4 a e
30 é ) 40 45 30 55 o

write

CDF ith wrrreterncren torte § GF wwwitdrcse G) enviv20 XK gh @itdomcias

Walpole et al. (2012):

Odds of success = p/(1-p)
Logistic regression estimates
the probability of classes:
p = P(y = 1|x,b) = ise¥
Coefficients in logistic
regression are in terms of the
log odds, that is, the
coefficient 0.08 implies that a
one unit change in “write”
results in a 0.08 unit change in
the log of the odds.

https ://s tats.idre.ucla.edu/stata/faq/how-do-i-interpret-

odds-ratios-in-logistic-regression/

JES
```


</details>


## Halaman PDF 24

> **[INTERPRETASI VISUAL]** Tiga kotak centang merangkum logistic regression sebagai linear model, binary classification, dan soft classification. Di kanan tertulis bentuk log-odds linear dan peluang kelas positif melalui fungsi sigmoid.

### Teks PDF

```text
Summary: Logistic Regression

 🗹 Linear model


 🗹 Binary
 classification


 🗹 Soft classification




                               24
```


<details><summary>OCR halaman (otomatis)</summary>


```text
Summary: Logistic Regression

= ™ Linear model ——, '
9= oe

Bccsiicion
classification p= P(y = 11x,b) =
m ™ Soft classification [aaa

) =p'x= bo. 1+ byxy +++ bgXxq

0 EF ith Wworreternicn tances GB wwmitd.scie G) @ndie20 XK gh eitdociat
```


</details>


## Halaman PDF 25

### Teks PDF

```text
Exercise


                                       Given these linear
                    y_hat=0.07x-4.85   regression and logistic
                                       regression models for
                                       classification, determine
 y_hat=0.03x-1.35                      whether a student that has
                                       write score 65 is in honors
                                       class.

                                       Threshold class 1 p > 0.5



                                                                     25
```


<details><summary>OCR halaman (otomatis)</summary>


```text
© Exercise ?

Ld)
10} @ Actual eee e@ 8 . .
© Levis Given these linear
08 — . . .
y_hat=0.07x-4.85. | regression and logistic
°° woot ne regression models for
,” a oe classification, determine
aj] (erU lees see g*° whether a student that has
e ecooseee® @ . -
ee write score 65 is in honors
e
02 ia class.
-0.4 — '
0 5 Ps se 55 & és Threshold class 1 p > 0.5

25

CDF ith werreterncren tortor § GF wwwitdacse G enviv20 XK gh @itdomcias
```


</details>


## Halaman PDF 26

### Teks PDF

```text
Stochastic Gradient Ascent
 Optimization Algorithm for Logistic Regression




                                                  26
```


<details><summary>OCR halaman (otomatis)</summary>


```text
Stochastic Gradient Ascent

0 EF fith Wworreeternien tantere GB wwmito.scie G) @ndie20 XK gt eitdomciat
```


</details>


## Halaman PDF 27

### Teks PDF

```text
Logistic Regression


                       +1
                                 b0
                 x1
                       b1                      Logistic
                        b2
                                      ∑=bT.x function     p   p≥0.5   class
                 x2

                 ...
                            bd



                 xd




                                                                              27
```


<details><summary>OCR halaman (otomatis)</summary>


```text
p

y= ie(2 >) = bl x = by.1 + by x, +--+ baXa p =P(y =1|x,b) =

Input x=(1, x), Xp, ...,Xq)

Model b=(bo, b;, by, ..., by)

Y= bx = by.1 + bx, +--+ + Dyxq
Output = o(>)

© Logistic Regression

1
1+e-b'x

+1

Logistic
function

DF fit weeeterrciee tasters GB wrmitoacie @ e@nviv20 XK _t @itdomciat

class

oe
```


</details>


## Halaman PDF 28

### Teks PDF

```text
   Maximum Likelihood Estimator For Logistic
   Regression
Estimator that results in a maximum value for its joint probability or maximizes
the likelihood of the sample

Formal
definition
(Elkan, 2014):




Stochastic gradient ascent is optimization method that changes the coefficient
values (as random approximation to true derivative) to increase the log
likelihood based on a randomly chosen example at a time.
Stochastic gradient update of bj is:

                                                             https://cseweb.ucsd.edu/~elkan/250B/logreg.pdf
                                                                                                              28
```


<details><summary>OCR halaman (otomatis)</summary>


```text
@© Maximum Likelihood Estimator For Logistic
Regression

Estimator that results in a maximum value for its joint probability or maximizes
the likelinood of the sample

Given the training set {<x,,y,>..<x,,y,7}, learn logistic regression classifier by maximizing
Formal the log joint conditional likelihood, that is the sum of log conditional likelihood (LCL) for
definition each training example. x;; is the value of the jth feature of the ith training example.

Chiro LCL = di_,loglL(@;ylxi) = Liz1,),-: logpi + dist;y log(1 — p;)
ALC
> a = Lily — Pi) xij

Stochastic eT is optimization method that changes the coefficient
values (as random apiece arta to true derivative)to = ~——itthe log

likelihood based ona | tie = at a time.

Stochastic gradient update of b is: | a
n : learning rate the tS As st]

https ://cseweb.ucsd.edu/~elk an/250B/logreg.pdf

28

CF ith were terror torte GF wwwitdacie @nvi920 XK dt @itbomciat
```


</details>


## Halaman PDF 29

### Teks PDF

```text
     Stochastic Gradient Ascent for Logistic
     Regression


                Initialize b                                                    b=[0,0,0] #b0=0; b1=0; b2=0
                                                                                t=1:
                For t=1, …, T:                                                   <[62,58],1>:
                                                                                 pi=1/(1+e-0)=0.5
                    For each example <xi,yi>: #randomly chosen example           b0=0+0.1(1-0.5)*1=0.05
                                                                                 b1=0+0.1(1-0.5)*62=3.1
    One                                                                          b2=0+0.1(1-0.5)*58=2.9
iteration =             pi=prediction for xi using the current coefficients b
                                                                                 <[52,41],0>:
one epoch                                                                        pi=1/(1+e-(0.05+3.1*52+2.9*41))
                                                                                 =1/(1+e-280.15)=1
                                                                                 b0=0.05+0.1(0-1)*1= -0.05
                Return b                                                         b1=3.1+0.1(0-1)*52= -2.1
                                                                                 b2=2.9+0.1(0-1)*41= -1.2
              http://www.cs.cmu.edu/~wcohen/10-605/sgd-part2.pdf

                                                                                                                   29
```


<details><summary>OCR halaman (otomatis)</summary>


```text
Regression

@ Stochastic Gradient Ascent for Logistic

INPUT: TRAINING DATA D={<X,,Y1>...<Xy,Yy>}; MAX-ITER T; LEARNING RATE 77

a

X

Initialize b

a

he

For t=1, ..., T:

iteration= §&
one epoch

r “For each example <xi,yi>: #randomly chosen example |

pi=prediction for xi using the current coefficients b

For each non-zero feature of xij: bj = bj + ni — Pi) Xi;

6

Xe

Return b

http:/Avww.cs.cmu.edu/~wcohen/10-605/sgd-part2. pdf

CO EF fit weeterren tortre GD wrmitoacie enni920 XK ¢h @itbomciat

D: {<[52,41],0>,<[62,58], |>};T=1;7=0.1

| b=[0,0,0] #b0=0; b1=0; b2=0
t=1:

<[62,58],1>:

pi=1/ (1+e°)=0.5
b0=0+0.1(1-0.5) *1=0.05
b1=0+0.1(1-0.5) *62=3.1
b2=0+0.1(1-0.5) *58=2.9
<[52,41] ,0>:

pi=1/ (te (0-05+3.1*52+2.9%41) )
=1/ (1+e°280-15) =]
bO=0.05+0.1(0-1) *1= -0.05
Ibis 3 OFF 1 CO = 1s) 2a ae
lb2—2F 9+ O02 10-1) +4 — ade

78
```


</details>


## Halaman PDF 30

### Teks PDF

```text
Prediction
•   b0= -0.05; b1= -2.1; b2= -1.2
•   D: {<[52,41],0>,<[62,58],1>}
     •   x1=[52,41]: p1= 1/(1+e-(-0.05-2.1*52-1.2*41)) =1/(1+e158.45)=1.53*10-69 ->
         class=0 (p1<0.5)
     •   x2=[62,58]: p2= 1/(1+e-(-0.05-2.1*62-1.2*58)) =1/(1+e199.85)=1.61*10-87 ->
         class=0 (p2<0.5)
•   Akurasi training = ½ = 50%




                                                                                      30
```


<details><summary>OCR halaman (otomatis)</summary>


```text
© Prediction

* b0= -0.05; b1= -2.1; b2= -1.2

- D: {<[52,41],0>,<[62,58], 1>}
© x4=[52,41]: p1= 1/(1 +e--0.05-2.1°52-1.2°41)) = 4 /(4 +@158.45)= 1 53*4 0-69 >
class=0 (p1<0.5)
© x2=[62,58]: p2= 1/(1+e-(-0.05-2.1°62-1.2°58)) =4/(4 +e199.85)=4_61*10-87 >
class=0 (p2<0.5)

- Akurasi training = 7/2 = 50%

30
```


</details>


## Halaman PDF 31

### Teks PDF

```text
      Summary: Logistic Regression

                                                             Model: b ∈ ℜd+1
      +1
                b0
x1
      b1                      Logistic
                     ∑=bT.x function         p≥0.5   class   Maximum Likelihood
x2     b2
                                         p                   estimator
...

                                                             Stochastic gradient
           bd
                                                             ascent
xd




                                                                                   31
```


<details><summary>OCR halaman (otomatis)</summary>


```text
Summary: Logistic Regression

= Model: b € R41 ——
+1
peewee Vaximum Likelihood
estimator
m™ Stochastic gradient
ascent

Logistic
function

0 EF ith Wworreternicn tances GB wwmitd.scie G) @ndie20 XK gh eitdociat

a
```


</details>


## Halaman PDF 32

### Teks PDF

```text
References
•   Walpole, R. E., Myers, R. H., Myers, S. L., & Ye, K. (2012). Probability
    and Statistics for engineering and sciences. Pearson Education, 430-
    435. Chapter 11 & 12.12, 9.14
•   RO Duda, PE Hart, and DG Stork, Pattern Classification, 2nd edition,
    John Wiley & Sons, 2001. Chapter 5
•   Charles Elkan (2014). Maximum Likelihood, Logistic Regression, and
    Stochastic Gradient Training.
    https://cseweb.ucsd.edu/~elkan/250B/logreg.pdf
•   Russell, S., & Norvig, P. (2010). Artificial intelligence: a modern
    approach. 3rd edition. Chapter 18.6.4.

                                                                               32
```


<details><summary>OCR halaman (otomatis)</summary>


```text
© References

¢ Walpole, R. E., Myers, R. H., Myers, S.L., & Ye, K. (2012). Probability
and Statistics for engineering and sciences. Pearson Education, 430-
435. Chapter 11 & 12.12, 9.14

¢ RO Duda, PE Hart, and DG Stork, Pattern Classification, 2nd edition,
John Wiley & Sons, 2001. Chapter 5

¢ Charles Elkan (2014). Maximum Likelihood, Logistic Regression, and
Stochastic Gradient Training.
https://cseweb.ucsd.edu/~elkan/250B/logreg.pdf

¢ Russell, S., & Norvig, P. (2010). Artificial intelligence: a modern
approach. 3 edition. Chapter 18.6.4.

Sv
```


</details>


## Halaman PDF 33

### Teks PDF

```text
Thank You




            33
```


<details><summary>OCR halaman (otomatis)</summary>


```text
Thank You

EF itn worreterncen tontens GD wowiti.acie G) ends920 XX gh eiidomeiat
```


</details>
