<img src="../img/logo.jpg" width="16%" align="right">
# Classes, methods, and inheritance

<!-- <img src="../img/hash_table.png" width="50%" align="right"> -->
---
layout: false
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Class Goals

]
.right-column[
  * Dive deep into OOPs

  ]
???
How are we going to do it?

By creating awesome class definitions
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Pure functions vs Modifiers
]
.right-column[
  Take a look at this class definition:

  ```python
  class Time(object):
      """
      Represents the time of the day.

      Attributes: hour, minute, second
      """
  ```
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Pure functions vs Modifiers
]
.right-column[
  **Problems: write functions that bring about two features to any object of the `Time()` class.**

  1. `print_time`: print time in the format `HH:MM:SS`
  2. `is_after`: takes in two objects `t1` and `t2` and returns `True` if `t1` comes chronologically after `t2`
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Pure functions vs Modifiers
  ## - Pure functions
]
.right-column[
  Let's create a function, that adds two time objects and returns the sum object.

  ```python
  def add_time(t1, t2):
      sum_obj = Time()
      sum_obj.hour = t1.hour + t2.hour
      sum_obj.min = t1.min + t2.min
      sum_obj.sec = t1.sec + t2.sec
      # add some logic to check for boundary conditions like if sum_obj.min > 60, then increment hour.

      return sum_obj
  ```
  This is a **pure function** as it doesn't modify the original objects.  
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Pure functions vs Modifiers
  ## - Pure functions
]
.right-column[
  A better but longer version:

  ```python
  def add_time(t1, t2):
      sum_obj = Time()
      sum_obj.hour = t1.hour + t2.hour
      sum_obj.min = t1.min + t2.min
      sum_obj.sec = t1.sec + t2.sec

      if sum_obj.sec >= 60:
          sum_obj.sec -= 60
          sum_obj.min += 1

      if sum_obj.min >= 60:
          sum_obj.min -= 60
          sum_obj.hour += 1

      sum_obj.hour %= 24

      return sum_obj
  ```
]
???
---

<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Pure functions vs Modifiers
  ## - Pure functions
  ## - Modifiers
]
.right-column[
  Sometimes its useful to modify the incoming objects in a function.

  ```python
  def increment(time, seconds):
      # time is an object of class Time() and seconds is an integer

      time.sec += seconds

      if time.sec >= 60:
          time.sec -= 60
          time.min += 1

      if time.min >= 60:
          time.min -= 60
          time.hour += 1

      time.hour %= 24

      # NO RETURN STATEMENT

  ```
  Remember, objects are *mutable*

  Problem-1: Identify and fix the flaws in the above code.
  Problem-2: Write a pure function for increment
]
???
What happens if secodns is > 60?
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Pure functions vs Modifiers
  ## - Pure functions
  ## - Modifiers
  ## Prototyping vs Planning
  ## - Prototyping
]
.right-column[
  So far we went about creating something and as we found issues with it we fixed it.

  This can be called **Prototyping and Patching**. First create a prototype, run it and when you find it incomplete, patch it.
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Pure functions vs Modifiers
  ## - Pure functions
  ## - Modifiers
  ## Prototyping vs Planning
  ## - Prototyping
]
.right-column[
  On the other side, we can **planned development**.

  Find the best way to represent a time object before starting to code.
]
???
---

<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Pure functions vs Modifiers
  ## - Pure functions
  ## - Modifiers
  ## Prototyping vs Planning
  ## - Prototyping
]
.right-column[
  Use `sexagesamal` numeric system. How do we go about it?

  Represent time in numbers of base 60.

  ```python
  def time_to_int(t):
      minutes = t.hour*60 + t.min
      seconds = minutes * 60 + t.sec
      return seconds
  ```

]
???
---

