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
]
---
layout: false
<img src="../img/logo.jpg" width="16%" align="right">

.right-column[
To use HSB color mode in processing, use

```
# add this line to setup() or before using this mode in draw()
colorMode(HSB, 360, 100, 100);    # the args 2,3,4 denotes the range we assign to H,S,B channels.
```
]
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
]
---
layout: false
<img src="../img/logo.jpg" width="16%" align="right">

.right-column[
**Problem-2**

_level: intermediate_

*Make the cursor act like a pencil tool in MS-Paint*
]
---
layout: false
<img src="../img/logo.jpg" width="16%" align="right">

.right-column[
**Problem-3**

_level: intermediate_

*Make a rainbow canvas animation, like one below:*

<iframe src="https://giphy.com/embed/SBi6eBtWMUvnO" width="480" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/animation-rainbow-colorful-SBi6eBtWMUvnO">via GIPHY</a></p>

*Hint: Use create a sine wave using python.*

]
???
---
layout: false
<img src="../img/logo.jpg" width="16%" align="right">

.right-column[
**Problem-4**

_level: hard_

*Draw a square of size 50x50px at the center of 400x400px canvas.
Rotate the square in such a way that if the mouse is moved quickly from left to right,
or right to left, the square rotates quickly in clockwise or anti-clockwise respectively.
If the mouse movement is slow, the square rotates slowly.
In short, do physics programming, mapping linear motion to circular motion.
*

*Hint: Go the processing docs and find appropriate functions and variables*

]
???
