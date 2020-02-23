Python 3.6.9 (default, Nov  7 2019, 10:44:02) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> type(32)
<class 'int'>
>>> max('Hello world')
'w'
>>> min('Hello world')
' '
>>> len('Hello world')
11
>>> len('1+2+3-4')
7
>>> print('Type conversion functions')
Type conversion functions
>>> int('32')
32
>>> int('Hello')
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    int('Hello')
ValueError: invalid literal for int() with base 10: 'Hello'
>>> int(3.999999)
3
>>> int(-2.3)
-2
>>> float(32)
32.0
>>> float('3.14159'
	  )
3.14159
>>> str(32)
'32'
>>> str(3.14159)
'3.14159'
>>> print('Math functions')
Math functions
>>> import math
>>> print(math)
<module 'math' (built-in)>
>>> ratio = signal_power / noise power
SyntaxError: invalid syntax
>>> ratio = signal_power / noise_power
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    ratio = signal_power / noise_power
NameError: name 'signal_power' is not defined
>>> radians = 0.7
>>> height = math.sin(radians)
>>> print(height)
0.644217687237691
>>> degrees = 45
>>> radians = degrees/360*2*math.pi
>>> radians
0.7853981633974483
>>> math.sin(radians)
0.7071067811865475
>>> math.sqrt(2)/2.0
0.7071067811865476
>>> print('Random numbers')
Random numbers
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/5th_Exercises.py ===========
0.3505861890477001
0.23348476864019652
0.2789564983444647
0.5016670415563002
0.9018100234043698
0.214880050134036
0.6709417075308547
0.5782215371385937
0.5667610830493951
0.2003021220578196
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/5th_Exercises.py ===========
0.7188759928510589
0.39739267972241443
0.2403155880967437
0.400847451835206
0.2596871359701357
0.4030366198921925
0.6149438883725858
0.44725746279471223
0.9384440048753753
0.24009439315166625

>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/5th_Exercises.py ===========
0.7342810067458498
0.03825626898401002
0.637653409355901
0.14844219646557655
0.8698098109632798
0.442038489941055
0.142032773685979
0.12984196521186397
0.1204226141752539
0.09268579512445219
>>> random.randint(5,10)
8
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/5th_Exercises.py ===========

 Exercise 1 

0.05632831745920586
0.4834941772264967
0.27420665894054885
0.5964117196232678
0.11887494100046458
0.030126995853229865
0.7690353903897643
0.3036324821218117
0.9201648761613141
0.30787588278283395
6
7
7
9
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/5th_Exercises.py ===========

 Exercise 1 

0.2221191892401585
0.20428374271683147
0.7572532120967904
0.3636571361926315
0.3512104364406514
0.565672701711252
0.2449511785972841
0.8454695427708362
0.08995164929835409
0.8222391681193103

Random int's

9
5
9
10
To choose an element from a sequence at random, you can use choice
Traceback (most recent call last):
  File "/home/ren/RTR108_2020/4WEEK/5th_Exercises.py", line 15, in <module>
    z = random.choice(t)
  File "/usr/lib/python3.6/random.py", line 258, in choice
    i = self._randbelow(len(seq))
TypeError: object of type 'int' has no len()
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/5th_Exercises.py ===========

 Exercise 1 

0.4328390190303154
0.756195305613011
0.41661632652407643
0.42863661949715715
0.4988479177810088
0.7907249743175851
0.2105514356006365
0.28594155857243697
0.7280162339528345
0.27784894210677946

Random int's

8
9
10
10
To choose an element from a sequence at random, you can use choice
Traceback (most recent call last):
  File "/home/ren/RTR108_2020/4WEEK/5th_Exercises.py", line 14, in <module>
    for t in range(t):
TypeError: 'list' object cannot be interpreted as an integer
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/5th_Exercises.py ===========

 Exercise 1 

0.3236144799722914
0.7822004709083406
0.17722956068586915
0.17145434455366138
0.4625188347794622
0.7439218740279343
0.6489539730676148
0.8163505302729532
0.13467142164178736
0.8971436947759026

Random int's

10
6
6
6
To choose an element from a sequence at random, you can use choice
2
1
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/5th_Exercises.py ===========

 Exercise 1 

0.16967615224311328
0.7824089005483552
0.6264141613509611
0.7030255519198269
0.09504272260187308
0.3592361597877646
0.1769744795777819
0.15567747881234106
0.6221936487075013
0.33875038302540084

Random int's

9
7
6
8

To choose an element from a sequence at random, you can use choice

2
2
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/5th_Exercises.py ===========

 Exercise 1 

0.5267534943327858
0.578048417707197
0.364541996614987
0.9436799347698083
0.3464933642186284
0.11995653202032974
0.6060496905507715
0.4673672864023485
0.7498562030178831
0.038469597734801075

Random int's

8
8
5
6

To choose an element from a sequence at random, you can use choice

2
2
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/5th_Exercises.py ===========

 Exercise 1 

0.5114695263896792
0.56085214389006
0.268437905131805
0.8361737174040167
0.08771521207200017
0.14839959771737465
0.24263790551084818
0.9559501705453263
0.9166568518133948
0.4695689805104093

Random int's

6
10
5
7

To choose an element from a sequence at random, you can use choice

1
1

Adding new functions

>>> print(print_lyrics)
<function print_lyrics at 0x7f6ed9851e18>
>>> print(type(print_lyrics))
<class 'function'>
>>> print_lyrics()
I'm a lumberjack, and I'm okay
I sleep all night and work all day
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/5th_Exercises.py ===========

 Exercise 1 

0.7901846747161358
0.7328828840662397
0.4658394779926758
0.542031937535423
0.06651855825816988
0.9114797801178445
0.15626678922273607
0.06848368657563886
0.9336128977614497
0.48671342639990234

Random int's

7
5
6
7

To choose an element from a sequence at random, you can use choice

1
3

Adding new functions

I'm a lumberjack, and I'm okay
I sleep all night and work all day
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/5th_Exercises.py ===========

 Exercise 1 

0.16015386922429442
0.08096388510213326
0.9194888390513699
0.8650999383909865
0.10348304248840812
0.9173750172854883
0.6230175968530955
0.35463243604331696
0.8278775187646845
0.311151959122262

