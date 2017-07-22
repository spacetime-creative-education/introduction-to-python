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
