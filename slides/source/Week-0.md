<img src="../img/logo.jpg" width="16%" align="right">
# A Fun Dive into Python Programming
### Road to full-stack development

![parser-tongue](../img/parser-tongue.png)

---
layout: false
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Class Goals

]
.right-column[
  * Introduction to python
    * What is a program?
    * An opiniated view on the art of programming
    * Difference between Formal and Natural languages
    * Compilers vs interpreters
    * What is debugging?


  * Getting your hands dirty
    * Installing python on your device
    * Picking an editor
]
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Introduction to python
  ### - What is a program?
]
.right-column[
  A set of instructions that specifies how to perform a computation.

  Let's find an analogy, just to get some perspective.
]
???
Or better, what is code?
It is a set of instructions that we give the computer which upon executing
leads to desired results
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Introduction to python
  ### - What is a program?
]
.right-column[
  *Making Software is like cooking! code is the recipe*
  .right[![cooking-owl](../img/cooking_owl.png)]
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Introduction to python
  ### - What is a program?
]
.right-column[
<img src="../img/rgb.png" width="16%" align="right">
  The components of a program are:
  - Input (*Ingredients*)
  - Output (*The food*)
  - math (*The Process*)
  - conditional execution
  - repetition

  **These are the only components of any code anywhere you find, there isn't anything more to it.**
]
???
Input: Get data from the keyboard, a file, or some other device.
output: Display data on the screen or send data to a file or other device.
math: Perform basic mathematical operations like addition and multiplication.
conditional execution: Check for certain conditions and execute the appropriate code.
repetition: Perform some action repeatedly, usually with some variation.
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Introduction to python
  ### - What is a program?
  ### - Formal vs Natural language
]
.right-column[
  Computers only understand **Formal languages** (*The revolution is here to change the fact!!*)

  Its hard to make computers understand **Natural languages** like English, Hindi or Tamil.

]
???
Sanskrit is a formal language?
The change is from machine learning and NLP developments

---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Introduction to python
  ### - What is a program?
  ### - Formal vs Natural language
]
.right-column[
  **Programming languages are formal languages that have been designed to express computations.**

  features:
  - Strict syntax rules
  - structure is also important
  - No place for misinterpretation. A line of code means one, and only one thing!
]
???
When you read a sentence in English or a statement in a formal language, you have to
figure out what the structure of the sentence is (although in a natural language you do this
subconsciously). This process is called __parsing__.

Natural language is full of ambiguity and redundancy, sometimes literalness (idioms, metaphors)
Prose is closer to programs than poetry.
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Introduction to python
  ### - What is a program?
  ### - Formal vs Natural language
]
.right-column[
  **Written music is formal, and generally each arrangement can be played on only one way by the musician**

  <img src="../img/sheet-music.jpg" width="75%" align="center">
]
???
The language of music is formal, and each symbol on the sheet means one and only one thing.
Not much room for misinterpretation.

---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Introduction to python
  ### - What is a program?
  ### - Formal vs Natural language
  ### - Debugging
]
.right-column[
  *Programming can never be error free*

  > “Failure is an option here. If things are not failing, you are not innovating enough.” ~ Elon Musk

  **bugs** are errors in your code. Debugging is finding and removing them.

  A good cook tastes the food they make, find faults, and corrects them until it tastes good.
]
???

---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Introduction to python
  ### - What is a program?
  ### - Formal vs Natural language
  ### - Debugging
]
.right-column[
  Types of bugs:
  - **Syntactic Error**: Programming languages are unforgiving, any mis-splet word is a syntax Error thrown on your face
  - **Runtime Error**: Some errors pop-up only after a program starts executing. These are **runtime errors** or in python **exceptions**
  - **Semantic Error**: When your code doesn't do what you think it should do (*But its doing exactly what you asked it to do*)

  <img src="../img/robot.png" width="40%" align="left">
]
???
Syntactic errors are caught and a "You are wrong!" message is thrown on your face, before executing the program
Runtime errors are caught only when the program is executed,
Semantic errors: Debugging these are where half your Programming life is going to go