Random int's

6
9
8
7

To choose an element from a sequence at random, you can use choice

3
3

Adding new functions

I'm a lumberjack, and I'm okay
I sleep all night and work all day
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/5th_Exercises.py ===========

 Exercise 1 

0.8508484122525781
0.6293706757664804
0.8338021042382827
0.56431824048262
0.7612395890266074
0.9605820982437431
0.8670079178150334
0.7405186644482479
0.8708497410475335
0.4276262926651556

Random int's

9
5
7
8

To choose an element from a sequence at random, you can use choice

2
1

Adding new functions

I'm a lumberjack, and I'm okay
I sleep all night and work all day
I'm a lumberjack, and I'm okay
I sleep all night and work all day
I'm a lumberjack, and I'm okay
I sleep all night and work all day
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/5th_Exercises.py ===========

 Exercise 1 

0.711575741665753
0.5288442477530603
0.8458570019633765
0.24884162990844827
0.6329654944526762
0.80870076428218
0.7501702448852021
0.7270007497508199
0.48773436299613593
0.44118006250066377

Random int's

5
5
10
10

To choose an element from a sequence at random, you can use choice

2
2

Adding new functions

I'm a lumberjack, and I'm okay
I sleep all night and work all day
I'm a lumberjack, and I'm okay
I sleep all night and work all day
I'm a lumberjack, and I'm okay
I sleep all night and work all day

Definitions and uses
 Exercise 2

Traceback (most recent call last):
  File "/home/ren/RTR108_2020/4WEEK/5th_Exercises.py", line 33, in <module>
    repeat_lyrics_1
NameError: name 'repeat_lyrics_1' is not defined
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/5th_Exercises.py ===========

 Exercise 1 

0.9118952271379306
0.9834337104976328
0.8783006478438306
0.7259781479019264
0.8017692223374484
0.9091950139138871
0.8417624780759962
0.8890292991631867
0.21789271469591986
0.2885716526890064

Random int's

10
8
5
10

To choose an element from a sequence at random, you can use choice

2
2

Adding new functions

I'm a lumberjack, and I'm okay
I sleep all night and work all day
I'm a lumberjack, and I'm okay
I sleep all night and work all day
I'm a lumberjack, and I'm okay
I sleep all night and work all day

Definitions and uses
 Exercise 2 & 3

>>> def print_twice(bruse)
SyntaxError: invalid syntax
>>> 
>>> def print_twice(bruce):
	print(bruce)
	print(bruce)

>>> print_twice(huh)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    print_twice(huh)
NameError: name 'huh' is not defined
>>> print_twice(bruce)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    print_twice(bruce)
NameError: name 'bruce' is not defined
>>> math.pi(*4)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    math.pi(*4)
NameError: name 'math' is not defined
>>> import math
>>> math.pi(*4)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    math.pi(*4)
TypeError: float object argument after * must be an iterable, not int
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/5th_Exercises.py ===========

 Exercise 1 

0.3560822106553254
0.8050643956661057
0.4741570466582725
0.768414390803069
0.8773875248957995
0.5256603512597797
0.003083059140182809
0.46755002758850894
0.6670504349766593
0.4283022482126878

Random int's

6
8
8
5

To choose an element from a sequence at random, you can use choice

2
1

Adding new functions

I'm a lumberjack, and I'm okay
I sleep all night and work all day
I'm a lumberjack, and I'm okay
I sleep all night and work all day
I'm a lumberjack, and I'm okay
I sleep all night and work all day

Definitions and uses
 Exercise 2 & 3


Parameters and arguments

>>> print_twice('Spam')
Spam
Spam
>>> print_twice(1)
1
1
>>> import math
>>> print_twice(math.pi)
3.141592653589793
3.141592653589793
>>> print_twice('Spam '*4)
Spam Spam Spam Spam 
Spam Spam Spam Spam 
>>> print_twice(math.cos(math,pi))
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    print_twice(math.cos(math,pi))
NameError: name 'pi' is not defined
>>> import math
>>> print_twice(math.cos(math.pi))
-1.0
-1.0
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/5th_Exercises.py ===========

 Exercise 1 

0.6320312995207475
0.04193084904041744
0.07624299260205558
0.724561358035751
0.017067699389572977
0.7984920518486145
0.0021255235555496244
0.2608981133465279
0.7874608809161161
0.6599754491564374

Random int's

8
10
10
10

To choose an element from a sequence at random, you can use choice

3
3

Adding new functions

I'm a lumberjack, and I'm okay
I sleep all night and work all day
I'm a lumberjack, and I'm okay
I sleep all night and work all day
I'm a lumberjack, and I'm okay
I sleep all night and work all day

Definitions and uses
 Exercise 2 & 3


Parameters and arguments

Eric, the half a bee.
Eric, the half a bee.
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/5th_Exercises.py ===========

 Exercise 1 

0.6712665787135128
0.002303567049259714
0.9315807502896918
0.9787267779684051
0.6146062022516856
0.5859767741064031
0.24859362835418464
0.4795585774551502
0.5585491663867256
0.95900682992279

Random int's

9
7
5
6

To choose an element from a sequence at random, you can use choice

1
3

Adding new functions

I'm a lumberjack, and I'm okay
I sleep all night and work all day
I'm a lumberjack, and I'm okay
I sleep all night and work all day
I'm a lumberjack, and I'm okay
I sleep all night and work all day

Definitions and uses
 Exercise 2 & 3


Parameters and arguments

Eric, the half a bee.
Eric, the half a bee.

Fruitful functions and void functions

Traceback (most recent call last):
  File "/home/ren/RTR108_2020/4WEEK/5th_Exercises.py", line 51, in <module>
    x = math.cos(radians)
NameError: name 'math' is not defined
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/5th_Exercises.py ===========

 Exercise 1 

0.17565374993678562
0.8319255488052409
0.5498295922347077
0.40771189869880975
0.7086181159891664
0.2800637320288373
0.2187176136179214
0.6234734500684386
0.6913608968030641
0.14681107373427738

Random int's

8
8
8
5

To choose an element from a sequence at random, you can use choice

3
1

Adding new functions

I'm a lumberjack, and I'm okay
I sleep all night and work all day
I'm a lumberjack, and I'm okay
I sleep all night and work all day
I'm a lumberjack, and I'm okay
I sleep all night and work all day

