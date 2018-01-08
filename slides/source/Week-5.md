<img src="../img/logo.jpg" width="16%" align="right">
# List, Tuples and more strings

<!-- <img src="../img/loop_flowchart.png" width="50%" align="right"> -->
---
layout: false
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Class Goals

]
.right-column[
  * Lists
  * Tuples
  * More string patterns
]
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Lists
  ## - List is a sequence
]
.right-column[
  Often we would have to collect information together. Imagine a deck of cards or a box filled with your treasures. These physical collections help organise stuff, and easier to handle multiple items. You know what I mean. similarly, some data structures help us organise and process data. Lists are one of the most common complex data structures we would use in python.

  A **list** is a collection of similar **items**. It is a sequence of **elements**.

  The basic way to create a list is to use `[]`
  ```python
  tens = [10, 20, 30, 40]
  bill = ["noodles", "kebab", "sandwitch"]
  ```
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Lists
  ## - List is a sequence
]
.right-column[
  A string is a sequence of characters, right? Similarly, a list is a sequence, but the elements of a list can be of any datatypes. Infact different elements of the same list can have different types.

  ```python
  favourites = ["chess", 42, True, "indian food", 3.14]
  ```
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Lists
  ## - List is a sequence
  ## - List within a list
]
.right-column[
  When a list is assigned to a variable, its type is `list`

  Keeping true to the claim that list elements can be of any type, the elements can also be lists!
  These lists can be called **nested** lists.
  ```python
  nested = [1, 2, ["a", "b"]]
  ```
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Lists
  ## - List is a sequence
  ## - List within a list
]
.right-column[
  A list without any elements is an *empty list*
  ```python
  empty = []
  ```
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Lists
  ## - List is a sequence
  ## - List within a list
]
.right-column[
  *Problem-1*

  Create a list of grocery items you want to buy.
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Lists
  ## - List is a sequence
  ## - List within a list
  ## - Lists are mutable
]
.right-column[
  Lists belong to the x-men universe, they are mutants! Am kidding! not really.

  lists are mutable, meaning you can change the content of a list anytime during the life cycle of your program

  ```python
  groceries = ["eggs", "bread", "mayo"]
  # remembered we have bread at home, but we dont have ketchup
  groceries[1] = "ketchup"
  print(groceries)    # try this
  ```
  This is in contrast to strings. Even though strings are a sequece you cannot do **item assignment** as you did to the list above.

  Strings are **Immutable**
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Lists
  ## - List is a sequence
  ## - List within a list
  ## - Lists are mutable
]
.right-column[
  You can think of a list as a relationship between `index` and `items`.

  For example in `numbers = ["a", "b", "x", "y", "z"]` index `0` is mapped to `"a"`, index `3` is mapped to `"y"` and so on. The relationship between indices and items is called **mapping**.
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Lists
  ## - List is a sequence
  ## - List within a list
  ## - Lists are mutable
  ## - Traversing lists
]
.right-column[
  just like strings, lists can be traversed easily using a `for` block.

  ```python
  groceries = ["eggs", "bread", "mayo"]
  for item in groceries:
      print("Bought: ", item)
  ```
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Lists
  ## - List is a sequence
  ## - List within a list
  ## - Lists are mutable
  ## - Traversing lists
]
.right-column[
  Say you want to declare a list of numbers first, then multiply each number by 2.

  This is how its done.
  ```python
  numbers = [2, 7, 11, 3]
  for i in range(len(numbers)):
      numbers[i] = numbers[i]*2
  print(numbers)  # try this
  ```
  And this does nothing:
  ```python
  for x in []:
      print("This line will never be printed")
  ```
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Lists
  ## - List is a sequence
  ## - List within a list
  ## - Lists are mutable
  ## - Traversing lists
]
.right-column[
  *Problem-2*

  When Traversing through a nested list, what do you think happens?

  ```python
  random_list = ['spam', 1, ['Brie', 'Roquefort', 'Pol le Veq'], [1, 2, 3]]
  for x in random_list:
      print(x)   # try this
  ```
]
???
Although a list can contain another list, the nested list still counts as a single element. The
length of this list is four
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Lists
  ## - List is a sequence
  ## - List within a list
  ## - Lists are mutable
  ## - Traversing lists
  ## - List operations
]
.right-column[
  The `+` operator concatenates lists
  ```python
  a = [1, 2, 3]
  b = [4, 5, 6]
  c = a + b
  print(c)
  ```
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Lists
  ## - List is a sequence
  ## - List within a list
  ## - Lists are mutable
  ## - Traversing lists
  ## - List operations
]
.right-column[
  The `*` operator repeats a list `n` times
  ```python
  >>> a = [1, 2, 3]
  >>> b = a*2
  >>> print(b)
  [1, 2, 3, 1, 2, 3]
  ```
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Lists
  ## - Aliasing
]
.right-column[
  This might be a bit counter intuitive.

  ```python
  >>> a = [1,2,3]
  >>> b = a
  >>> a[1] = 4
  >>> print(b)
  [1,4,3]
  ```
  a and b refers to the same object
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Lists
  ## - Aliasing
]
.right-column[
  This might be a bit counter intuitive.

  ```python
  >>> a = [1,2,3]
  >>> b = a
  >>> a[1] = 4
  >>> print(b)
  [1,4,3]
  >>> b is a
  True
  ```
  a and b refers to the same object. You can use the `is` operator to verify if two variables are referring to the same object.
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Lists
  ## - Aliasing
  ## - List and strings
]
.right-column[
  How to make a list of characters from a string?
  Hint: You don't need a for loop.

  ```python
  >>> string = "hello"
  >>> chars = list(string)
  >>> print(chars)
  ['h', 'e', 'l', 'l', 'o']
  ```
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Lists
  ## - Aliasing
  ## - List and strings
]
.right-column[
  You can split a string into words using `split()` method

  ```python
  >>> string = "hello how are you?"
  >>> words = string.split()
  >>> print(words)
  ['hello', 'how', 'are', 'you?']
  ```

  An optional argument called a **delimiter** can be used to break a string at different boundaries.
  For the above example, the string is split using a *whitespace* delimiter
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Lists
  ## - Aliasing
  ## - List and strings
]
.right-column[
  To stitch together a list of words into a string, use the string method `.join()`

  ```python
  >>> words = ['hello', 'how', 'are', 'you?']
  >>> # join words with a delimiter inbetween
  >>> string = " ".join(words)
  >>> print(string)
  'hello how are you?'

  ```
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Lists
  ## - Aliasing
  ## - List and strings
  ## - `in` operator
]
.right-column[
  You can split a string into words using `split()` method

  ```python
  >>> L = [1, 2, 3, 4]
  >>> 2 in L
  >>> True
  >>> 4 in L
  >>> False
  ```
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Lists
  ## - Aliasing
  ## - List and strings
  ## - `in` operator
  ## - Deleting element
]
.right-column[
  You can use the `pop` method to delete elements from a list.

  ```python
  >>> t = ['a', 'b', 'c', 'd']
  >>> t.pop()
  'd'
  >>> print(t)
  ['a', 'b', 'c']
  >>> t.pop(0)
  'a'
  >>> print(t)
  ['b', 'c']
  ```
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Lists
  ## - Aliasing
  ## - List and strings
  ## - `in` operator
  ## - Deleting element
]
.right-column[
  You can use the `pop` method to delete elements from a list.

  ```python
  >>> t = ['a', 'b', 'c', 'd']
  >>> del t[1]
  >>> print(t)
  ['a', 'c', 'd']
  >>> t.remove('d')
  >>> print(t)
  ['a', 'c']
  ```

]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Lists
  ## - Aliasing
  ## - List and strings
  ## - `in` operator
  ## - Deleting element
  ## - List arguments
]
.right-column[

  ```
  def delete_head(t):
      del t[0]
  ```

  ```python
  >>> letters = ['a', 'b', 'c']
  >>> delete_head(letters)
  >>> print letters
  ['b', 'c']
  ```
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Lists
  ## - Aliasing
  ## - List and strings
  ## - `in` operator
  ## - Deleting element
  ## - List arguments
]
.right-column[

  ```
  def bad_delete_head(t):
      t = t[1:]
  ```

  ```python
  >>> letters = ['a', 'b', 'c']
  >>> bad_delete_head(letters)
  >>> print letters
  ['a', 'b', 'c']
  ```
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Tuples
]
.right-column[

  Tuples are comma seperated list of values.

  ```python
  >>> t = 1, 2, 3, 4
  >>> print(t)
  (1, 2, 3, 4)
  >>> type(t)
  <class 'tuple'>
  ```
]
???
---

