<img src="../img/logo.jpg" width="16%" align="right">
# Using functions with Pyprocessing
### Let's sketch some code

<img src="../img/processing_logo.png" width="40%" align="right">
---
layout: false
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Class Goals

]
.right-column[
  * What is Processing?
  * 2D Graphics Programming
]
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## What is Processing?
]
.right-column[
  Processing is an open-source computer language (Not python!) which is used
  by artists to create *sketches* using code.

  But... we aren't here to learn processing, right?

  The good news is processing has a python port. Which means we can make
  processing sketches with python. Let's dig in.
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## What is Processing?
  ## Graphics Programming
]
.right-column[
  Graphics programming is using code to manipulate visuals on a computer device.

  Its the basis of game programming.

  <img src="../img/games.png" width="100%" align="center">
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## What is Processing?
  ## Graphics Programming
  ## Installing Processing, PyProcessing and using the Editor
]
.right-column[
  Download and install Processing from https://processing.org/download/

  Next, lets activate Python-mode in Processing. Open the processing IDE (Integrated development Enviroment)

  Select *Add Mode* from the right drop down. And install the plugin.

  <img src="../img/python_mode_processing.png" width="50%" align="left">
  <img src="../img/python_mode_processing_install.png" width="50%" align="left">
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## What is Processing?
  ## Graphics Programming
  ## Installing Processing, PyProcessing and using the Editor
  ## Setup a canvas
]
.right-column[
  Let's setup a canvas to draw (code) our sketch

  ```python
  def setup():
      size(400, 400)
  ```

  Run the program. You should see a canvas!
]
???
Set the mode in processing IDE to python
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Draw on the canvas
]
.right-column[
  Use the **draw** function to draw a rectangle on the canvas

  ```python
  def draw():
      rect(0, 0, 50, 100)
  ```
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Draw on the canvas
  ## Coordinate geometry sneek-peek
]
.right-column[
  ref: http://py.processing.org/tutorials/drawing/

  **Coordinate space**

  On a graph sheet we can join two **points** with the shortest distance using a **line**

  <img src="../img/graph_paper.jpg" width="80%" align="center">

  In processing we can use the function **line()** to draw a line on the canvas.
  Try:

  ```python
  line(10, 20, 200, 300)
  ```
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Draw on the canvas
  ## Coordinate geometry sneek-peek
]
.right-column[
  ref: http://py.processing.org/tutorials/drawing/

  **Coordinate space**

  The key here is to realize that the computer screen is nothing more than a fancier piece of graph paper. Each pixel of the screen is a coordinate - two numbers, an "x" (horizontal) and a "y" (vertical) - that determines the location of a point in space. And it is our job to specify what shapes and colors should appear at these pixel coordinates.

  <img src="../img/graph_paper_quadrant.jpg" width="80%" align="center">
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Draw on the canvas
  ## Coordinate geometry sneek-peek
  ## Basic shapes
]
.right-column[
  Four basic shapes:
  * point
  * line
  * rectangle
  * ellipse

  think about what are the information we need to represent each of these shapes on a graph sheet.
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Draw on the canvas
  ## Coordinate geometry sneek-peek
  ## Basic shapes
]
.right-column[
  ```python
  # point(x, y)
  point(2, 20)
  ```
  A **line** can be described using 2 set of coordinates on a graph sheet.

  ```python
  line(x1, y1, x2, y2)
  ```
  A **rectangle** can be properly described in many ways. For example, we can define a top
  left corner coordinates and then describe the length and breath of the rectangle.
  ```python
  # rectangle described from the
  # CORNER (top-left)
  rect(x, y, width, height)
  ```

]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Draw on the canvas
  ## Coordinate geometry sneek-peek
  ## Basic shapes
]
.right-column[
  A **rectangle** can also be described by specifying a center point (x, y) and
  then specify a height, width. This can be used by first switching the `rect` funciton
  to use CENTER from the default CORNER mode.
  ```python
  # rectangle described from the
  # CENTER
  rectMode(CENTER)
  rect(x, y, width, height)
  ```
  You can also describe it using two corners, therefore the CORNERS mode.
  ```python
  rectMode(CORNERS)
  rect(x1, y1, x2, y2)
  ```
  The last mode is kinda a tweak over the CENTER mode. This one uses the center point
  and a X radius, Y radius to describe the rectangle
  ```python
  rectMode(RADIUS)
  rect(x, y, x_radius, y_radius)
  ```
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Draw on the canvas
  ## Coordinate geometry sneek-peek
  ## Basic shapes
]
.right-column[
  Problem-1:

  *Design a 4x4 checker board (smaller chess board)*
  ]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Draw on the canvas
  ## Coordinate geometry sneek-peek
  ## Basic shapes
  ## Colors
]
.right-column[
  If you want a color on screen Its not enough to say stuff like "I want a greenish orange color"

  Color is defined by a range of numbers. The simplest case is grayscale.

  Grayscale is defined by a range of numbers from 0 to 255, 0 represents black,
  255 represents white.

  <img src="../img/grayscale.jpg" width="100%" align="center">

  Why 0 to 255, why not 0 to 164 or something??!
  ]