Definitions and uses
 Exercise 2 & 3


Parameters and arguments

Eric, the half a bee.
Eric, the half a bee.

Fruitful functions and void functions

Traceback (most recent call last):
  File "/home/ren/RTR108_2020/4WEEK/5th_Exercises.py", line 52, in <module>
    x = math.cos(radians)
NameError: name 'radians' is not defined
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/5th_Exercises.py ===========

 Exercise 1 

0.7729022233226501
0.9635749758429983
0.7876556058848749
0.3173050515283453
0.6374529777994737
0.18409258647648452
0.20358252525731968
0.5188426495959569
0.3602945030933349
0.021436987697529553

Random int's

6
9
10
8

To choose an element from a sequence at random, you can use choice

1
1

Adding new functions

I'm a lumberjack, and I'm okay
I sleep all night and work all day
I'm a lumberjack, and I'm okay
I sleep all night and work all day
I'm a lumberjack, and I'm okay
I sleep all night and work all day

Definitions and uses
 Exercise 2 & 3


Parameters and arguments

Eric, the half a bee.
Eric, the half a bee.

Fruitful functions and void functions

>>> result print_twice('Bing')
SyntaxError: invalid syntax
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/5th_Exercises.py ===========

 Exercise 1 

0.7112220352165729
0.8030508238309699
0.7464293424672873
0.05697225781860327
0.21922271505523927
0.3546022584755727
0.23463686395144379
0.5100926873255646
0.585602433006981
0.2500235904644815

Random int's

6
6
8
9

To choose an element from a sequence at random, you can use choice

1
3

Adding new functions

I'm a lumberjack, and I'm okay
I sleep all night and work all day
I'm a lumberjack, and I'm okay
I sleep all night and work all day
I'm a lumberjack, and I'm okay
I sleep all night and work all day

Definitions and uses
 Exercise 2 & 3


Parameters and arguments

Eric, the half a bee.
Eric, the half a bee.

Fruitful functions and void functions

>>> print_twice(17)
17
17
>>> result = print_twice('Bing')
Bing
Bing
>>> print(result)
None
>>> print(type(None))
<class 'NoneType'>
>>> print(type(result))
<class 'NoneType'>
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/5th_Exercises.py ===========

 Exercise 1 

0.26234128539465196
0.5485499551205462
0.7738868845529642
0.0887343754399218
0.11862312116759899
0.2564867914652711
0.1613999842016336
0.5392550959993982
0.6745218126640249
0.9430106565582022

Random int's

10
10
8
9

To choose an element from a sequence at random, you can use choice

3
1

Adding new functions

I'm a lumberjack, and I'm okay
I sleep all night and work all day
I'm a lumberjack, and I'm okay
I sleep all night and work all day
I'm a lumberjack, and I'm okay
I sleep all night and work all day

Definitions and uses
 Exercise 2 & 3


Parameters and arguments

Eric, the half a bee.
Eric, the half a bee.

Fruitful functions and void functions

>>> addtwo(1,2)
3
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/5th_Exercises.py ===========

 Exercise 1 

0.38334972689344227
0.8821653513775966
0.7493724642244128
0.23524840554611026
0.3578748057739112
0.7442679369210408
0.10849738970760858
0.2213297276123729
0.1610148545839024
0.4266188238819729

Random int's

9
10
9
8

To choose an element from a sequence at random, you can use choice

2
1

Adding new functions

I'm a lumberjack, and I'm okay
I sleep all night and work all day
I'm a lumberjack, and I'm okay
I sleep all night and work all day
I'm a lumberjack, and I'm okay
I sleep all night and work all day

Definitions and uses
 Exercise 2 & 3


Parameters and arguments

Eric, the half a bee.
Eric, the half a bee.

Fruitful functions and void functions

8
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/5th_Exercises.py ===========

 Exercise 1 

0.10426792517643857
0.48719681906152135
0.34856905224623813
0.48025931133475774
0.7418710779786479
0.25969539465405467
0.05537857477980479
0.2679382089073974
0.7260024565670659
0.6715821513016969

Random int's

9
9
9
10

To choose an element from a sequence at random, you can use choice

3
2

Adding new functions

I'm a lumberjack, and I'm okay
I sleep all night and work all day
I'm a lumberjack, and I'm okay
I sleep all night and work all day
I'm a lumberjack, and I'm okay
I sleep all night and work all day

Definitions and uses
 Exercise 2 & 3


Parameters and arguments

Eric, the half a bee.
Eric, the half a bee.

Fruitful functions and void functions

8

Exercise 5

ABC
Zap
ABC
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/5th_Exercises.py ===========

 Exercise 1 

0.11231241893696786
0.6081264266614572
0.6470931036038249
0.6512651344491922
0.4197280536108168
0.729839272311287
0.34186131431313216
0.4635352716213267
0.05903494969027412
0.406119687182117

Random int's

6
7
10
9

To choose an element from a sequence at random, you can use choice

2
1

Adding new functions

I'm a lumberjack, and I'm okay
I sleep all night and work all day
I'm a lumberjack, and I'm okay
I sleep all night and work all day
I'm a lumberjack, and I'm okay
I sleep all night and work all day

Definitions and uses
 Exercise 2 & 3


Parameters and arguments

Eric, the half a bee.
Eric, the half a bee.

Fruitful functions and void functions

8

 Exercise 5 

ABC
Zap
ABC

 Exercis 6 

>>> computepay(45,10)
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/5th_Exercises.py ===========

 Exercise 1 

0.3557604549148795
0.8121270569252563
0.5159267407537192
0.542469257436314
0.12732644385308556
0.5052238990895708
0.07158424511160122
0.5938958974431535
0.2769611864068031
0.672994959255319

Random int's

8
10
8
8

To choose an element from a sequence at random, you can use choice

1
3

Adding new functions

I'm a lumberjack, and I'm okay
I sleep all night and work all day
I'm a lumberjack, and I'm okay
I sleep all night and work all day
I'm a lumberjack, and I'm okay
I sleep all night and work all day

Definitions and uses
 Exercise 2 & 3


Parameters and arguments

Eric, the half a bee.
Eric, the half a bee.

Fruitful functions and void functions