<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Tuples
]
.right-column[

  Although not required, the most common way to define tuples are using paranthesis

  ```python
  >>> t = (1, 2, 3, 4)
  ```

  Just putting a value in paranthesis won't make it a tuple.

  ```python
  >>> s = ("a")
  >>> type(s)
  <class 'str'>
  ```

  If you need to make a tuple with just one element, you can do this:

  ```python
  >>> t = ("a",)    # notice the comma
  ```
]
???
---

<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Tuples
]
.right-column[

  You can also create tuples using the `tuple()` function.

  ```python
  >>> t = tuple()
  >>> x = tuple([1,2,3])
  >>> x
  (1,2,3)
  >>> tuple("harry")
  ('h', 'a', 'r', 'r', 'y')
  ```
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Tuples
]
.right-column[

  Tuple has many similarities to `list`. You can access elements using `[]`.

  ```python
  >>> x = tuple([1,2,3,4,5,6,7])
  >>> x[2]
  3
  >>> x[2:5]
  (3,4,5)
  ```
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Tuples
]
.right-column[

  So why do we have tupples again? Like I can just use list right?

  Ans. Tuples are **immutable**

  You can't modify any element of a tuple.
  ```python
  >>> t = (1, 4, 6)
  >>> t[1] = 6
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  TypeError: 'tuple' object does not support item assignment
  ```
]
???
---

