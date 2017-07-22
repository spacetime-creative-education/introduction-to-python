<img src="../img/logo.jpg" width="16%" align="right">
# Basic blocks of Python
### Colors of the palette

<img src="../img/lego.jpg" width="50%" align="right">
---
layout: false
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Class Goals

]
.right-column[
  * Dive into python
    * Python as a calculator
    * Operators and operands
    * Variables
    * Writing your first script
    * Comments
    * String operations
    * Data types
    * Debugging
    * Course project Introduction
    * Homework
]
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Dive into python
]
.right-column[
  In this section we would learn the basics of Programming with python.

  But, before getting to the concepts, let us open the python interpreter and type some code into it.
]
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Dive into python
]
.right-column[
```bash
$ python
Python 3.6.1 |Continuum Analytics, Inc.| (default, May 11 2017, 13:09:58)
[GCC 4.4.7 20120313 (Red Hat 4.4.7-1)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```
--
We already saw the simplest code! The `Hello World` program

```python
>>> print("Hello, world!")
```

]
---
<img src="../img/logo.jpg" width="16%"\] align="right">
.left-column[
  ## Dive into python
  ### - Python as a calculator
]
.right-column[
--
But `print()` doesn't stop there, it does a lot more.

```python
>>> print(2+2)
4
>>> print("2+2")
2+2
>>> print("I am you `go to tool` when it comes to debugging!")
```

]
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Dive into python
  ### - Python as a calculator
]
.right-column[
**Python as a calculator**

It is pretty straight-forward to use python REPL as your calculator.

Do not summon the a calculator app on your PC/mobile. Its lot more
faster to compute your grades or add up your monthly credit on a python command-line

*Practise*
Figure out what each of the operators `*, /, +. -, (), **` does and try out some basic computations. You would need it for your first exercise.

```
>>> 30 / 2
15.0
```
]
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Dive into python
  ### - Python as a calculator
  ### - Operators and operands
]
.right-column[

**Operators** are special symbols that represent computations like addition and multiplication.
The values the operator is applied to are called **operands**

  Math operators:

  `*`: `multiplication`

  `/`: `division`

  `+`: `addition`

  `-`: `subtraction`

  `**`: `power`

  `//`: `integer division`

  ```python  
  >>> 7 // 2    # try This
  ```
]
???
In python 2 `/` was by default integer division, if you wanted to do float division
like the one in py3, you needed to do `float(3)/2`.
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Dive into python
  ### - Python as a calculator
]
.right-column[
**BODMAS** or **PEMDAS** or just use your math intuition

Hierarchy:

B - Bracket (Parentheses)

O - Order (Exponential or Power of)

D, M - Division, multiplication

A, S - addition, subtraction
]
???
`float` is floating-point
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Dive into python
  ### - Python as a calculator
  ### - Operators and operands
]
.right-column[
**Let us do some physics**

**Exercise-1**
*Insert a nice simple one line physics problem here*
]
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Dive into python
  ### - Python as a calculator
  ### - Operators and operands
  ### - Variables
]
.right-column[
  In the most popular sense, Variables are containers in which you store data
  and process them easily, anytime in the lifecycle of a program.

  They help a lot in maintaining the flow of your code, and saves you a LOT of time and energy.
  <img src="../img/kitchen.jpg" width="75%" alight="center">
]
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Dive into python
  ### - Python as a calculator
  ### - Operators and operands
  ### - Variables
]
.right-column[
  *Let's say you want to work on "Answer to the Ultimate Question of Life, the Universe, and Everything",
  obviously you are Working with a number. You can put this into a `named container` (a.k.a variable) and process it.*

  For example:
  ```python
  >>> answer = 42    # need a better name for this variable
  >>> print(answer)
  ```
]
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Dive into python
  ### - Python as a calculator
  ### - Operators and operands
  ### - Variables
]
.right-column[

  **statements**
  ```python
  >>> x = 42       # statement
  >>> y = x + 5    # statement, something the Interpreter can execute
  ```

  `x`, `42`, `x+42` or any fragments of code that makes up a statement are called **expressions**
]
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Dive into python
  ### - Python as a calculator
  ### - Operators and operands
  ### - Variables
]
.right-column[
  **How to name it?**

  > There are only two hard things in Computer Science: cache invalidation and naming things. -- Phil Karlton

  If you give a variable an illegal name, the Interpreter will throw a `SyntaxError` when you run your program.

  ```python
  >>> 42isthesecretofuniverse = 42
  SyntaxError
  >>> emailid@website = "myemailid@gmail.com"    # only symbols allowed AFAIK is _
  SyntaxError
  >>> class = "12th"    # `class` is a reserved keyword, so is `if`, `for`, `while` and many more
  SyntaxError
  >>> google.com = "Google.com"    # . is reserved for something you will learn later
  SyntaxError
  ```
]
???
keyword: A reserved word that is used by the compiler to parse a program; you cannot
use keywords like if , def , and while as variable names.
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Dive into python
  ### - Python as a calculator
  ### - Operators and operands
  ### - Variables
]
.right-column[
  **There are different kinds of data your program works with, like text data, numbers, maybe complex numbers**

  This essential quality of data is called a `datatype` or casually just `type`.

  Each variable has a `type`. To find the type of the data you assigned to a variable, simply use `type()`.

  ```python
  >>> salutation = "Hello"
  >>> type(salutation)
  str
  >>> type(3.14)
  float
  >>> type(3)
  int
  >>> type(True)    # or try False
  bool
  ```
]
???
You generally work with three types of three types of data, text (string), numbers (integer and float), binary (Boolean). There are also more complex datatypes which we will see later.

