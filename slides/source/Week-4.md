<img src="../img/logo.jpg" width="16%" align="right">
# Iteration and Strings

> “Did you hear about that new branded MegaSuperComputer? It returns from an infinite loop just on 6 seconds!” :D

<img src="../img/loop_flowchart.png" width="50%" align="right">
---
layout: false
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Class Goals

]
.right-column[
  * Iteration
  * Strings
]
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Iteration
  ## - Multiple Assignment
]
.right-column[
  Through the life cycle of a program, we can assign Multiple values to a variable.
  Its legal to do that. That's why its called a variable, otherwise its called a constant.

  ```python
  bruce = 5
  print(bruce)
  bruce = 7
  print(bruce)
  ```
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Iteration
  ## - Multiple Assignment
  ## - identifiers
]
.right-column[
  In Python, a "name" or "identifier" is like a parcel tag (or nametag) attached to an object.

  ```python
  a = 1
  ```
  ![a1tag](../img/a1tag.png)

  Here, an integer 1 object has a tag labelled "a".
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Iteration
  ## - Multiple Assignment
  ## - identifiers
]
.right-column[
  If we reassign to "a", we just move the tag to another object:

  ```python
  a = 2
  ```
  ![a2tag](../img/a2tag.png)

  Now the name "a" is attached to an integer 2 object.

  The original integer 1 object no longer has a tag "a". It may live on, but we can't get to it through the name "a". (When an object has no more references or tags, it is removed from memory.)
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Iteration
  ## - Multiple Assignment
  ## - identifiers
]
.right-column[
  If we assign one name to another, we're just attaching another nametag to an existing object:

  ```python
  b = a
  ```
  ![ab2tag](../img/ab2tag.png)

  The name "b" is just a second tag bound to the same object as "a".

  Try changing the value of `a`, say `a=10`. Now check what `b` is.

  Is it behaving the way you expected? Is it counter intuitive?
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Iteration
  ## - Multiple Assignment
  ## - identifiers
]
.right-column[
  Although we commonly refer to "variables" even in Python (because it's common terminology), we really mean "names" or "identifiers". In Python, "variables" are nametags for values, not labelled boxes.

  Variables are not containers as we saw earlier in this course. That was cheating!
  variables are actually tags, just names in python.
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Iteration
  ## - Multiple Assignment
  ## - identifiers
  ## - Updating variables
]
.right-column[
  A common form of multiple assignment is **update**.

  ```python
  x = x + 1
  ```
  Gets the current value of `x` and updates it (increments).

  ```python
  >>> x = x + 1
  NameError: name 'x' is not defined
  >>> x = 0
  >>> x = x + 1
  >>> x
  1
  ```
  `x = x - 1` is called decrementing.
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Iteration
  ## - Multiple Assignment
  ## - identifiers
  ## - Updating variables
  ## - While Loop
]
.right-column[
  Get ready to blow your mind. *Breaking knuckles*

  Computers are cool, because it can repeat doing stuff 1000s of time without frowning.

  ```python
  def countdown(n):
      while n > 0:
          print(n)
          n = n - 1    # decrement by 1
      print 'Blastoff!'
  ```
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Iteration
  ## - Multiple Assignment
  ## - identifiers
  ## - Updating variables
  ## - While Loop
]
.right-column[
  `while` consume a boolean and if the boolean is `True` it executes the block written underneath it.

  You can generate this boolean using conditionals.

  ```python
  while Condition:
      # write your code here
  ```
]
???
---

<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Iteration
  ## - Multiple Assignment
  ## - identifiers
  ## - Updating variables
  ## - While Loop
]
.right-column[
  `while` consume a boolean and if the boolean is `True` it executes the block written underneath it.

  You can generate this boolean using conditionals.

  ```python
  while Condition:
      # write your code here
  ```
  ![loop_flowchart](../img/loop_flowchart.png)
  This type of flow is called a **loop**
]
???
---

<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Iteration
  ## - Multiple Assignment
  ## - identifiers
  ## - Updating variables
  ## - While Loop
]
.right-column[
  The body of the loop should change the value of variables and eventually the
  conditionals consumed by while header turns False, and the loop ends.

  If the conditionals will never turn False, the loop never ends and runs eternally.

  These loops are called **infinite loops**

  ```python
  print("May I have your attention please?\nWill the real Slim Shady")
  while True:
      print("Please stand up")
  ```

  When will this loop stop executing?
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Iteration
  ## - Multiple Assignment
  ## - identifiers
  ## - Updating variables
  ## - While Loop
]
.right-column[
  Let's look at a more complex loop.

  ```python
  def sequence(n):
      while n != 1:
          print(n)
          if n%2 == 0:
              n = n/2
          else:
              n = n*3+1
  ```
  In the last loop, we can easily prove when the loop will terminate. If we start with n = 5, on each **iteration** n decrements and the loop terminates in 5 iterations.

  This one is more complex, right? This is called *Collatz conjecture* and will eventually terminate for all positive integers.
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Iteration
  ## - Multiple Assignment
  ## - identifiers
  ## - Updating variables
  ## - While Loop
  ## - break
]
.right-column[
  There is a handy way to break out of the loop.

  ```python
  def sequence(n):
      while True:
        line = raw_input('>>>')
        if line == 'exit()':
            break
        print(eval(line))
  ```
  Remember, the python console (`>>> `) is a loop, and to break out of it you can use `>>> exit()`. So there you go a working example of `while` loop and `break`.
]
???
---

