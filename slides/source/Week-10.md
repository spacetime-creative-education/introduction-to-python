<img src="../img/logo.jpg" width="16%" align="right">
# Special expressions, Generators, Map, Reduce, Filter, Lambda
## All the goodies in one place

<!-- <img src="../img/hash_table.png" width="50%" align="right"> -->
---
layout: false
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Class Goals

]
.right-column[
  * Special arsenel to load up your toolbox

  ]
???
How are we going to do it?

By creating awesome class definitions
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Goodies
]
.right-column[
  So far along the course, we have seen the basic ways to write python.

  What we learnt so far is enough to express most of your ideas into programs, but there are these set of tools that makes things faster, consise and complete. This session is about such python tools.
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Goodies
  ## - Conditional expressions
]
.right-column[
  Here is another way to express conditionals, but more like in a single line fashion.

  ```python
  y = math.log(x) if x > 0 else float('nan')
  ```
  This is equivalent to
  ```python
  if x > 0:
    y = math.log(x)
  else:
    y = float('nan')
  ```
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Goodies
  ## - Conditional expressions
]
.right-column[
  Recursive functions are ruled by contionals right? See this example of how we can write consise code in a Recursive function:

  ```python
  def factorial(n):
      return return 1 if n == 0 else n * factorial(n - 1)
  ```
  *Not the best way to write factorial, but works for clean inputs*
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Goodies
  ## - Conditional expressions
  ## - List comprehensions
]
.right-column[
    Loops that generate lists are a common pattern. The pythonic way to achieve it that mostly works is using **list comprehensions**. consider this example in which we capitalize every word in a sentence.

  ```python
  text = "Baa, baa, black sheep, Have you any wool?"
  caps = []
  for w in text.split():
      caps.append(w.capitalize())
  new_text = " ".join(caps)
  ```
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Goodies
  ## - Conditional expressions
  ## - List comprehensions
]
.right-column[
    Using list comprehensions, we can have shorter code, trading the readablity of it a little bit. The last code would look like:

    ```python
    caps = [w.capitalize() for w in text.split()]
    new_text = " ".join(caps)
    ```
    *We can achieve the above code in 1 line, any ideas how?*
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Goodies
  ## - Conditional expressions
  ## - List comprehensions
  ## - Generator expressions
]
.right-column[
    Generator expressions are similar to list comprehensions, but with parantheses instead of square brackets

    ```python
    caps = (w.capitalize() for w in text.split())
    new_text = " ".join(caps)
    ```

    What's the difference? Well, this one's lazy
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Goodies
  ## - Conditional expressions
  ## - List comprehensions
  ## - Generator expressions
]
.right-column[
    A list comprehensions computes the list and keeps it in memory. This method is inefficient in case the list to be produced is huge. Such cases would be ideal for *Generator expressions*

    Generator expressions, computes one element at a time at the time of execution.

    consider this generator expression:

    ```python
    >>> g = (x**2 for x in range(2, 10))
    >>> print(g)
    <generator object <genexpr> at 0x7f16931eba40>
    >>> next(g)
    4
    >>> next(g)
    9
    ```

    You can call the genexpr with the `next()` function or `g.__next__()` method to get the value of the next element.

    This is what a for loop or while loop to which these expressions are plugged to, does.
]
???
---

<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Goodies
  ## - Conditional expressions
  ## - List comprehensions
  ## - Generator expressions
  ## - Generator functions
]
.right-column[
  We can make functions that behave like generator expressions, these are called generator functions (cool unpredicable name).

  Consider this function:
  ```python
  def fibo(n):
      seq = [0, 1]
      for _ in range(n-2):
          seq.append(seq[-1] + seq[-2])
      return seq
  ```
  It works great for anywhere upto n = 100, but what about n = 10k, or 1M. If we need such fibo sequences loading so much data into RAM at once is a bad idea, that calls for the need to use Generators.
]
???
---

<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Goodies
  ## - Conditional expressions
  ## - List comprehensions
  ## - Generator expressions
  ## - Generator functions
]
.right-column[
  To understand generator functions, we need to use the `yield` keyword.

  ```python
  def fibo(n):
      left = 0
      right = 1
      yield 0
      for _ in range(n):
          ans = left + right
          yield ans
          left = right
          right = ans
  ```
  `g = fibo(n)` makes `g` a generator. So it needs to plugged to a loop or `next()` can be used to get the values out of it.

  * Every time the `next()` function is called on the generator, the latest value held at `yield` is given out.

  * Until a yield is triggered, the code below is paused and not executed. This functionality brings many use cases, as these functions can be time delayed. (Asynchronous programming)

]
???
---

