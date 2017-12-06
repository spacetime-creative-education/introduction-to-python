<img src="../img/logo.jpg" width="16%" align="right">
# Functions
### Worksheet - 1

<img src="../img/function_machines_composed.png" width="50%" align="right">
---
layout: false
<img src="../img/logo.jpg" width="16%" align="right">

.right-column[
**MouseX, MouseY**

Processing autoupdates the mouse pointer locations to the variables `MouseX`, `MouseY`.

Just like the predefined variables `displayWidth`, `displayHeight`, `width`, `height`
Use these to make your program more versatile .

]
---
layout: false
<img src="../img/logo.jpg" width="16%" align="right">

.right-column[
**Problem-1**

_level: easy_

*Draw a circle that follows the cursor on the canvas*

```
Spec:

canvas size: 400x600px
circle diameter: 100px
```
---
layout: false
<img src="../img/logo.jpg" width="16%" align="right">

.right-column[
We saw RGB color model last class and we know how we can get colors using R,G,B channels.

There are many other color models and one other popular one is HSB.

HSB stands for Hue, Saturation and Brightness. It is visualized as a circle (color wheel), with the color placed in 0 to 360degs, Saturation from 0 to 100 says how saturated the color is, and Brightness with values 0 to 100, denotes how bright the color is. Just like RGB, any color that can be produced by this computer screen by be denoted using HSB as well.
---
layout: false
<img src="../img/logo.jpg" width="16%" align="right">

.right-column[
To use HSB color mode in processing, use

```
# add this line to setup() or before using this mode in draw()
colorMode(HSB, 360, 100, 100);    # the args 2,3,4 denotes the range we assign to H,S,B channels.
```
---
layout: false
<img src="../img/logo.jpg" width="16%" align="right">

.right-column[
**Problem-1B**

_level: intermediate_

*Draw a circle that follows the cursor on the canvas. Fill the circle with color.*

```
Spec:

canvas size: 400x600px
circle diameter: 100px
color range:
  1. H should vary from 0 to 360 for mouseX varying from leftmost to rightmost part of canvas
  2. Brightness should vary from 0 to 100 for mouseY varying from topmost to bottommost part of canvas.
```
---
layout: false
<img src="../img/logo.jpg" width="16%" align="right">

.right-column[
**Problem-2**

_level: easy_

*Print the following message*

  ```
  One of Python's strengths is its diverse community.
  ```
]
---
layout: false
<img src="../img/logo.jpg" width="16%" align="right">

.right-column[
**Problem-3**

_level: easy_

*Get firstname and lastname of an user. And print Hello {fullname}*

*Example run:*

  ```
  Enter firstname: prashanth
  Enter lastname: gandhiraj
  Hello, Prashanth Gandhiraj
  ```
]
???
hint: use fullname.title() method
---
layout: false
<img src="../img/logo.jpg" width="16%" align="right">

.right-column[
**Problem-4**

_level: intermediate_

*Phone number validation:*

*Ask user to input a phone number. Store it in the variable `phonenumber`*

*Check if all the characters in that variaable is a number.*

*Print, The user entered a number: True/False*

*Example run:*

  ```
  What is your phone number?: 9790744316
  The user entered a number: True
  ```
]
???
hint: use phonenumber.isnumeric() method
---
layout: false
<img src="../img/logo.jpg" width="16%" align="right">

.right-column[
**Problem-5**

_level: easy_

*Length of the string*

*Take any string. Find the length, as in the number of characters in that string*

*Example run:*

  ```
  String: Hey there
  Length: 9
  ```
]
???
hint: use len() fn

---
layout: false
<img src="../img/logo.jpg" width="16%" align="right">

.right-column[
**Eval()**

`eval()` can consume a string and evaluate it like a python expression.

```
eval("2+3*5")    # note the double quotes in the argument (its a F*in string! :P)
17
```
]
---
layout: false
<img src="../img/logo.jpg" width="16%" align="right">

.right-column[
**Problem-6**

_level: intermediate_

*User calculator*

*Make a program, that when run will ask the user to enter any valid python expression and return back the results to the user*
]
---
layout: false
<img src="../img/logo.jpg" width="16%" align="right">

.right-column[
**Problem-7**

_level: intermediate_

*Even or odd*

*Make a program that asks user for a number, and if the number is even, prints True, otherwise prints False*

*Example run:*

  ```
  Number to check if even: 23
  False
  ```
]
---
layout: false
<img src="../img/logo.jpg" width="16%" align="right">

.right-column[
**Problem-7**

*Functions you know so far*

  ```
  print()
  input()
  help()
  len()
  eval()
  int()
  str()
  bool()
  %
  ```
]
