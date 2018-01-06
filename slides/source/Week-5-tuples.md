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

  >>> t.remove('d)
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
---<img src="../img/logo.jpg" width="16%" align="right">
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
