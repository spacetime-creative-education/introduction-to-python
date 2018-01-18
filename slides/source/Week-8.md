<img src="../img/logo.jpg" width="16%" align="right">
# Classes, Objects and more Functions

<!-- <img src="../img/hash_table.png" width="50%" align="right"> -->
---
layout: false
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Class Goals

]
.right-column[
  * Figure out what object oriented programming is and how to do it

  ]
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## User defined datatypes
]
.right-column[
  Remember:

  * A major component of programming is **Abstraction**
  * All programs does just one thing: **Convert one data into another**
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## User defined datatypes
]
.right-column[
  Let's build programs that handles the backend of graphics. The requirement is to make a software that understands 2D geometry. This means we need to tell the computer how to interpret geometric elements like:

  * points
  * rectangles
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## User defined datatypes
  ## - Point
]
.right-column[
  A point has 2 coordinates. We could use python datatypes to store and manipulate this information.
  Say

  ```python
  p = {'x': 2, 'y': 4}    # A point in 2d space
  ```
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## User defined datatypes
  ## - Point
]
.right-column[
  As convinent as the `dict` looks, we can actually make better representation of this data.
  We only have one use case here, handling graphics. So its a better thing to go for a better representation of the data.

  Python datatypes are generic datatypes that work everywhere. What we want is a specific datatypes that only works in our system.

  Introducting User defined datatypes, AKA classes

  ```python
  class Point(object):
      """Represnts a point in 2D space"""
  ```
]
???
---

<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## User defined datatypes
  ## - Point
]
.right-column[
  ```python
  class Point(object):
      """Represnts a point in 2D space"""
  ```
  ^^This above is the class definition. Think of it like a function definition.

  The word `object` there passed to it just tells python that we are going to create customized objects. So treat it like you treat any other python object.
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## User defined datatypes
  ## - Point
]
.right-column[
  ```python
  class Point(object):
      """Represnts a point in 2D space"""
  ```
  ^^This above is the class definition. Think of it like a function definition.

  The word `object` there passed to it just tells python that we are going to create customized objects. So treat it like you treat any other python object.
<!--
  Remember:
  In python all data are objects.

  ```python
  >>> print(Point)
  <class '__main__.Point'>    # the class object
  ``` -->
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## User defined datatypes
  ## - Point
]
.right-column[
  Just like functions, when you call it, you execute it.

  Here when we call `Point` you create an instance of the class.

  ```python
  p = Point()    # p is a point object
  ```

  We are going to add more code to the class so that the intance can be manipulated easily and can be used to do the graphics processing.

  (it should work more or less like the point class in py.processing does)
]
???
---

<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## User defined datatypes
  ## - Point
  ## Attributes
]
.right-column[
  You can assign values to an instance using dot notation:

  ```python
  p = Point()    # p is a point object
  p.x = 3
  p.y = 4
  ```

  This is similar to `math.pi` syntax
]
???
---

<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## User defined datatypes
  ## - Point
  ## Attributes
]
.right-column[
  You can assign values to an instance using dot notation:

  ```python
  >>> p = Point()    # p is a point object
  >>> p.x = 3
  >>> p.y = 4
]
```
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## User defined datatypes
  ## - Point
  ## Attributes
]
.right-column[
  You can read the attributes using the dot notation as well

  ```python
  >>> p = Point()    # p is a point object
  >>> p.x = 3
  >>> p.y = 4
  >>> print(p.x)    # Reading the attribute
  3.0
  ```

  This is similar to `math.pi` syntax.
]
???
---

<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## User defined datatypes
  ## - Point
  ## Attributes
  ## - Rectangle
]
.right-column[
  A rectangle could be drawn in many ways. What we are interested in is finding out all the pieces of information needed for it to be drawn.

  Some possibilities are:

  * You could specify one corner of the rectangle (or the center), the width, and the
height.
  * You could specify two opposing corners.

  Without evaluating which is a better way to go, lets implement the first one.
]
???
---

<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## User defined datatypes
  ## - Point
  ## Attributes
  ## - Rectangle
]
.right-column[
  ```py
  class Rectangle(object):
    """Represents a rectangle.
       attributes: width, height, corner.
    """
```
We need to add relevant code to the above template. Before that...
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## User defined datatypes
  ## - Point
  ## Attributes
  ## - Rectangle
]
.right-column[
  Lets create an instance of this class and assign some attributes.

  ```py
  box = Rectangle()
  box.width = 20
  box.height = 40
  ```

]
???
---
We need to add relevant code to the above template. Before that...
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## User defined datatypes
  ## - Point
  ## Attributes
  ## - Rectangle
]
.right-column[
  To actually be able to drawn, we need atleast a 3rd piece of information. Let's use the `top-left` corner for the absolute position in space.

  ```py
  box = Rectangle()
  box.width = 20
  box.height = 40

  box.corner = Point()
  box.corner.x = 0
  box.corner.y = 50
  ```
]
???
---

<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## User defined datatypes
  ## - Point
  ## Attributes
  ## - Rectangle
]
.right-column[
After defining these classes, we can handle these data easier. Lets use some functions to process them.

Lets create a function that finds the center of the rectangle, given all the above info we fed it.

```py
def find_center(rect):
    p = Point()
    p.x = rect.corner.x + rect.width/2.0
    p.y = rect.corner.y + rect.height/2.0
    return p
```
example usage:
```py
>>> center = find_center(box)
>>> print_point(center)
(50.0, 100.0)
```
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## User defined datatypes
  ## - Point
  ## Attributes
  ## - Rectangle
]
.right-column[
Objects are mutable

You can change the state of an object by making an assignment to one of its attributes. For
example, to change the size of a rectangle without changing its position, you can modify
the values of width and height

```py
  box.width = box.width + 50
  box.height = box.width + 100
```

You can also write functions that modify objects.

```py
def grow_rectangle(rect, dwidth, dheight):
  rect.width += dwidth
  rect.height += dheight
```
]
???
---

<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## User defined datatypes
  ## - Point
  ## Attributes
  ## - Rectangle
  ## Debugging
]
.right-column[
When you start working with objects, you are likely to encounter some new exceptions. If
you try to access an attribute that doesn’t exist, you get an `AttributeError`:

```
  >>> p = Point()
  >>> print p.z
  AttributeError: Point instance has no attribute 'z'
```
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## User defined datatypes
  ## - Point
  ## Attributes
  ## - Rectangle
  ## Debugging
]
.right-column[
If you are not sure whether an object has a particular attribute, you can use the built-in
function `hasattr`:
```
  >>> hasattr(p, 'x')
  True
  >>> hasattr(p, 'z')
  False
```
]
???
---
