<img src="../img/logo.jpg" width="16%" align="right">
# Dictionary and Set

<img src="../img/hash_table.png" width="50%" align="right">
---
layout: false
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Class Goals

]
.right-column[
  * Dictionary

  * Global variables

  ]
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Dictionary
]
.right-column[
  There are many use cases in which we would have to make a collection of values, against different datatypes, this is what a Dictionary is meant to do.

  In lists, the indices had to be integers. In Dictionaries it could be almost any datatype (with exceptions)

  Look at how a physical dictionary works, it stores value matched againsts words. Or think of your twitter id. That's the index I can use to search for your tweets.
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Dictionary
  ## - `dict` type
]
.right-column[
  To create a dictionary in python, you need to tell python the key-value pairs you wish to store in this dictionary, like this:

  ```
  >>> d = {"name": "Jhonny", "age": 25}
  >>> # you can access any item in the dictionary using the [] op
  >>> print(d["name"])
  'Jhonny'
  ```
  If a key you want to access is not present in the dict, it leads to a `KeyError`.
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Dictionary
  ## - `dict` type
]
.right-column[
  Lets create a dictionary that maps English words to Tamil (english script)

  ```python
  >>> eng2tam = {"one": "onnu", "two": "rendu", "three": "moonu"}
  >>> print(eng2tam)
  {'one': 'onnu', 'two': 'rendu', 'three': 'moonu'}
  ```  
  *If you are using python2 or Python3.5 or lesser, then the order of the dictionary will not be preserved. This is important since, order preservation in dictionary is a recent addition (around v3.6.4) and most code have been written without this fact in mind.*
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Dictionary
  ## - `dict` type
]
.right-column[
  Lets create a dictionary that maps English words to Tamil (english script)

  ```python
  >>> eng2tam = {"one": "onnu", "two": "rendu", "three": "moonu"}
  >>> print(eng2tam)
  {'one': 'onnu', 'two': 'rendu', 'three': 'moonu'}
  ```
  *If you are using python2 or Python3.5 or lesser, then the order of the dictionary will not be preserved. This is important since, order preservation in dictionary is a recent addition (around v3.6.4) and most code have been written without this fact in mind.*
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Dictionary
  ## - `dict` type
  ## - Ops, methods and Funcs for `dict`
]
.right-column[
  1. Just like in `list`, to get the number of elements in a `dict` do this:

  ```python
  >>> len(eng2tam)
  ```
]
???
Python uses an algorithm called `hashtable` in dictionaries, which is really interesting as it takes constant time for the `in` op irrespective of the len of the dict.

More later in the course.
---

<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Dictionary
  ## - `dict` type
  ## - Ops, methods and Funcs for `dict`
]
.right-column[
  2. The `in` op tells you whether a *key* is present in the dictionary

  ```python
  >>> 'one' in eng2tam
  True
  ```
]
???
Python uses an algorithm called `hashtable` in dictionaries, which is really interesting as it takes constant time for the `in` op irrespective of the len of the dict.

More later in the course.
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Dictionary
  ## - `dict` type
  ## - Ops, methods and Funcs for `dict`
]
.right-column[
  3. To get the values of items in a `dict`
  ```python
  >>> eng2tam.values()
  dict_values(['onnu', 'rendu', 'moonu'])
  ```
  You can traverse through the values like a list. Or make it into a pure python list by passing it into the `list()` function.
]
???
Python uses an algorithm called `hashtable` in dictionaries, which is really interesting as it takes constant time for the `in` op irrespective of the len of the dict.

More later in the course.
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Dictionary
  ## - `dict` type
  ## - Ops, methods and Funcs for `dict`
]
.right-column[
  4. To get both the keys and values as a dict object of list of tuples, use `.items()`

  ```python
  >>> eng2tam.items()
  dict_values([('one','onnu'), ('two', 'rendu'), ('three', 'moonu')])
  ```
  You can traverse through the values like a list. Or make it into a pure python list by passing it into the `list()` function.
]
???
Python uses an algorithm called `hashtable` in dictionaries, which is really interesting as it takes constant time for the `in` op irrespective of the len of the dict.

More later in the course.
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Dictionary
  ## - `dict` type
  ## - Ops, methods and Funcs for `dict`
  ## - What can I do with `dict`?
]
.right-column[
  Suppose you wish to count the number of times a particular character appears in a text, how would you go about implementing it? ("apple", a:1, p:2, l:1, e:1)

]
???
1. You can use a list with many indices and using the `ord()` the character as the index
2. Create 26 variables, intialize to 0 and increment. (bad one)
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Dictionary
  ## - `dict` type
  ## - Ops, methods and Funcs for `dict`
  ## - What can I do with `dict`?
]
.right-column[
  The dict way is pretty sleek. Check this out:

  ```python
  def histogram(string):
      d = dict()
      for char in string:
          if char not in d:    # checks if the key is present in d
              d[char] = 1
          else:
              d[char] += 1     # You can use x += 1, instead of x = x + 1
  ```
**histogram** means frequencies of appearence of different items.
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Dictionary
  ## - `dict` type
  ## - Ops, methods and Funcs for `dict`
  ## - What can I do with `dict`?
]
.right-column[
  The dict way is pretty sleek. Check this out:

  ```python
  def histogram(string):
    ...

  h = histogram("superman")
  print(h)
  ```
  prints
  ```python
  {'s': 1, 'u': 1, 'p': 1, 'e': 1, 'r': 1, 'm': 1, 'a': 1, 'n': 1}
  ```
]
???
---

