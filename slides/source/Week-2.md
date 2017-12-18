<img src="../img/logo.jpg" width="16%" align="right">
# Functions
### Do not repeat yourself

<img src="../img/function_machines_composed.png" width="40%" align="right">

*image src: mathinsight.org*
---
layout: false
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Class Goals

]
.right-column[
  * Functions
    * Function calls
    * Type conversion
    * Math Functions
    * Code blocks and Intendation
    * Debugging


  * GUI programming
    * Introduction to Pyprocessing
    * What is a module?
    *
    * Homework


]
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Functions
]
.right-column[
  In programming, a *function* is a named sequence of statements that performs
  a computation.  

  When you define a function, you specify the name and the sequence of
  statements. Later, you can “call” the function by name.
]
???

---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Functions

]
.right-column[
  Functions in programming are very similar to functions in math.

  Common math functions: `log`, `sine`, `polynomials`

  Say, you wish to compute a polynomial function `f(x) = x**2 + 2*x + 3`, the sequence of steps involved
  might be:

  1. Read `x`
  2. Find `x**2`, store it in a variable (say `x_sqr`)
  3. Find `2*x`, store it in a variable (say `two_x`)
  4. Add the terms `x_sqr`, `two_x` and the constant `3` and store the result in
  a variable `result`
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Functions
  ### - Function call
]
.right-column[
  Let's see a function we have already seen in this course:

  ```python
  >>> type(32)
  <class 'int'>
  ```
  `type()` is a *function* that takes one **argument** (an integer in this example)
  and **returns** the type of the argument.

  ```python
  >>> type("Hello")
  <class 'str'>  
  ```
]
???
**Argument** Input to a function

Just like the polynomial example, a sequence of steps would have been executed
to find the type of the input argument.
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Functions
  ### - Function call
  ### - Type conversion functions
]
.right-column[
  Python exposes a lot of in-built functions to make our life easier.

  Some of the key functions are `type conversion` functions.
  ```python
  >>> int("32")
  32
  >>> x = int("32")
  >>> type(x)
  >>> <class 'int'>
  >>> int(3.14)
  3
  ```
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Functions
  ### - Function call
  ### - Type conversion functions
]
.right-column[
  ```python
  >>> float(32)
  32.0
  >>> str(32)
  '32'
  ```
]
???
Introduce bool() later in flow control
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Functions
  ### - Function call
  ### - Type conversion functions
  ### - import modules
]
.right-column[
  Functions makes code re-distributable, and coders enjoy using functions, as
  they don't have to write every logic from scratch.

  In fact we are most likely to use **functions** written by other programmers,
  which they distribute as modules.

  You can simply `import` a **module** of functions and work with them.

  <img src="../img/toolbox.jpg" width="50%" align="right">
  *The word Toolbox is also used sometimes to refer to modules*
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Functions
  ### - Function call
  ### - Type conversion functions
  ### - import modules
]
.right-column[
  **Python as a scientific calculator**

  ```python
  >>> import math
  >>> print(math)
  <module 'math'>
  ```
  A period (`.`) is used to access different functions inside a module.
  ```python
  >>> math.pi    # the PI constant from math module
  3.141592653589793
  >>> # Let us find the value of sin(90)
  >>> degrees = 90
  >>> radians = (degrees / 360.0) * 2 * math.pi
  >>> math.sin(radians)    # using sin() function from math
  1.0
  ```
]
???
A module is a file that contains a collection of related functions.

