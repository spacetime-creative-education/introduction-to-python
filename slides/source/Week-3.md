<img src="../img/logo.jpg" width="16%" align="right">
# Conditionals, Recursion and a little bit of Iteration
### Lather, rinse, repeat

---
layout: false
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Class Goals

]
.right-column[
  * Conditionals
    * Boolean Operators
    * Debugging


  * Recursion
    * Debugging

  * Iteration
]
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Conditionals
]
.right-column[
  When you want your programs to make choices, you need to write Conditional statements.

  Like in a game when you press the right arrow key (say) and your game software
  turns the player right, thats based on conditional statements.
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Conditionals
  ## - Boolean Operators
]
.right-column[
  You have a pet robot and you need to program it to take some simple choices.
  You want it to use an umbrella when it is raining, and
  put on sunglasses when it is sunny. To do this you can use the `if` keyword

  ```python
  rain = True    # set the variable rain with a bool data
  if rain:       # `if` is a code block, just like `def`
      print("Opening umbrella")    # beware of the indent
  ```
  ```python
  sunny = True
  if sunny:     # Reminder: A colon marks the opening of a code blocl
      print("Putting on sunglasses")
  ```
]
???
Try setting rain = False and running your program. It wouldn't print anything
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Conditionals
  ## - Boolean Operators
]
.right-column[
  An `if` block consumes `True` or `False` values and optionally executes a code block.

  Sometimes we might want the program to compute the bool to be True or False.
  Just like math operators, we need Boolean operators to do that.

  Try:
  ```python
  >>> 5 == 5
  >>> 6 == 5
  >>> type(True)
  >>> type(False)
  <class 'bool'>
  ```
  These are called **Boolean expressions** that is either True or False. The
  operator here is `==` which finds if the values on its two sides are equal.
]
???
Executes a code block under a if when the bool is True.
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Conditionals
  ## - Boolean Operators
]
.right-column[
  **Relational operators**

  If you want to know the relationship between two values, you can use Relational
  operators.

  ```python
  >>> x != y    # x is not equal to y
  >>> x > y     # x is greater than y
  >>> x < y     # x is less than y
  >>> x >= y    # x is greater than or equal to y
  >>> x <= y    # x is less than or equal to y
  ```
]
???

---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Conditionals
  ## - Boolean Operators
]
.right-column[
  **Modulas Operator**

  There is one math operator that we didn't see in detail. The modulus operator
  finds the reminder after division of 2 integers.

  For example
  ```python
  >>> 5 % 3
  2
  >>> 5 % 2
  1
  ```

  This is sometimes very useful when writing Conditionals.

  *How would you find the reminder of division of two integers, if you weren'- [ ]
  introduced to modulus operator?*
]
???

---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Conditionals
  ## - Boolean Operators
]
.right-column[
  **Logical operators**

  There are three logical operators `and`, `or` and `not`. The Semantics of these
  operators are similar to their meaiing in English.

  ```python
  n % 2 == 0 or n % 3 == 0    # if True, then n is divisible by both 2 and 3
  ```
]
???

---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Conditionals
  ## - Boolean Operators
]
.right-column[
  Guess if a coin toss will yield Heads or Tails.

  ```python
  import random
  toss = random.randint(1, 2)    # generate integers in range 1 to 2
  user_input = input("Heads ('h') or Tails ('t')")

  if user_input == 'h' and toss == 1:
      print("Right, its a head")

  if user_input == 't' and toss == 2:
      print("Right, its a tail")

  if user_input == 'h' and toss != 1:
      print("Bad luck")

  if user_input == 't' and toss != 2:
      print("Bad luck")
  ```
  ]
???

---

<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Conditionals
  ## - Boolean Operators
]
.right-column[
  **Conditional Execution**

  We know that the statements in a `if` block is executed only if the `if` consumes a `True`.
  This is called conditional execution. Execute some code only when a condition is met.

  ```python
  if x > 0:
      print("x is a positive integer")
  ```
]
???

---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Conditionals
  ## - Boolean Operators
]
.right-column[
  **Alternate Execution**

  When we need to execute a block of code when a condition fails, we can use the `else` keyword

  ```python
  if x % 2 == 0:
      print("x is an even integer")
  else:
      print("x is an odd integer")
  ```
  This is really close to how we say conditions in English.
]
???