---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Introduction to python
  ### - What is a program?
  ### - Formal vs Natural language
  ### - Debugging
]
.right-column[
  Experimental Debugging:
  *For beginners, debugging is a crude art* You debug by trial-and-error.

  That's also good, as this is the only way to sharpen that coder instinct!
]
???
Analogy: An untrained musician wants to reproduce a sound in his mind, he tries a chord, then by trial-and-error he goes towards the right sound. Thats the most basic debugging.

One of the most important skills you will acquire is debugging. Although it can be frus-
trating, debugging is one of the most intellectually rich, challenging, and interesting parts
of programming.
In some ways, debugging is like detective work. You are confronted with clues, and you
have to infer the processes and events that led to the results you see.

# Insert a nice pic in this slide
---
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Introduction to python
  ### - What is a program?
  ### - Formal vs Natural language
  ### - Debugging
]
.right-column[
  Experimental Debugging:
  > “When you have eliminated the impossible, whatever remains, however im-
probable, must be the truth.” ~ A Conan Doyle

`Insert Sherlock pic here`
]
???
For some debugging and programming are the same thing. There are two types of programmers,
one who think of every possible way in which a line would fail the Software before adding it
to codebase. The second programmer just adds a line, solves the problem at hand, and studies how the software reacts to the change, and like a detective debugs it to stability.
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Introduction to python
  ### - What is a program?
  ### - Formal vs Natural language
  ### - Debugging
  ### - Programs that process programs
]
.right-column[
  There are two kinds of programs that read code and translate them into a language your hardware understands

  - **Compilers**: They read and translate the entire code into `object-code` and then executes it.
  - **Interpreter**: They read and execute each line of code, before reading the next line. (*Lazy*)
]
???
lets say you want to help someone with a cooking contest, you get a recipe online, its in English and this someone ends up translating it into Tamil before going to the contest and cooking, they compiled the recipe

---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Getting your hands dirty
]
.right-column[
  *Enough talk, let's start digging*

  Things to do:
  1. Install python (duh!)
  2. Find and install a nice text editor
  3. Write your first Python program :)
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Getting your hands dirty
  ### - Installing Python
]
.right-column[
  There are many flavours of python and a few versions. Throughout this course
  we are gonna work with Python 3 (*version*), I suggest Anaconda installation (*flavour*)
  for the ease of use. You can also get the default flavour from Python.org.

  1. Go to https://www.continuum.io/downloads (*Google Anaconda installation*)
  2. Scroll down and Choose the Python 3.6 installer for your OS.
  3. Download and install it. (*Linux users, need to run the Anaconda3-x---.sh find using bash on a terminal*)
]
???

---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Getting your hands dirty
  ### - Installing Python
  ### - Text Editor
]
.right-column[
  A text editor is your best ally in coding, especially while coding in python (*why? later*).

  A great text editor understands the language you code in. Makes you write clean code.

  <img src="../img/atom.png" width="20%" align="right">
  <img src="../img/sublime.jpg" width="20%" align="right">
  <img src="../img/pycharm.jpeg" width="20%" align="right">
  <img src="../img/vim.png" width="20%" align="right">
  <img src="../img/notepad++.png" width="20%" align="right">
]
???

---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Getting your hands dirty
  ### - Installing Python
  ### - Text Editor
  ### - First program
]
.right-column[
  Open the python REPL
  ```bash
  $ python
  Python 3.6.1 |Continuum Analytics, Inc.| (default, May 11 2017, 13:09:58)
  [GCC 4.4.7 20120313 (Red Hat 4.4.7-1)] on linux
  Type "help", "copyright", "credits" or "license" for more information.
  >>>
  ```
  ```python
  print("Hello, beautiful world!")
  ```
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Getting your hands dirty
  ### - Installing Python
  ### - Text Editor
  ### - First program
]
.right-column[
  Feel free to get help
  ```python
  >>> help()
  ```
  ```python
  >>> help(print)    # would tell you how to use print
  ```
]
???