???
Computer saves information in memory. A memory is a sequence of 1s and 0s, each
bit has 2 options, and a byte of memory is made of 8 bits, so we can save a total
of 2**8 combinations, which is 256. So 256 unique values, 256 colors in grayscale.

If you save colors in 16-bit memory, you can have more resolution in your colors.
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Draw on the canvas
  ## Coordinate geometry sneek-peek
  ## Basic shapes
  ## Colors
]
.right-column[
  Let paint the background *white*

  use
  ```python
  background(255)  
  ```
  Now update problem-1 with a black background
  ]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Draw on the canvas
  ## Coordinate geometry sneek-peek
  ## Basic shapes
  ## Colors
]
.right-column[
  use `fill()` to set the bucket fill color of any shapes drawing
  If you want a transparent filling into your shapes, use `noFill()` (case sensitive)

  If you want to set the stroke color, use `stroke()`
  If you do not want a border to your shapes, remove it using `noStroke()`

  If you use both `noStroke()` and `noFill()` together, nothing will appear on
  screen, duh!
  ]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Draw on the canvas
  ## Coordinate geometry sneek-peek
  ## Basic shapes
  ## Colors
]
.right-column[
  use `fill()` to set the bucket fill color of any shapes drawing
  If you want a transparent filling into your shapes, use `noFill()` (case sensitive)

  If you want to set the stroke color, use `stroke()`
  If you do not want a border to your shapes, remove it using `noStroke()`

  If you use both `noStroke()` and `noFill()` together, nothing will appear on
  screen, duh!
  ]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Draw on the canvas
  ## Coordinate geometry sneek-peek
  ## Basic shapes
  ## Colors
]
.right-column[
  To make colorful colors, we need to understand RGB.

  In painting if we add primary colors together you get black. But computer
  graphics works like light. If you mix the primary light colors you get white.

  We need to mix just three colors in right proportions to get any color we can see.
  (that's because we have only 3 kinds of color sensitive cells in our eyes. There are more colors we can't see. ;) )
  ]
???
---

<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Draw on the canvas
  ## Coordinate geometry sneek-peek
  ## Basic shapes
  ## Colors
]
.right-column[
  Just like black to white can be represented with one byte of information (remember 0 to 255?)

  We can represent a "RGB" color with 3 bytes of information. That is one byte allotted
  to Red, Green and Blue each.

  By coming up with a right ratio for each of the 3 colors, we can put (almost) any color on screen.

  Try:
  ```python
  background(255, 255, 0)    # Red + Green = Yellow
  ```
  ]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Draw on the canvas
  ## Coordinate geometry sneek-peek
  ## Basic shapes
  ## Colors
]
.right-column[
  In addition to RGB colors, we can set the transparency of the color.

  This helps us visualize two objects overlapped on each other simultaneously.

  transparency takes another byte. Its also called the Alpha channel. So a color
  represented this way is called a RGBA color.

  Try:
  ```python
    noStroke()
    fill(0, 255, 255)    # cyan
    rectMode(CENTER)
    rect(width // 2, height // 2, 100, 100)    # 100x100 rect from center of canvas
    fill(255, 255, 0, 128)     # Yellow with 50 % transparency
    ellipse(width // 2 - 50, height // 2, 100, 100)    # circle inside 100x100 rect left of center of canvas
  ```
  ]
???
---

<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Draw on the canvas
  ## Coordinate geometry sneek-peek
  ## Basic shapes
  ## Colors
]
.right-column[
  Problem-2

  I need a color pallete image for my course. Something like this below
  <img src="../img/rgb.jpg" width="50%" align="center"> It need not make the white color in the center though. (it wont!)

  Specs:
  Canvas size: 400px x 400px
  circle size: 100px radius

  Go nuts.  
  ]
???
---

<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Draw on the canvas
  ## Coordinate geometry sneek-peek
  ## Basic shapes
  ## Colors
  ## Functions and Docstring
]
.right-column[
  As you can see, we deal with functions mostly in pyprocessing.

  There is a great way in python to add documentation to functions. This makes
  the reader understand what this function does.

  For example:

  ```python
  def doc():
    """
    This is a doc string. Using three double or single quotes to open or close a Docstring
    This function is used to illustrate the beauty that is a doc string.
    You can specify what the inputs to this function are, and what the outputs are.
    Make sure to write about what this function does here.
    """
    return "You are Awesome!"
  ```

  Try calling the function, and it should work as it would without a **Docstring**.
  ]
???
---

<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Draw on the canvas
  ## Coordinate geometry sneek-peek
  ## Basic shapes
  ## Colors
  ## Functions and Docstring
]
.right-column[
  Some more Docstring examples:

  ```python
  def setup():
    """
    Setup your program here. This function is executed first before any other
    user logic, by processing.

    By overriding the setup() fn you can initialize the canvas, set default
    options like noStroke() or fill() or any background shapes.
    """
    pass
  ```
  ```python
  def draw():
    """
    Draw is called before every frame is rendered on screen.

    By overriding the draw() fn you can update the canvas and animate any
    object over each frame.
    """
    pass
  ```
  ]
???
---