C, Java etc has more datatypes for numbers, like double, In such languages the coder is responsible for memory management which python automates for you.
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Dive into python
  ### - Python as a calculator
  ### - Operators and operands
  ### - Variables
]
.right-column[
  <img src="../img/Variables.png" width="100%" align="right">
]
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Dive into python
  ### - Python as a calculator
  ### - Operators and operands
  ### - Variables
  ### - Writing your first script
]
.right-column[
*When you write software, generally you would want to ship it so that an end user can use it.*

- You either ship the source code
[OR]
- You can make an executable with your code (*Like an App*)

<img src="../img/ship_software.jpg" width="75%" align="right">
]
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Dive into python
  ### - Python as a calculator
  ### - Operators and operands
  ### - Variables
  ### - Writing your first script
]
.right-column[
To make code that can be shared with others and run on other devices, you need to save it in files.
*Time to fire up your editor*

1. Create a course folder named `python_course`
2. Open your editor, and create an empty file named `say_hello.py`

Here `.py` is the extension of python source code.

]
???
`say_hello.py` asks you for your name and says hello to you specifying your name
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Dive into python
  ### - Python as a calculator
  ### - Operators and operands
  ### - Variables
  ### - Writing your first script
]
.right-column[
`say_hello.py`
```python
salutation = "Hello, "
name = input('What is your name? : ')
print(salutation + name)
```
]
???

---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Dive into python
  ### - Python as a calculator
  ### - Operators and operands
  ### - Variables
  ### - Writing your first script
]
.right-column[
**How to execute your script?**
1. Open a terminal/Command prompt
2. Go to (use `cd`) the desired folder, like `cd python_course`
3. Run `python say_hello.py`
]
???

