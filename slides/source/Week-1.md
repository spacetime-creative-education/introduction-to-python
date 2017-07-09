<img src="../img/logo.jpg" width="16%" align="right">
# Basic blocks of Python
### Colors of the palette


---
layout: false
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Language Introduction

]
.right-column[
  In this section we would learn the basics of Programming with python.

  But, before getting to the concepts, let us open the python interpreter and type some code into it.

]

---
[//]:#<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Language Introduction
  ### - Dive into python
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
The simplest code!

```bash
>>> print "I am ready!"
```

]
---
[//]: #<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Language Introduction
  ### - Dive into python
]
.right-column[
```bash
$ python
Python 3.6.1 |Continuum Analytics, Inc.| (default, May 11 2017, 13:09:58)
[GCC 4.4.7 20120313 (Red Hat 4.4.7-1)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

The simplest code!

```bash
>>> print "I am ready!"
```

]
---

### Language Introduction

The simplest code!

```bash
>>> print "I am ready!"
```

<img src="../img/logo.jpg" width="16%" align="left">

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