<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Tuples
  ## - Swapping and Tuple assignment
]
.right-column[

  If you have two variables, Generally we can swap them like this:

  ```python
  >>> a = 5
  >>> b = 10
  >>> temp = a
  >>> a = b
  >>> b = temp
  >>> del temp
  ```
  Is there a better way?
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Tuples
  ## - Swapping and Tuple assignment
]
.right-column[

  **Tuple assignment**

  Before finding out how to swap better, picture this. Tuples are comma seperated values.

  ```python
  >>> a = 1, 2    # this is a tuple, even without the ()
  ```

  In python if you comma seperate variables on the left hand side, they are treated as tuples too.
  which means:

  ```python
  a, b = 1, 2
  ```
  will assign `1` to `a` and `2` to `b` respectively. Awesome, that's handy.

]
???
---

<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Tuples
  ## - Swapping and Tuple assignment
]
.right-column[

  **Tuple assignment**
  Swapping in python is probably the most elegant among all languages. To swap variables in python you just do:

  ```python
  >>> a = 5
  >>> b = 10
  >>> b, a = a, b    # that's it
  ```
  The right side has a tuple of two variables, its **unpacked** and assigned into another tuple of two variables on the left side.

]
???
---

<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Tuples
  ## - Swapping and Tuple assignment
]
.right-column[

  Here is an exception:

  ```python
  >>> a = 1, 2, 3    # works, type(a) == 'tuple'
  >>> a, b = 1, 2    # works  type(a) == 'int'
  >>> a, b = 1, 2, 3 # Wrong!
  ValueError: too many values to unpack
  ```
]
???
---