<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Dictionary
  ## - `dict` type
  ## - Ops, methods and Funcs for `dict`
  ## - What can I do with `dict`?
]
.right-column[
  You can also access the items in the dict using a `get` method.

  ```python
  d = histogram("a")
  d["b"]    # leads to KeyError
  ```
  ```python
  # if you want to get a default value, if a key is not present, use the get method
  >>> d.get("a", 0)
  1
  >>> d.get("b", 0)
  0
  ```
]
???
---

<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Dictionary
  ## - `dict` type
  ## - Ops, methods and Funcs for `dict`
  ## - What can I do with `dict`?
]
.right-column[
  Looping and Dictionary

  When you loop through a `dict` using `for` you get the keys out.
  ```python
  d = histogram("abcda")
  for char in d:
      print(char, d[char])
  ```
]
???
---

<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Dictionary
  ## - Reverse Lookup
]
.right-column[
  Given a value, can you find a key that matches.

  ```python
  # first match
  def reverse_lookup(d, v):
      for k in d:
          if d[k] == v:
              return v
      raise ValueError
  ```
  ```python
  >>> h = histogram('parrot')
  >>> k = reverse_lookup(h, 2)
  >>> print k
  ```
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Dictionary
  ## - Reverse Lookup
  ## - Inverse of a dict
]
.right-column[
if you were given a dictionary that maps from letters to frequencies, you might want to invert it; that is, create a dictionary that maps from frequencies to letters.

  ```python
  def invert_dict(d):
      inverse = dict()
      for key in d:
          val = d[key]
          if val not in inverse:
              inverse[val] = [key]
          else:
              inverse[val].append(key)
      return inverse
  ```
]
???
---

<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Dictionary
  ## - Reverse Lookup
  ## - Inverse of a dict
  ## - Memoization
]
.right-column[
  Take the example of fibonacci series we dealt with earlier in this course. This is a call graph of `fib(n)`

  <img src="../img/call_graph.png" width="50%" align="right">
]
???
---

<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Dictionary
  ## - Reverse Lookup
  ## - Inverse of a dict
  ## - Memoization
]
.right-column[
  This is how we would have implemented `fibo.py`

  ```python
  def fib(n):
      if n < 0:
          raise ValueError

      if n == 0:
          return 0
      elif n == 1:
          return 1
      else:
          res = fib(n-1) + fib(n-2)
      return res
  ```
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Dictionary
  ## - Reverse Lookup
  ## - Inverse of a dict
  ## - Memoization
]
.right-column[
  Is there a better way? Yup. That's the point. Check this out.

  ```python
  known = {0: 0, 1: 1}

  def fib(n):
      if n < 1:
          raise ValueError

      if n in known:
          return known[n]

      res = fib(n-1) + fib(n-2)
      known[n] = res    # storing for faster query in future
      return res
  ```
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Global variables
]
.right-column[
In the previous example, known is created outside the function, so it belongs to the special
frame called __main__ .

Variables in __main__ are sometimes called **global** because they
can be accessed from any function. Unlike **local variables**, which disappear when their
function ends, global variables persist from one function call to the next.
]
???
---

<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Global variables
]
.right-column[
```python
is_printable = True

def printer():
    if is_printable:
        print("Hello")

printer()
```

This prints the word "Hello" as the *global* variable `is_printable` is accesible from the function.
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Global variables
]
.right-column[
Ok, I have another use case. I want to keep track of if a function is executed or not using a global variable.
```python
is_executed = False

def foo():
    is_executed = True
    # more logic

foo()
print(is_executed)
```

Try this and see what happens?
]
???
---

<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Global variables
]
.right-column[
```python
is_executed = False

def foo():
    is_executed = True
    # more logic

foo()
print(is_executed)
```

What happens is the function `foo()` creates a local variable called `is_executed` and when the function ends, that variable goes away. poof.
]
???
---

<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Global variables
]
.right-column[
To reassign a global variable, use the `global` keyword
```python
is_executed = False

def foo():
    global is_executed    # now python knows which var you are refering to
    is_executed = True
    # more logic

foo()
print(is_executed)
```
This time you get `True`.
]
???
---