---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Dive into python
  ### - Python as a calculator
  ### - Operators and operands
  ### - Variables
  ### - Writing your first script
  ### - String operations
]
.right-column[
As you would have noticed in `say_hello.py` the `+` operator is not just mathematical.

`+` glues two strings together.

```python
>>> print("Hello" + "exciting" + "world")
```
]
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Dive into python
  ### - Python as a calculator
  ### - Operators and operands
  ### - Variables
  ### - Writing your first script
  ### - String operations
]
.right-column[
Other math operators doesn't really work with strings, except `*`
```python
>>> print("Hello" * "exciting")
TypeError: can't multiply sequence by non-int of type 'str'
```
So you need an `int` and a `str`. Hmmm...

Let's try using `*` with an `int` and a `str`, what could possibly go wrong?
```python
>>> "Hello"*5000
```
]
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Dive into python
  ### - Python as a calculator
  ### - Operators and operands
  ### - Variables
  ### - Writing your first script
  ### - String operations
  ### - Comments
]
.right-column[
Like good *Writers*, coders want their code to be readable.

> Simple is better than complex.
  Complex is better than complicated.
  ~ Zen of Python

*Keep things simple*

Use the `#` symbol to add comments. Any text after the `#` is not executed by
the interpreter in a line.
```python
# compute the percentage of the hour that has elapsed
percentage = (minute * 100) / 60
```
]
???
Formal languages are dense, and it is often difficult to look at a piece of code and figure out what
it is doing, or why. Its a good idea to add notes to your code to save effort trying to understand a piece of code (not only for others, for your future self too)

---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Dive into python
  ### - Python as a calculator
  ### - Operators and operands
  ### - Variables
  ### - Writing your first script
  ### - String operations
  ### - Comments
]
.right-column[
*Good code is self documented*

This comment is redundant with the code and useless:

`v = 5 # assign 5 to v`

This comment contains useful information that is not in the code:

`v = 5 # velocity in meters/second.`

Good variable names can reduce the need for comments, but long names can make
complex expressions hard to read, so there is a tradeoff.

`velocity_of_the_train_in_metres_per_second = 5    # really long`

`vel = 5    # in metres / second`
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Debugging
]
.right-column[
*Some more debugging*

When you leave a space in a variable name, python thinks it is two operands
without an operator in between, so it raises a `SyntaxError`

```python
>>> bad name = "Gru"
SyntaxError
```

```python
>>> unit_circle_area = (4/3)*pi
NameError: 'pi' is not defined

```

```python
>>> pi = 3.14
>>> velocity = 1    # metres / second
>>> omega = velocity / 2 * pi     # angular velocity

```
]
???
try `omega = velocity / pi * 2     # angular velocity`
Use Brackets.
---

### variables

<img src="../img/Variables.png" width="60%" alight="center">
<img src="../img/logo.jpg" width="16%" align="left">

<section data-background-image="../img/kitchen.jpg">
        <h2>Color</h2>
</section>

### variables

<img src="../img/Variables.png" width="60%" alight="center">
<img src="../img/logo.jpg" width="16%" align="left">

A variable in the classical programming sense is a container which holds
different types of data. Having data in `named containers` is really useful,
kind of like having salt and pepper in seperate shakers.

Analogy: Imagine a you are making a dish in your kitchen, then variables

<img src="../img/logo.jpg" width="16%" align="right">
### Language Introduction

- Declaring variables
- Python as a calculator

```python
one_dozen = 12
num_eggs = one_dozen / 2
print(num_eggs)
```

```python
# Buy 2 more eggs
num_eggs + 2
```

<img src="../img/logo.jpg" width="16%" align="right">
### Language Introduction

- Declaring variables
- Python as a calculator

```python
customer_name = "Elon Musk"    # A string can be expressed within a ' ' or a " "
print("Hello, " + customer_name)
```

<img src="../img/logo.jpg" width="16%" align="right">
### Language Introduction

- Declaring variables
- Python as a calculator

<img src="../img/logo.jpg" width="16%" align="right">
### Now that you got a feel of python, what do you think are its striking
features?

- Dynamic typing

- High-level with an interpreter which translates your code to low-level
language

![interpreter](../img/interpreter_vs_compiler.png)

An interpreter reads a high-level program and executes it, meaning that it
does what the program says. It processes the program a little at a time,
alternately reading
lines and performing computations. Figure 1.1 shows the structure of an
interpreter.

A compiler reads the program and translates it completely before the program
starts run-
ning. In this context, the high-level program is called the source code, and the
translated
program is called the object code or the executable. Once a program is compiled,
you
can execute it repeatedly without further translation.