8

 Exercise 5 

ABC
Zap
ABC

 Exercise 6 

>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/5th_Exercises.py ===========

 Exercise 1 

0.6711103944607288
0.7703134695838604
0.1131583380010226
0.3614934259573973
0.24154662414321226
0.564339166004269
0.6737882439735943
0.20454061695763182
0.193086666504924
0.7303226114759557

Random int's

9
8
9
8

To choose an element from a sequence at random, you can use choice

2
3

Adding new functions

I'm a lumberjack, and I'm okay
I sleep all night and work all day
I'm a lumberjack, and I'm okay
I sleep all night and work all day
I'm a lumberjack, and I'm okay
I sleep all night and work all day

Definitions and uses
 Exercise 2 & 3


Parameters and arguments

Eric, the half a bee.
Eric, the half a bee.

Fruitful functions and void functions

8

 Exercise 5 

ABC
Zap
ABC

 Exercise 6 

>>> computepay(45,10)
475.0
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/5th_Exercises.py ===========

 Exercise 1 

0.08014726341989664
0.3965291124334567
0.4366578987462071
0.1896875668788971
0.6094142108839702
0.6815045840213397
0.9574590543203678
0.9876700683622931
0.3977133504966903
0.950788861928667

Random int's

7
9
9
6

To choose an element from a sequence at random, you can use choice

3
1

Adding new functions

I'm a lumberjack, and I'm okay
I sleep all night and work all day
I'm a lumberjack, and I'm okay
I sleep all night and work all day
I'm a lumberjack, and I'm okay
I sleep all night and work all day

Definitions and uses
 Exercise 2 & 3


Parameters and arguments

Eric, the half a bee.
Eric, the half a bee.

Fruitful functions and void functions

8

 Exercise 5 

ABC
Zap
ABC

 Exercise 6 

>>> conputepay(45,10)
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    conputepay(45,10)
NameError: name 'conputepay' is not defined
>>> computepay(45,10)
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    computepay(45,10)
  File "/home/ren/RTR108_2020/4WEEK/5th_Exercises.py", line 78, in computepay
    print('Hours: %f \n Wage %f', hours, wage)
UnboundLocalError: local variable 'wage' referenced before assignment
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/5th_Exercises.py ===========

 Exercise 1 

0.5788083665998043
0.8202033471086602
0.09008521139406567
0.04940111601926778
0.31291549710029665
0.8729248579425722
0.3429578757284324
0.6715375844602017
0.4277889401300544
0.4023085360908998

Random int's

6
9
8
9

To choose an element from a sequence at random, you can use choice

2
3

Adding new functions

I'm a lumberjack, and I'm okay
I sleep all night and work all day
I'm a lumberjack, and I'm okay
I sleep all night and work all day
I'm a lumberjack, and I'm okay
I sleep all night and work all day

Definitions and uses
 Exercise 2 & 3


Parameters and arguments

Eric, the half a bee.
Eric, the half a bee.

Fruitful functions and void functions

8

 Exercise 5 

ABC
Zap
ABC

 Exercise 6 

>>> computepay(45,10)
Hours: %f 
 Rate: %f 45 10
475.0
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/5th_Exercises.py ===========

 Exercise 1 

0.6192303355594848
0.5249826676014668
0.2132713072250787
0.3825357901909885
0.7365871180729388
0.9145086293586333
0.2859416067574434
0.5021386148028414
0.0054078917178467245
0.17180845200551598

Random int's

8
10
8
6

To choose an element from a sequence at random, you can use choice

3
3

Adding new functions

I'm a lumberjack, and I'm okay
I sleep all night and work all day
I'm a lumberjack, and I'm okay
I sleep all night and work all day
I'm a lumberjack, and I'm okay
I sleep all night and work all day

Definitions and uses
 Exercise 2 & 3


Parameters and arguments

Eric, the half a bee.
Eric, the half a bee.

Fruitful functions and void functions

8

 Exercise 5 

ABC
Zap
ABC

 Exercise 6 

>>> computepay(45,10)
Hours: 45.000000 
 Rate: 10.000000
475.0
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/5th_Exercises.py ===========

 Exercise 1 

0.7031716159163139
0.7153261963378366
0.06112168147933861
0.20894615131489958
0.3935578793266381
0.35305050847744945
0.11739056431692774
0.8678704130682457
0.11300854436475549
0.5628266847820502

Random int's

9
10
10
7

To choose an element from a sequence at random, you can use choice

2
2

Adding new functions

I'm a lumberjack, and I'm okay
I sleep all night and work all day
I'm a lumberjack, and I'm okay
I sleep all night and work all day
I'm a lumberjack, and I'm okay
I sleep all night and work all day

Definitions and uses
 Exercise 2 & 3


Parameters and arguments

Eric, the half a bee.
Eric, the half a bee.

Fruitful functions and void functions

8

 Exercise 5 

ABC
Zap
ABC

 Exercise 6 

>>> computepay(45,10)
Hours: 45.000000.2 
 Rate: 10.000000.2
475.0
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/5th_Exercises.py ===========

 Exercise 1 

0.9518014668743437
0.9040059146236196
0.34636126693289804
0.8907744033013567
0.8273091864175154
0.06660310584455031
0.9722268898759314
0.4483245870075714
0.6963154810833538
0.7499992560339257

Random int's

6
7
7
9

To choose an element from a sequence at random, you can use choice

3
3

Adding new functions

I'm a lumberjack, and I'm okay
I sleep all night and work all day
I'm a lumberjack, and I'm okay
I sleep all night and work all day
I'm a lumberjack, and I'm okay
I sleep all night and work all day

Definitions and uses
 Exercise 2 & 3


Parameters and arguments

Eric, the half a bee.
Eric, the half a bee.

Fruitful functions and void functions

8

 Exercise 5 

ABC
Zap
ABC

 Exercise 6 

>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/5th_Exercises.py ===========

 Exercise 1 

0.5573495557445857
0.612842522080822
0.6744384869425971
0.2165941446913069
0.28377382423876096
0.8094224162754365
0.7260873524333865
0.5612716419879329
0.12057753856235598
0.7329116802956644

Random int's

10
10
6
8

To choose an element from a sequence at random, you can use choice

2
1

Adding new functions