<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Tuples
  ## - Swapping and Tuple assignment
  ## - Usage patterns
]
.right-column[

  The nature of tuple brings out interesting code patterns

  ```python
  >>> email = "hello@spacetime.education"
  >>> usernm, domain = email.split("@")
  ```
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Tuples
  ## - Swapping and Tuple assignment
  ## - Usage patterns
]
.right-column[

  **Tuple as return values**

  Technically a function only returns one value. But if that value is a tuple, it makes it equivalent to return multiple values.

  ```python
  def divmod(dividend, divisor):
      """
      return the reminder and quotient of division of two numbers
      """
      Q = dividend // divisor
      R = dividend % divisor
      return Q, R    # tuple

  >>> q, r = divmod(15, 2)
  >>> q, r
  (7, 1)
  ```
]
???
---

<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Tuples
  ## - Swapping and Tuple assignment
  ## - Usage patterns
  ## - Functions - Variable length arguments
]
.right-column[

  Sometimes we cannot be sure how many arguments does a function we define should consume.

  So a parameter, which starts with `*` gathers all arguments into a tuple

  ```python
  def print_all(*args):
      for x in args:
          print(x)

  >>> t = (1, 2, "hello", True)
  >>> print_all(t)
  1
  2
  'hello'
  True
  ```
  Before learning this snippet, how would you have implemented a multi arguments logic for functions?
]
???
def print_all(args):
    if not isinstance(args, list):
        raise TypeError

    for x in args:
         print(x)

Technically this is just one parameter. so the function call should be:
`>>> print_all([1, 2, "hello", True])`
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Tuples
  ## - Swapping and Tuple assignment
  ## - Usage patterns
  ## - Functions - Variable length arguments
  ## - `zip()` function
]
.right-column[

  `zip()` is a builtin function that takes two or more sequences and zips them into a zip object. This can be typecasted to list of tuples using the `list()` function.

  ```python
  >>> s = "abcde"
  >>> l = [1,2,3,4,5,6,7,8]
  >>> print(list(zip(s, l)))
  [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)]
  ```
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Tuples
  ## - Swapping and Tuple assignment
  ## - Usage patterns
  ## - Functions - Variable length arguments
  ## - `zip()` function
]
.right-column[

  `zip()` is handy when you want to traverse through two sequences within the same loop.

  ```python
  >>> s = "abcde"
  >>> l = [1,2,3,4,5,6,7,8]
  >>> for c, el in zip(s, l):    # not the multi iteration syntax "for c, el"
          print(c, el)
  'a', 1
  'b', 2
  'c', 3
  'd', 4
  'e', 5
  ```
]
???
---

<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Tuples
  ## - Swapping and Tuple assignment
  ## - Usage patterns
  ## - Functions - Variable length arguments
  ## - `zip()` function
  ## - `enumerate()` function
]
.right-column[

  If you need to traverse the elements of a sequence and their indices, you can use the built-in
  function enumerate

  ```python
  >>> for index, element in enumerate('abc'):
          print index, element
  0 a
  1 b
  2 c
  ```
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Tuples
  ## - comparison
]
.right-column[
  ```python
  >>> (0, 1, 2) < (0, 1, 3)
  True
  >>> (0, 1, 2000000) < (0, 2, 3)
  True
  ```
  Python starts from the first element of both sequences and compares them. If the first element of both sequences are equal, python takes the second element and compares.

  If any set elements are different, then it returns the comaprison result and stops any more comparison.

  In the above example, `1 < 2` returns True. So the interpreter never reaches to compare `2000000` with `3`.

]
???
---

<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Tuples
  ## - comparison
  ## - DSU pattern
]
.right-column[
  As a consequence of the above comparison we can leverage it in a pattern called **DSU**, which stands for **decorate, sort, undecorate**.

  Let us sort a list of words by the length of each word.
  ```python
  def sort_by_len(words):
      # D
      t = []
      for word in words:
          t.append((len(word), word))    # append a tuple

      t.sort()

      res = []
      for l, word in t:    # unpack the tuple in a loop
          res.append(word)

      return res    # this is a new list of words sorted by length of each word.
  ```
]
???
---