<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Pure functions vs Modifiers
  ## - Pure functions
  ## - Modifiers
  ## Prototyping vs Planning
  ## - Prototyping
]
.right-column[
  How do we convert back the seconds to minutes and hours?

  ```python
  def int_to_time(s):
      time = Time()
      minutes, time.sec = divmod(s, 60)
      time.hour, time.min = divmod(minutes, 60)
      return time
  ```

]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Pure functions vs Modifiers
  ## - Pure functions
  ## - Modifiers
  ## Prototyping vs Planning
  ## - Prototyping
]
.right-column[
  Let's try to recreate the `add_time` function now.

  ```python
  def add_time(t1, t2):
      seconds = time_to_int(t1) + time_to_int(t2)
      return int_to_time(seconds)
  ```

  This version is shorter and easier to verify.

  See how planned development helped make things bug free and relatively fool proof?
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Methods
]
.right-column[
we saw how we wrote the print_time function that accomponies the Time class

```python
class Time(object):
    """
    Represents time

    Attr: hour, min, sec
    """

def print_time(time):
    print("{0}:{1}:{2}".format(time.hour, time.min, time.sec))
```
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Methods
]
.right-column[
Since the `print_time` function is made only for the `Time()` class, it makes more sense to bind it with it, and not keep it in a generic way we have now.

We are turning this function into a method.


```python
class Time(object):
    """
    Represents time

    Attr: hour, min, sec
    """

    def print_time(time):
        print("{0}:{1}:{2}".format(time.hour, time.min, time.sec))
```
Call the method like this.
```python
t1 = Time()
t1.hour, t1.min, t1.sec = 11, 20, 30
Time.print_time(t1)
```
]
???
---

<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Methods
]
.right-column[
A more consise way to achieve this is using the syntax"


```python
t1 = Time()
t1.hour, t1.min, t1.sec = 11, 20, 30
t1.print_time()
```
The object whose method you are calling, gets automatically passed as the first argument. So its OK and obligatory to not give the first argument when calling methods from the object.
]
???
---

<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Methods
]
.right-column[
```python
class Time(object):
    """
    Represents time

    Attr: hour, min, sec
    """

    def print_time(self):   # <<< use self
        print("{0}:{1}:{2}".format(time.hour, time.min, time.sec))
```

By convention, the first parameter of a method is called `self` as when you call the method of an object, it passes **itself** as the first arg.

Now when you call `t1.print_time`, its like saying `hey! print yourself`
]
???
---

<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Methods
]
.right-column[
Another example of methods:

```python
class Time(object):

    def print_time(self):   # <<< use self
        print("{0}:{1}:{2}".format(time.hour, time.min, time.sec))

    def increment(self, seconds):
        seconds += self.time_to_int()
        return int_to_time(seconds)

```


]
???
---

<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Methods
  ## Magic methods
  ## - `__init__`
]
.right-column[
The `__init__` method short for initialization is invoked when an object is instantiated.


```python
class Time(object):

    def __init__(self, hour=0, minute=0, second=0):
      self.hour = hour
      self.min = minute
      self.sec = second

```
That's it. From now, you can pass in arguments and assign attributes when you create an object.

```python
>>> t1 = Time(2, 3, 10)
>>> t1.print_time()
02:03:10
```
]
???
---

<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Methods
  ## Magic methods
  ## - `__init__`
]
.right-column[
The `__init__` method short for initialization is invoked when an object is instantiated.

```python
>>> t1 = Time(2)
>>> t1.print_time()
02:00:00
```
We have default arguments setup, so if less arguments are passes, the defaults kick in.
]
???
---

<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Methods
  ## Magic methods
  ## - `__init__`
  ## - `__str__`
]
.right-column[
`__str__` is a special method, like `__init__` , that is supposed to return a string representation of an object.

```python
def __str__(self):
    return "%.2d:%.2d:%.2d" % (self.hour, self.min, self.sec)
```

So now you can directly `print` Time objects:

```python
>>> print(t)
02:00:00
```
]
???
---

<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Methods
  ## Magic methods
  ## - `__init__`
  ## - `__str__`
  ## Operator overloading
]
.right-column[
You can change how basic operators like `+ - *` etc in python behaves with your class.

In the time class, you can **override** the addition op, using:

```python
def __add__(self, other):
    seconds = self.time_to_int() + other.time_to_int()
    return int_to_time(seconds)
```
]
???
---