---

<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Conditionals
  ## - Boolean Operators
]
.right-column[
  **Chained Conditionals**

  When there are more than two posibilities, we need more than 2 **branches**

  ```python
  if x > 0:
      print("x is a positive integer")
  elif x < 0:
      print("x is a negative integer")
  else:
      print("x is zero")
  ```
]
???

---

<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Conditionals
  ## - Boolean Operators
]
.right-column[
  **Nested Conditionals**

  writing if-else inside if-else. You can go as deep as you would like, but always remember
  "Flat is better than nested"

  ```python
  if x > 0:
      print("x is a positive integer")
  else:
      if x < 0:
          print("x is a negative integer")
      else:
          print("x is zero")
  ```
]
???

---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Conditionals
  ## - Boolean Operators
  ## Recursion
]
.right-column[
  **Recursion**

  *"It is legal for a function to call another function.*

  Before learning Recursion, lets test this hypotheses

  ```python
  def customer_support():
      print("How may I help you?")

  def client():
      inp = input("Enter 0 to talk to our customer care executive.\nEnter 1 to exit this program")
      if inp == "0":
          customer_support()    # call another function from this one.          
  ```
]
???

---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Conditionals
  ## - Boolean Operators
  ## Recursion
]
.right-column[
  **Recursion**

  *"It is legal for a function to call itself*

  ```python
  def countdown(n):
      if n <= 0:
          print 'Blastoff!'
      else:
          print n
          countdown(n-1)       
  ```
  What happens when we call `countdown(3)`?
]
???
A function that calls itself is recursive; the process is called recursion
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Conditionals
  ## - Boolean Operators
  ## Recursion
  ## - Stack diagram
]
.right-column[
  **Stack diagram**

  http://www.openbookproject.net/thinkcs/python/english2e/ch03.html#stack-diagrams

  <!-- <img src="../img/stack.png" width="50%" align="right"> -->

  ```python
  def print_twice(param):
      print param, param
      print cat

  def cat_twice(part1, part2):
      cat = part1 + part2
      print_twice(cat)

  chant1 = "Pie Jesu domine, "
  chant2 = "Dona eis requim."
  cat_twice(chant1, chant2)     
  ```
]
???
Use stack diagram to understand recursion.
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Conditionals
  ## - Boolean Operators
  ## Recursion
]
.right-column[
  **Infinite Recursion**

  ```python
  def recurse():
      recurse()       
  ```
  Can you see how this is bad?

  This is known as **Infinite recursion** and Python intelligently, stops this with a
  `RuntimeError` after a certain depth. Try it!
]
???
A function that calls itself is recursive; the process is called recursion
---

<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Conditionals
  ## - Boolean Operators
  ## Recursion
]
.right-column[
  **Problem-1.**

  Fermat’s Last Theorem says that there are no positive integers a, b, and c such that

      `a**n + b**n = c**n`

  for any values of n greater than 2.

  1. Write a function named check_fermat that takes four parameters— a , b , c and n —and that
  checks to see if Fermat’s theorem holds. If n is greater than 2 and it turns out to be true that
  `a**n + b**n = c**n` the program should print, “Holy smokes, Fermat was wrong!” Otherwise the program should print, “No, that doesn’t work.”
  2. Write a function that prompts the user to input values for a , b , c and n , converts them to
  integers, and uses `check_fermat` to check whether they violate Fermat’s theorem.
]
???
A function that calls itself is recursive; the process is called recursion
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Conditionals
  ## - Boolean Operators
  ## Recursion
]
.right-column[
  **Problem-2.**

  Draw a Koch curve using pyprocessing.
]
???
A function that calls itself is recursive; the process is called recursion
---

<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Conditionals
  ## - Boolean Operators
  ## Recursion
  ## Iteration
]
.right-column[
  Iteration is the most common way to achieve repition in programming.

  ```python
  import random
  while True:
    condition = random.rand()
    print("Heads")
    if condition > 0.5:
        print("Tails")
        break

  ```
]
???
A function that calls itself is recursive; the process is called recursion
---