I'm a lumberjack, and I'm okay
I sleep all night and work all day
I'm a lumberjack, and I'm okay
I sleep all night and work all day
I'm a lumberjack, and I'm okay
I sleep all night and work all day

Definitions and uses
 Exercise 2 & 3


Parameters and arguments

Eric, the half a bee.
Eric, the half a bee.

Fruitful functions and void functions

8

 Exercise 5 

ABC
Zap
ABC

 Exercise 6 

Hours: 45.00 
 Rate: 10.00
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/5th_Exercises.py ===========

 Exercise 1 

0.3239348444027512
0.5922151593092938
0.8214768321204081
0.7624856768043159
0.13169554620498036
0.01808052273382743
0.28410864170556527
0.9260822216161021
0.40219867767372575
0.17810615485218673

Random int's

6
6
7
7

To choose an element from a sequence at random, you can use choice

3
2

Adding new functions

I'm a lumberjack, and I'm okay
I sleep all night and work all day
I'm a lumberjack, and I'm okay
I sleep all night and work all day
I'm a lumberjack, and I'm okay
I sleep all night and work all day

Definitions and uses
 Exercise 2 & 3


Parameters and arguments

Eric, the half a bee.
Eric, the half a bee.

Fruitful functions and void functions

8

 Exercise 5 

ABC
Zap
ABC

 Exercise 6 

Hours: 45.00 
 Rate: 10.00
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/5th_Exercises.py ===========

 Exercise 1 

0.38568578103810514
0.8558804913791681
0.24604995630486293
0.2557511270819368
0.9054970595879355
0.540431396148204
0.8702630267679694
0.649201151348691
0.2508097180427096
0.52147559862539

Random int's

10
6
5
5

To choose an element from a sequence at random, you can use choice

2
2

Adding new functions

I'm a lumberjack, and I'm okay
I sleep all night and work all day
I'm a lumberjack, and I'm okay
I sleep all night and work all day
I'm a lumberjack, and I'm okay
I sleep all night and work all day

Definitions and uses
 Exercise 2 & 3


Parameters and arguments

Eric, the half a bee.
Eric, the half a bee.

Fruitful functions and void functions

8

 Exercise 5 

ABC
Zap
ABC

 Exercise 6 

Hours: 45.00 
 Rate: 10.00
Pay:  475.0
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/5th_Exercises.py ===========

 Exercise 1 

0.30401640516507744
0.21564358209803391
0.020690459094083513
0.2644735494253825
0.4521158130707752
0.2817892174340304
0.5470561964253802
0.9262665214836113
0.003294690886684104
0.7209531835148093

Random int's

10
6
7
8

To choose an element from a sequence at random, you can use choice

3
3

Adding new functions

I'm a lumberjack, and I'm okay
I sleep all night and work all day
I'm a lumberjack, and I'm okay
I sleep all night and work all day
I'm a lumberjack, and I'm okay
I sleep all night and work all day

Definitions and uses
 Exercise 2 & 3


Parameters and arguments

Eric, the half a bee.
Eric, the half a bee.

Fruitful functions and void functions

8

 Exercise 5 

ABC
Zap
ABC

 Exercise 6 

Hours: 45.00 
Rate: 10.00
Pay:  475.0
>>> computepay(11,11)
Hours: 11.00 
Rate: 11.00
Pay:  121
121
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/5th_Exercises.py ===========

 Exercise 1 

0.6852657597602502
0.28362369682242994
0.4225044612113007
0.5372776805597689
0.43709601546543275
0.2543056295203615
0.8033935293128215
0.13608311251625516
0.4836474621870386
0.03642118945834205

Random int's

8
8
6
6

To choose an element from a sequence at random, you can use choice

2
3

Adding new functions

I'm a lumberjack, and I'm okay
I sleep all night and work all day
I'm a lumberjack, and I'm okay
I sleep all night and work all day
I'm a lumberjack, and I'm okay
I sleep all night and work all day

Definitions and uses
 Exercise 2 & 3


Parameters and arguments

Eric, the half a bee.
Eric, the half a bee.

Fruitful functions and void functions

8

 Exercise 5 

ABC
Zap
ABC

 Exercise 6 

Hours: 45.00 
Rate: 10.00
Pay:  475.0

 Exercise 7 

>>> computegrade(0.2)
Grade: C
>>> computegrade(gg)
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    computegrade(gg)
NameError: name 'gg' is not defined
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/5th_Exercises.py ===========

 Exercise 1 

0.09972460237907044
0.32915823917049203
0.686938633253133
0.0013256721340325628
0.8374345444105513
0.9720997053768686
0.08025095921369085
0.4523324238697035
0.01940278365018866
0.5197649466697343

Random int's

5
9
5
6

To choose an element from a sequence at random, you can use choice

1
2

Adding new functions

I'm a lumberjack, and I'm okay
I sleep all night and work all day
I'm a lumberjack, and I'm okay
I sleep all night and work all day
I'm a lumberjack, and I'm okay
I sleep all night and work all day

Definitions and uses
 Exercise 2 & 3


Parameters and arguments

Eric, the half a bee.
Eric, the half a bee.

Fruitful functions and void functions

8

 Exercise 5 

ABC
Zap
ABC

 Exercise 6 

Hours: 45.00 
Rate: 10.00
Pay:  475.0

 Exercise 7 

>>> computegrade(0.3)
Grade: C
>>> computegrade(gg)
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    computegrade(gg)
NameError: name 'gg' is not defined
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/5th_Exercises.py ===========

 Exercise 1 

0.12749989750700297
0.8191310889088477
0.9322869381225588
0.07709181264841514
0.28126959303033483
0.040944210255621116
0.5531746923697631
0.944161040040746
0.34898998852029084
0.4175354684547966

Random int's

10
9
8
8

To choose an element from a sequence at random, you can use choice

1
2

Adding new functions

I'm a lumberjack, and I'm okay
I sleep all night and work all day
I'm a lumberjack, and I'm okay
I sleep all night and work all day
I'm a lumberjack, and I'm okay
I sleep all night and work all day

Definitions and uses
 Exercise 2 & 3


Parameters and arguments

Eric, the half a bee.
Eric, the half a bee.

Fruitful functions and void functions

8

 Exercise 5 