<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Goodies
  ## - Conditional expressions
  ## - `any()` and `all()`
]
.right-column[
  Handy functions that can be used on sequences in conjunction with conditionals.

  ```python
  >>> any([True, False, False])
  True
  >>> all([True, True, False])
  False
  ```
  Any and all also consumes generator expressions and generator functions to come up with a boolean.
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Goodies
  ## - Conditional expressions
  ## - `any()` and `all()`
  ## - Sets
]
.right-column[
  A special datatype, that mimics the `set` functionality in mathematics. Very useful for doing probability and statistics problems in python.

  Consider this function:

  ```python
  def subtract(d1, d2):
      res = dict()
      for key in d1:
          if key not in d2:
              res[key] = None
      return res
  ```
  let d1 contain words from any text doc as keys, and d2 be a list of words. If the document contains words that are not in d2, then values are set to None `res[key] = None`.
]
???
---

<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Goodies
  ## - Conditional expressions
  ## - `any()` and `all()`
  ## - Sets
]
.right-column[
  If you Remember set theorem, a set contains unique values, and has various operators like union, intersection, subtraction etc.

  The last example is a classic use case for set subtraction.

  ```python
  def subtract(d1, d2):
      return set(d1) - set(d2)
  ```

  The result is a set instead of a dictionary, but for operations like iteration, the behavior is the same.

  Let's dig deeper
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Goodies
  ## - Conditional expressions
  ## - `any()` and `all()`
  ## - Sets
]
.right-column[
  You can define a set using `{}` just like dictionary, the only difference being sets are not `key-value` pairs, they only have values.

    ```python
    >>> s = {}
    >>> dice = {1,2,3,4,5,6}
    >>> suites = {'heart', 'spade', 'club', 'diamond'}
    ```
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Goodies
  ## - Conditional expressions
  ## - `any()` and `all()`
  ## - Sets
]
.right-column[
  Unique list. If you want a list of items to have only unique items, just convert it into a set, and if required convert back into a list.

    ```python
    >>> l = [1,2,2,3,3,3,4,4,4,4]
    >>> s = set(l)
    >>> for x in s:
            print(x)
    1
    2
    3
    4
    >>>
    ```
]
???
---

<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Goodies
  ## - Conditional expressions
  ## - `any()` and `all()`
  ## - Sets
]
.right-column[
  Set has methods like union, and intersection. Also operators like `< > ==` etc works exactly like how they do in set theorem.

  HomeWork:

  Explore set operators and give an explanation of behaviour for each of the op.
]
???
---

<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Goodies
  ## - Conditional expressions
  ## - `any()` and `all()`
  ## - Sets
]
.right-column[
  Unique list. If you want a list of items to have only unique items, just convert it into a set, and if required convert back into a list.

    ```python
    >>> l = [1,2,2,3,3,3,4,4,4,4]
    >>> s = set(l)
    >>> for x in s:
            print(x)
    1
    2
    3
    4
    >>>
    ```
]
???
---

<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Goodies
  ## - Conditional expressions
  ## - `any()` and `all()`
  ## - Sets
]
.right-column[
  Unique list. If you want a list of items to have only unique items, just convert it into a set, and if required convert back into a list.

    ```python
    >>> l = [1,2,2,3,3,3,4,4,4,4]
    >>> s = set(l)
    >>> for x in s:
            print(x)
    1
    2
    3
    4
    >>>
    ```
???
---

<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Goodies
  ## `Lambda`
]
.right-column[
  `lambda` keyword helps us create unnamed, disposable functions.

  for example:

  ```python
  f = lambda x: x**2
  ```
  Is a function that squares and returns the input.

  try: `f(4)`
]
???
http://book.pythontips.com/en/latest/map_filter.html
---

<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Goodies
  ## - Conditional expressions
  ## - `any()` and `all()`
  ## - Sets
]
.right-column[
  Unique list. If you want a list of items to have only unique items, just convert it into a set, and if required convert back into a list.

    ```python
    >>> l = [1,2,2,3,3,3,4,4,4,4]
    >>> s = set(l)
    >>> for x in s:
            print(x)
    1
    2
    3
    4
    >>>
    ```
???
---

<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Goodies
  ## `Lambda`
  ## `Map`, `Filter` and `Reduce`
]
.right-column[
http://book.pythontips.com/en/latest/map_filter.html]
???

---
