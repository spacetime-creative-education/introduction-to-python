<img src="../img/logo.jpg" width="16%" align="right">
# Magic methods
### Creating a list-like object

<img src="../img/lego.jpg" width="50%" align="right">
---
layout: false
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Class Goals

]
.right-column[
    * What are magic methods?
    * Define a new class
    * Make the class list-like step by step
]
---
layout: false
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## What are magic methods?

]
.right-column[
    `Magic methods` or `dunder functions` are special functions that the python
    interpreter looks for in class. By overriding the built-in defaults we can
    hack the nature of how a class should behave.

    Examples of magic functions: `__init__()`, `__contents__()`, `__getitem__()`
]
---
layout: false
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Define a new class

]
.right-column[
    Let's make a class to list all the primary Looney Toons characters. There
    are 15 of them.

    ```python
    class LooneyToons(object):
        def __init__(self):
            """
            Initializes an object. Here we make the list of all characters
            """
            self._characters = ["Elmer Fudd",
                                "Tweety",
                                "Sylvester",
                                "Road Runner",
                                "Wile E. Coyote",
                                "Tasmanian Devil",
                                "Yosemite Sam",
                                "Pepe Le Pew",
                                "Marvin the Martian",
                                "Foghorn Leghorn",
                                "Speedy Gonzales",
                                "Bosko"                               
                                ]
    ```
]
---
layout: false
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Define a new class

]
.right-column[
    Try creating an instance of `LooneyToons` and indexing out the 3rd character.

    ```python
    toons = LooneyToons()
    print(toons[2])
    ```

    We get:

    ```python
    File "<ipython-input-4-40a7b76d28ff>", line 1, in <module>
      toons[2]
    TypeError: 'LooneyToons' object does not support indexing
    ```

    So what should we do?
]
---
layout: false
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Define a new class

]
.right-column[
    We should add indexing support.

    *How?*
    Add the `__getitem__()` method

    ```python
    class LooneyToons(object):
        def __init__(self):
            ...

        def __getitem__(self, key):
            return self._characters.pop(key)

    print(toons[2])
    ```

    We get:

    ```python
    Sylvester
    ```

    Great. Now lets handle runtime errors and make life better.
]
---
layout: false
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Define a new class

]
.right-column[
    ```python
    class LooneyToons(object):
        def __init__(self):
            ...

        def __getitem__(self, key):
            """
            The rules are that we can access an item only once per instance.
            Once indexed, it pops out.
            :param key:
            :return:
            """
            if isinstance(key, int):
                if key < len(self._characters) and key >= 0:
                    return self._characters.pop(key)
                else:
                    raise ValueError("Key {KEY} cannot be reached".format(KEY=key))
            else:
                raise TypeError("Key {KEY} needs to be an integer".format(KEY=key))
    ```
]
---

layout: false
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Define a new class

]
.right-column[
    What happens when we want to check if an item exists in this object.

    ```python
    characters = LooneyToons()
    print("Tweety" in characters)
    ```

    ```python
    ValueError: Key 6 cannot be reached
    ```

    What's happening now?

    There are definitely more than 6 items. If it failed, why didn't it fail for item 1 itself?
]
---

layout: false
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Define a new class

]
.right-column[
    The reason is, `__getitem__()` is used in the background.

    Each time it is triggered, an item is popped out of the list, also the key
    is incremented by 1 after calling `__getitem__()` once.

    When the key increments to 6, there isn't 6 items in the list.
]
---
layout: false
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Define a new class

]
.right-column[
    How to fix this?

    Use `__contains__`. This is a special magic function and `__getitem__` is more
    generic. Which means if `__contains__` is implemented, python will leave `__getitem__`
    for comparison.

    ```python
        ...
        def __contains__(self, item):
            return item in self._characters
    ```
]
---

layout: false
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Define a new class

]
.right-column[
    Awesome, can I plug this object to a for loop?
    ```python
        toons = LooneyToons()
        for item in toons:
            print(item)
    ```

    We get:

    ```python
    ValueError: Key 6 cannot be reached
    ```

    Same error? So `__getitem__` is used unnecesarily.

    So how to fix this?
]
---
layout: false
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Define a new class

]
.right-column[
    implement `__iter__()`.

    ```python
        ...
        def __contains__(self, item):
            return item in self._characters


        def __iter__(self):
            while self._characters:
                yield self._characters.pop()

    ```

]
---
layout: false
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Define a new class

]
.right-column[
    What about length of the object.

    ```python
        toons = LooneyToons()
        print(len(toons))
    ```

    More errors, no `len()`. Fix?

    ```python
        ...
        def __len__(self):
            return len(self._characters)
    ```
]
---
layout: false
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Define a new class

]
.right-column[
    That's some basics of magic functions. There are a lot more that can be overridden!

    and many cool features can be coded using them.
]
---