A module exposes functions, classes and even constants like in the case of PI.
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Functions
  ### - Function call
  ### - Type conversion functions
  ### - import modules
]
.right-column[

  ```python
  # Try these
  >>> math.sqrt(2)
  >>> math.exp(1)
  >>> math.log(10)
  >>> math.exp(math.log(10))
  ```
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Functions
  ### - Function call
  ### - Type conversion functions
  ### - import modules
]
.right-column[
  So what other functions are in `math`?

  *To understand the contents of a module, it is best to read its documentation.*

  Python built-ins are beautifully documented on the web. Google: python math module
  and open a link that starts with "https://docs.python.org/3/library/"
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Functions
  ### - Function call
  ### - Type conversion functions
  ### - import modules
]
.right-column[
  Other ways to explore a module are:
  ```python
  >>> # import a module and use the dir() function to see the contents of a module
  >>> dir(math)    # pass the module as an argument
  >>> # To get a more detailed documentation of the functions use help()
  >>> help(math)
  >>> help(math.sin)    # help on a specific function
  ```
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Functions
  ### - Function call
  ### - Type conversion functions
  ### - import modules
  ### - Adding new functions
]
.right-column[
  To define a function you need to use the `def` keyword
  ```python
  def print_lyrics():
      print("Imagine there's no heaven")
      print("It's easy if you try")
      print("No hell below us")
      print("Above us only sky")
      print("Imagine all the people living for today")
  ```

  ```python
  >>> print_lyrics()    # calling function
  ```
  Note:

  1. The rules to name a function are same as that of Variables.
  2. The empty paranthesis of the function indicates no argument is *consumed* by it
  3. The line `def print_lyrics():` is called the **header** of the function
  4. The rest of the lines are called the **body**.
  5. The header has to end with a `:` and make sure each statement in the body has exactly 4 spaces indented.
]
???
The strings in the print statements are enclosed in double quotes. Single quotes and double
quotes do the same thing; most people use single quotes except in cases like this where a
single quote (which is also an apostrophe) appears in the string.
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Functions
  ### - Function call
  ### - Type conversion functions
  ### - import modules
  ### - Adding new functions
  ### - Code blocks
]
.right-column[
  A function is a **code block** (A group of statements). There are other code blocks
  which we will see later in this course.

  The structure of a code block is unique in python. In many **other popular languages**
  a code block is defined by using curly braces `{}`. But in python, `intendation`
  is used.

  ```python
  def say_hello():
  <-->print("Hello")    # <--> shows a 4 spaces indentation.
  ```

  The python interpreter uses the `:` to understand that a block of code follows.
  It expects the block to be more to the right than the header statement.
  ]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Functions
  ### - Flow of execution
]
.right-column[
  Exectution of the function always starts at the first statement in the body.
  statements are executed one at a time, from top to bottom.

  *Let's see the order in which python executes the script*
  <iframe width="600" height="400" frameborder="0" src="http://pythontutor.com/iframe-embed.html#code=%23%20define%20function%0Adef%20print_lyrics%28%29%3A%0A%20%20%20%20print%28%22Imagine%20there's%20no%20heaven%22%29%0A%20%20%20%20print%28%22It's%20easy%20if%20you%20try%22%29%0A%20%20%20%20print%28%22No%20hell%20below%20us%22%29%0A%20%20%20%20print%28%22Above%20us%20only%20sky%22%29%0A%20%20%20%20print%28%22Imagine%20all%20the%20people%20living%20for%20today%22%29%0A%0A%23%20call%20function%0Aprint_lyrics%28%29&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=0&heapPrimitives=false&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false"> </iframe>
  ]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Functions
  ### - Flow of execution
  ### - Arguments and Parameters
]
.right-column[
  In the built-ins we saw, some had Arguments, like in `type(32)`, the `integer`, `32` is the argument.

  We can include **parameters** in the functions we write. The arguments we pass
  during a function call will be assigned to the parameters defined.

  ```python
  def greet(name):
    print("Hello, " + name)    # greets using the `name` Parameter
  ```
  Calling function
  ```python
  >>> greet("neo")
  >>> 'Hello, neo'
  ```
  ]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Functions
  ### - Flow of execution
  ### - Arguments and Parameters
]
.right-column[
  functions call can take more than one argument. If you want your function to take 3
  arguments, use 3 parameters seperated by `,` in the function definition.

  ```python
  def greet(prefix, firstname, lastname):
      print("Hello, " + prefix + ". " + firstname + " " + lastname)    # greets using the `name` Parameter
  ```
  Calling function
  ```python
  >>> greet("Mr", "Elon", "Musk")
  >>> 'Hello, Mr. Elon Musk'
  ```
  ]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Functions
  ### - Flow of execution
  ### - Arguments and Parameters
  ### - Returning values
]
.right-column[
  You do not always write functions that print values. Infact like `math.sin()`
  you might want your function to **return** values, so that you can assign them
  to your Variables.

  *Try this*
  ```python
  >>> total = sum(3, 4)    # sum() is a built-in function.
  >>> print(total)
  7
  ```
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Functions
  ### - Flow of execution
  ### - Arguments and Parameters
  ### - Returning values
]
.right-column[
  What if I want to define a function called `adder()` which does exactly
  what `sum()` does, but its more special because I wrote it? :D

  use `return`
  ```python
  def adder(a, b):
      t = a + b
      return t
  ```
  ```python
  >>> total = adder(3, 4)
  >>> print(total)
  7  
  ```
  ]
???
Juice maker example. Takes fruits and vegetables and returns juice.
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Functions
  ### - Flow of execution
  ### - Arguments and Parameters
  ### - Returning values
  ### - Variables and Parameters are local
]
.right-column[
  The variables and Parameters inside a function are **local** which means it only
  exists inside the function. For example

  ```python
  >>> def adder(a, b):
  ...     t = a + b
  ...     return t
  ...
  >>> adder(3,4)
  7
  >>> t
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  NameError: name 't' is not defined
  >>>
  ```
  ]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Debugging
]
.right-column[
  Try this in IDLE or a terminal python REPL

  ```python
  def say_hello_twice():
     print("Hello")    # Use Tab to indent this statement
     print("Hello")    # Use 4 spaces to indent this statement
  ```

  a `TabError` is raised stating `inconsistent use of tabs and spaces in indentation`.
  Python doesn't like it when you mix Tabs with spaces. Fortunately, all your editors (the good ones)
  convert Tabs to spaces, so you can feel free to use Tabs.
]
???
One more reason why you wound want to use a Editor configured for coding.
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Debugging
]
.right-column[

  ```python
  >>> minutes = hours * 60    # Right!
  >>> hours * 60 = minutes    # wrong
  SyntaxError: can't assign to operator
  ```
]
???
---

## Functions
- ### Function calls
- ### Type conversion
- ### Math Functions
- ### Code blocks and Intendation
- ### Zen of python