ABC
Zap
ABC

 Exercise 6 

Hours: 45.00 
Rate: 10.00
Pay:  475.0

 Exercise 7 

>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/5th_Exercises.py ===========

 Exercise 1 

0.7584921669871223
0.7211471018307086
0.06025722847142023
0.6159830581818185
0.0689958673302764
0.9726189236232231
0.9760410116870343
0.027375198525736
0.1868486216411952
0.2482190627762656

Random int's

9
8
10
7

To choose an element from a sequence at random, you can use choice

2
3

Adding new functions

I'm a lumberjack, and I'm okay
I sleep all night and work all day
I'm a lumberjack, and I'm okay
I sleep all night and work all day
I'm a lumberjack, and I'm okay
I sleep all night and work all day

Definitions and uses
 Exercise 2 & 3


Parameters and arguments

Eric, the half a bee.
Eric, the half a bee.

Fruitful functions and void functions

8

 Exercise 5 

ABC
Zap
ABC

 Exercise 6 

Hours: 45.00 
Rate: 10.00
Pay:  475.0

 Exercise 7 

>>> computegrade(Ogg)
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    computegrade(Ogg)
NameError: name 'Ogg' is not defined
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/5th_Exercises.py ===========

 Exercise 1 

0.9134044189025495
0.006936748625963718
0.5224005295171819
0.24734379358388459
0.5497858715739886
0.531864558012226
0.48430375220813027
0.619181773849152
0.5283574470336069
0.261073637010225

Random int's

8
8
8
7

To choose an element from a sequence at random, you can use choice

2
3

Adding new functions

I'm a lumberjack, and I'm okay
I sleep all night and work all day
I'm a lumberjack, and I'm okay
I sleep all night and work all day
I'm a lumberjack, and I'm okay
I sleep all night and work all day

Definitions and uses
 Exercise 2 & 3


Parameters and arguments

Eric, the half a bee.
Eric, the half a bee.

Fruitful functions and void functions

8

 Exercise 5 

ABC
Zap
ABC

 Exercise 6 

Hours: 45.00 
Rate: 10.00
Pay:  475.0

 Exercise 7 


=========== RESTART: /home/ren/RTR108_2020/4WEEK/5th_Exercises.py ===========

 Exercise 1 

0.4473900008350382
0.9421010082183617
0.12924064766172483
0.21410405803121513
0.25543544879597035
0.2544501977890491
0.7715149955946383
0.9994006528103891
0.7625155313834334
0.10757287040222119

Random int's

5
9
8
7

To choose an element from a sequence at random, you can use choice

2
1

Adding new functions

I'm a lumberjack, and I'm okay
I sleep all night and work all day
I'm a lumberjack, and I'm okay
I sleep all night and work all day
I'm a lumberjack, and I'm okay
I sleep all night and work all day

Definitions and uses
 Exercise 2 & 3


Parameters and arguments

Eric, the half a bee.
Eric, the half a bee.

Fruitful functions and void functions

8

 Exercise 5 

ABC
Zap
ABC

 Exercise 6 

Hours: 45.00 
Rate: 10.00
Pay:  475.0

 Exercise 7 

>>> computegrade(gg)
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    computegrade(gg)
NameError: name 'gg' is not defined
>>> computegrade(10)
>>> computegrade(0.1)
Grade: C
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/5th_Exercises.py ===========

 Exercise 1 

0.9506614892922854
0.026609042132132554
0.03181229373753747
0.20349361020863177
0.4109448057323981
0.28430681659306856
0.11642225136739104
0.4744300325009575
0.6156321667387286
0.8468504682957486

Random int's

6
6
10
6

To choose an element from a sequence at random, you can use choice

2
3

Adding new functions

I'm a lumberjack, and I'm okay
I sleep all night and work all day
I'm a lumberjack, and I'm okay
I sleep all night and work all day
I'm a lumberjack, and I'm okay
I sleep all night and work all day

Definitions and uses
 Exercise 2 & 3


Parameters and arguments

Eric, the half a bee.
Eric, the half a bee.

Fruitful functions and void functions

8

 Exercise 5 

ABC
Zap
ABC

 Exercise 6 

Hours: 45.00 
Rate: 10.00
Pay:  475.0

 Exercise 7 

>>> computegrade(10)
Bad score!
>>> computegrade(perfect)
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    computegrade(perfect)
NameError: name 'perfect' is not defined
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/5th_Exercises.py ===========

 Exercise 1 

0.060460321963656805
0.8437117949570051
0.6701970299070648
0.13868956080043227
0.44911335446828593
0.021028147853414225
0.9856761039392331
0.6589676225900813
0.7238676766898392
0.660519570417454

Random int's

6
8
7
5

To choose an element from a sequence at random, you can use choice

3
2

Adding new functions

I'm a lumberjack, and I'm okay
I sleep all night and work all day
I'm a lumberjack, and I'm okay
I sleep all night and work all day
I'm a lumberjack, and I'm okay
I sleep all night and work all day

Definitions and uses
 Exercise 2 & 3


Parameters and arguments

Eric, the half a bee.
Eric, the half a bee.

Fruitful functions and void functions

8

 Exercise 5 

ABC
Zap
ABC

 Exercise 6 

Hours: 45.00 
Rate: 10.00
Pay:  475.0

 Exercise 7 

>>> computegrade(4)
Bad score!
>>> computegrade(gg)
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    computegrade(gg)
NameError: name 'gg' is not defined
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/5th_Exercises.py ===========

 Exercise 1 

0.18663867010827617
0.621406314005678
0.1282367418881698
0.6236566447964059
0.28913218596380874
0.5725139060626768
0.5589430868805891
0.03347465695214624
0.19882277026026773
0.006993922817471354

Random int's

6
6
5
9

To choose an element from a sequence at random, you can use choice

1
1

Adding new functions

I'm a lumberjack, and I'm okay
I sleep all night and work all day
I'm a lumberjack, and I'm okay
I sleep all night and work all day
I'm a lumberjack, and I'm okay
I sleep all night and work all day

Definitions and uses
 Exercise 2 & 3


Parameters and arguments

Eric, the half a bee.
Eric, the half a bee.

Fruitful functions and void functions

8

 Exercise 5 

ABC
Zap
ABC

 Exercise 6 