<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Iteration
  ## - for
]
.right-column[
  Another way to execute a code block N times is using the `for` statement. A basic example of `for` in python goes like this:

  ```python
  # counter.py
  for i in range(1, 11):
      print(i)
  ```
  Here `range` creates a sequence of numbers from 1 to 10 (11 is excluded).
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Iteration
  ## - for
]
.right-column[
  Let's build a launch counter for spaceX.

  ```python
  # launch_counter.py
  for i in range(10, -1, -1):
      print(i)
  else:
      print("Blastoff!")
  ```
  Let's see the important pieces of this code in detail
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Iteration
  ## - for
]
.right-column[
  ```python
  # launch_counter.py
  for i in range(10, -1, -1):
      ...
  ```
  `range(10, -1, -1)` counts from 10 to 0, decrementing by 1 per iteration.
  range consumes 3 parameters, `start`, `end` and `step`. The default `start` is `0` and the default `step` is `1`.
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Iteration
  ## - for
]
.right-column[
  ```python
  # launch_counter.py
  for i in range(10, -1, -1):
      print(i)
  else:
      print("Blastoff!")
  ```
  What is `else` doing with for? Here the `else` block is executed only if the `for` block executes successfully. Let's say for some reason the launch is called off during the countdown, then the else won't be executed.
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Iteration
  ## - for
]
.right-column[
  ```python
  # launch_counter.py
  import random
  for i in range(10, -1, -1):
      print(i)
      if random.randint(0, 5) == 0:    # 1 in 6 chances of launch cancellation
          print("Launch cancelled")
          break    # yes, break can be used in for loops also
  else:
      print("Blastoff!")
  ```
]
???
---

<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Iteration
  ## - for
]
.right-column[
  How would we have achieved the above logic without the else block?

  To do that you might need a flag variable.
  ```python
  # launch_counter.py
  import random
  cancelled = False
  for i in range(10, -1, -1):
      print(i)
      if random.randint(0, 5) == 0:    # 1 in 6 chances of launch cancellation
          print("Launch cancelled")
          cancelled = True
          break    # yes, break can be used in for loops also

  if not cancelled:
      print("Blastoff!")
  ```
  Python developers are like, why one more variable? I hate that.
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## String
]
.right-column[
  So far we have seen how to use string and manipulate them using in-built methods.
  Remember `"hello".capitalize()`, `"hello".upper()` etc?

  Unlike other scalar types (`int`, `bool`) `str` can be broken and dealt with in pieces.

  You can access each character in a string and work with it.
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## String
]
.right-column[
  So far we have seen how to use string and manipulate them using in-built methods.
  Remember `"hello".capitalize()`, `"hello".upper()` etc?

  Unlike other scalar types (`int`, `bool`) `str` can be broken and dealt with in pieces.

  You can access each character in a string and work with it.
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## String
]
.right-column[
  String is a sequence of characters. You can access characters one at a time using the rectangular bracket operator.

  ```python
  fruit = "banana"
  letter = fruit[0]
  print(letter)    # prints the first letter of the string.
  ```
  The expression in the bracket is called `index`.
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## String
]
.right-column[
  The `index` of a string must always be integers.

  ```python
  fruit = "banana"
  letter = fruit[1.5]    # <<< Raises TypeError
  print(letter)    # prints the first letter of the string.
  ```
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## String
  ## - len()
]
.right-column[
  You can use `len()` function to find the length of a string.

  ```python
  >>> print(len("banana"))
  6
  ```
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## String
  ## - len()
]
.right-column[
  To access the last character of a string you can do:

  ```python
  fruit = "banana"
  length = len(fruit)
  last = fruit[length]
  last_but_one = fruit[length - 1]
  ```
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## String
  ## - len()
  ## - Traverse with `for`
]
.right-column[
  `for` loop unlike `while`, consumes a sequence and processes the elements in the sequence one-by-one.
  This pattern of processing is called **traversal**
  ```python
  for char in fruit:
      print(char)
  ```
  Prints all characters in the string.
]
???
---

<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## String
  ## - len()
  ## - Traverse with `for`
]
.right-column[
  **Problem-1**

  Find how you can traverse and print characters in a string using `while`

]
???
index = 0
while index < len(fruit):
  letter = fruit[index]
  print(letter)
  index = index + 1
---

<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## String
  ## - len()
  ## - Traverse with `for`
]
.right-column[
  **Problem-2**

  Write a function, that consumes a string and prints it backwards

]
???
index = 0
length = len(fruit)
output = ""
while index < length:
  letter = fruit[length - index]
  output += letter
  index = index + 1
print(output)
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## String
  ## - len()
  ## - Traverse with `for`
  ## - Slicing
]
.right-column[
A segment of a string is called a **slice**.

```python
>>> s = "Monty Python"
>>> print(s[0:5])
Monty
```
Two simple and important things to note:
1. python counts from 0
2. When you give a range, the end of range is excluded
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## String
  ## - len()
  ## - Traverse with `for`
  ## - Slicing
]
.right-column[
A segment of a string is called a **slice**.

```python
>>> s = "Monty Python"
>>> print(s[0:5])
Monty
```
Two simple and important things to note:
1. python counts from 0
2. When you give a range, the end of range is excluded

The operator [n:m] returns the part of the string from the “n-eth” character to the “m-eth”
character, including the first but excluding the last.
]
???
---