Hours: 45.00 
Rate: 10.00
Pay:  475.0

 Exercise 7 

>>> computegrade(gg)
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    computegrade(gg)
NameError: name 'gg' is not defined
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/5th_Exercises.py ===========

 Exercise 1 

0.5396280225234261
0.27287216531272895
0.4513775507986011
0.06601477226497543
0.7338111763239494
0.6422519420282993
0.9333331631969799
0.5228587573012009
0.7470821468808977
0.3597186389398923

Random int's

5
7
10
9

To choose an element from a sequence at random, you can use choice

2
2

Adding new functions

I'm a lumberjack, and I'm okay
I sleep all night and work all day
I'm a lumberjack, and I'm okay
I sleep all night and work all day
I'm a lumberjack, and I'm okay
I sleep all night and work all day

Definitions and uses
 Exercise 2 & 3


Parameters and arguments

Eric, the half a bee.
Eric, the half a bee.

Fruitful functions and void functions

8

 Exercise 5 

ABC
Zap
ABC

 Exercise 6 

Hours: 45.00 
Rate: 10.00
Pay:  475.0

 Exercise 7 

>>> computegrade(gg)
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    computegrade(gg)
NameError: name 'gg' is not defined
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/5th_Exercises.py ===========

 Exercise 1 

0.8268475873375584
0.07523028039385438
0.18059833819971594
0.419003928470141
0.9482359579584977
0.2603953627853519
0.5365356807617782
0.2728293090654391
0.9055314845364255
0.7350192818595825

Random int's

8
5
5
7

To choose an element from a sequence at random, you can use choice

2
3

Adding new functions

I'm a lumberjack, and I'm okay
I sleep all night and work all day
I'm a lumberjack, and I'm okay
I sleep all night and work all day
I'm a lumberjack, and I'm okay
I sleep all night and work all day

Definitions and uses
 Exercise 2 & 3


Parameters and arguments

Eric, the half a bee.
Eric, the half a bee.

Fruitful functions and void functions

8

 Exercise 5 

ABC
Zap
ABC

 Exercise 6 

Hours: 45.00 
Rate: 10.00
Pay:  475.0

 Exercise 7 

>>> computegrade(gG)
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    computegrade(gG)
NameError: name 'gG' is not defined
>>> computegrade
<function computegrade at 0x7f75cb2de510>
>>> computegrade()
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    computegrade()
TypeError: computegrade() missing 1 required positional argument: 'score'
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/5th_Exercises.py ===========

 Exercise 1 

0.8057991056273597
0.3007906776851237
0.34314901321305935
0.036685715107762196
0.013779978751416233
0.4736882763904423
0.3083656519581137
0.7783421108770554
0.9079039020066973
0.9303239308149406

Random int's

9
5
7
9

To choose an element from a sequence at random, you can use choice

2
2

Adding new functions

I'm a lumberjack, and I'm okay
I sleep all night and work all day
I'm a lumberjack, and I'm okay
I sleep all night and work all day
I'm a lumberjack, and I'm okay
I sleep all night and work all day

Definitions and uses
 Exercise 2 & 3


Parameters and arguments

Eric, the half a bee.
Eric, the half a bee.

Fruitful functions and void functions

8

 Exercise 5 

ABC
Zap
ABC

 Exercise 6 

Hours: 45.00 
Rate: 10.00
Pay:  475.0

 Exercise 7 

>>> computegrade(g)
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    computegrade(g)
NameError: name 'g' is not defined
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/5th_Exercises.py ===========

 Exercise 1 

0.9642693274938626
0.9869225101910634
0.7993365362319084
0.2956127132765468
0.8318100398721879
0.659514696428277
0.7419691044023321
0.3726342908206586
0.23848660267277055
0.74979055591995

Random int's

8
7
7
8

To choose an element from a sequence at random, you can use choice

1
1

Adding new functions

I'm a lumberjack, and I'm okay
I sleep all night and work all day
I'm a lumberjack, and I'm okay
I sleep all night and work all day
I'm a lumberjack, and I'm okay
I sleep all night and work all day

Definitions and uses
 Exercise 2 & 3


Parameters and arguments

Eric, the half a bee.
Eric, the half a bee.

Fruitful functions and void functions

8

 Exercise 5 

ABC
Zap
ABC

 Exercise 6 

Hours: 45.00 
Rate: 10.00
Pay:  475.0

 Exercise 7 

>>> computegrade(g)
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    computegrade(g)
NameError: name 'g' is not defined
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/5th_Exercises.py ===========

 Exercise 1 

0.9597073471372227
0.0037436331307065807
0.595979997788329
0.35027184264858324
0.745924419608106
0.7510284315143727
0.11127462546611944
0.9848075524279267
0.4118518305464076
0.9913639734587412

Random int's

9
9
7
8

To choose an element from a sequence at random, you can use choice

3
2

Adding new functions

I'm a lumberjack, and I'm okay
I sleep all night and work all day
I'm a lumberjack, and I'm okay
I sleep all night and work all day
I'm a lumberjack, and I'm okay
I sleep all night and work all day

Definitions and uses
 Exercise 2 & 3


Parameters and arguments

Eric, the half a bee.
Eric, the half a bee.

Fruitful functions and void functions

8

 Exercise 5 

ABC
Zap
ABC

 Exercise 6 

Hours: 45.00 
Rate: 10.00
Pay:  475.0

 Exercise 7 

>>> computegrade(10)
Bad score!
>>> computegrade(0.2
		 )
Grade: C
>>> 
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/5th_Exercises.py ===========

 Exercise 1 

0.6675369636180516
0.03311805737073803
0.63967267857453
0.0675404362442219
0.7902531140161304
0.4102211650521991
0.9005347647840535
0.3401152856323659
0.6425539335397574
0.981797020787435

Random int's

5
8
5
6

To choose an element from a sequence at random, you can use choice

1
2

Adding new functions

I'm a lumberjack, and I'm okay
I sleep all night and work all day
I'm a lumberjack, and I'm okay
I sleep all night and work all day
I'm a lumberjack, and I'm okay
I sleep all night and work all day

Definitions and uses
 Exercise 2 & 3


Parameters and arguments

Eric, the half a bee.
Eric, the half a bee.

Fruitful functions and void functions

8

 Exercise 5 

ABC
Zap
ABC

 Exercise 6 

Hours: 45.00 
Rate: 10.00
Pay:  475.0

 Exercise 7 

>>> computegrade(gg)
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    computegrade(gg)
NameError: name 'gg' is not defined
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/5th_Exercises.py ===========

 Exercise 1 

0.6727597499159288
0.9950293380414403
0.786658288917174
0.9656944161860956
0.11134650035854943
0.8791455195204342
0.5914359324528269
0.796772848770527
0.27854444944498724
0.2935659008327325

Random int's

8
10
8
6

To choose an element from a sequence at random, you can use choice

2
2

Adding new functions

I'm a lumberjack, and I'm okay
I sleep all night and work all day
I'm a lumberjack, and I'm okay
I sleep all night and work all day
I'm a lumberjack, and I'm okay
I sleep all night and work all day

Definitions and uses
 Exercise 2 & 3


Parameters and arguments

Eric, the half a bee.
Eric, the half a bee.

Fruitful functions and void functions

8

 Exercise 5 

ABC
Zap
ABC

 Exercise 6 

Hours: 45.00 
Rate: 10.00
Pay:  475.0

 Exercise 7 

Enter a score between 0.0 and 1.0: gg
Bad input! Use numerals between 0.0 and 1.0
>>> computegrade(gg)
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    computegrade(gg)
NameError: name 'gg' is not defined
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/5th_Exercises.py ===========

 Exercise 1 

0.8118266854174674
0.8459471075264958
0.6885119081269411
0.5938384001236049
0.2609343076092866
0.34637096798741196
0.6172753942504233
0.3037815202426475
0.9592961288654765
0.166359771072756

Random int's

9
10
10
5

To choose an element from a sequence at random, you can use choice

2
3

Adding new functions

I'm a lumberjack, and I'm okay
I sleep all night and work all day
I'm a lumberjack, and I'm okay
I sleep all night and work all day
I'm a lumberjack, and I'm okay
I sleep all night and work all day

Definitions and uses
 Exercise 2 & 3


Parameters and arguments

Eric, the half a bee.
Eric, the half a bee.

Fruitful functions and void functions

8

 Exercise 5 

ABC
Zap
ABC

 Exercise 6 

Hours: 45.00 
Rate: 10.00
Pay:  475.0

 Exercise 7 

Enter a score between 0.0 and 1.0: gg
Bad input! Use numerals between 0.0 and 1.0
>>> computegrade(gg)
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    computegrade(gg)
NameError: name 'gg' is not defined
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/5th_Exercises.py ===========

 Exercise 1 

0.7379097652567234
0.32774274098249423
0.06393941246850032
0.9411785218677157
0.4931314674860131
0.5707529400356186
0.6701253000758686
0.6656549704567538
0.7918234190072386
0.7064404495950954

Random int's

5
7
8
5

To choose an element from a sequence at random, you can use choice

3
1

Adding new functions

I'm a lumberjack, and I'm okay
I sleep all night and work all day
I'm a lumberjack, and I'm okay
I sleep all night and work all day
I'm a lumberjack, and I'm okay
I sleep all night and work all day

Definitions and uses
 Exercise 2 & 3


Parameters and arguments

Eric, the half a bee.
Eric, the half a bee.

Fruitful functions and void functions

8

 Exercise 5 

ABC
Zap
ABC

 Exercise 6 

Hours: 45.00 
Rate: 10.00
Pay:  475.0

 Exercise 7 

Enter a score between 0.0 and 1.0: gg
Bad input! Use numerals between 0.0 and 1.0
>>> computegrade(gg)
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    computegrade(gg)
NameError: name 'gg' is not defined
>>> computegrade(10)
Bad score!
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/5th_Exercises.py ===========

 Exercise 1 

0.2632221738142223
0.4739705943422452
0.48051250349613284
0.3730971015516651
0.11163751164903835
0.26232040691893843
0.8789790260570473
0.3486748430224056
0.30254525544612765
0.8801748899164

Random int's

6
7
6
5

To choose an element from a sequence at random, you can use choice

3
2

Adding new functions

I'm a lumberjack, and I'm okay
I sleep all night and work all day
I'm a lumberjack, and I'm okay
I sleep all night and work all day
I'm a lumberjack, and I'm okay
I sleep all night and work all day

Definitions and uses
 Exercise 2 & 3


Parameters and arguments

Eric, the half a bee.
Eric, the half a bee.

Fruitful functions and void functions

8

 Exercise 5 

ABC
Zap
ABC

 Exercise 6 

Hours: 45.00 
Rate: 10.00
Pay:  475.0

 Exercise 7 

Enter a score between 0.0 and 1.0: 1
Bad input! Use numerals between 0.0 and 1.0
>>> computegrade(1)
Grade: A
>>> computegrade(uh)
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    computegrade(uh)
NameError: name 'uh' is not defined
>>> 
================= RESTART: /home/ren/RTR108_2020/4WEEK/uh.py =================
>>> computegrade(g)
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    computegrade(g)
NameError: name 'g' is not defined
>>> computegrade(1)
A
>>> computegrade(2)
A
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/5th_Exercises.py ===========

 Exercise 1 

0.6205899687379806
0.1204403792733254
0.49486170128804874
0.9164282616464631
0.3462004435699194
0.5537246023727567
0.6519111669734007
0.5839674827901311
0.3178590379412247
0.8620257193338363

Random int's

7
8
6
6

To choose an element from a sequence at random, you can use choice

3
2

Adding new functions

I'm a lumberjack, and I'm okay
I sleep all night and work all day
I'm a lumberjack, and I'm okay
I sleep all night and work all day
I'm a lumberjack, and I'm okay
I sleep all night and work all day

Definitions and uses
 Exercise 2 & 3


Parameters and arguments

Eric, the half a bee.
Eric, the half a bee.

Fruitful functions and void functions

8

 Exercise 5 

ABC
Zap
ABC

 Exercise 6 

Hours: 45.00 
Rate: 10.00
Pay:  475.0

 Exercise 7 

Enter a score between 0.0 and 1.0: 4
Bad score! Use numerals between 0.0 and 1.0
>>> computegrade(1)
Grade: A
>>> 
