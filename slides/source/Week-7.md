<img src="../img/logo.jpg" width="16%" align="right">
# Files and Databases, Exception handling

<img src="../img/database.png" width="50%" align="right">
---
layout: false
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Class Goals

]
.right-column[
  Topics

  * File handling

  * Exception handling  
  ]
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Persistence
]
.right-column[
  Most programs we wrote till now works like **run and forget**. The data created during the program is destroyed at the end of it.

  Another way to code, is to make the data **persistent**, which means atleast some parts of the data is stored on a harddisk.

  Examples of persistent programs: OS, Web servers.
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Persistence
  ## - text files
]
.right-column[
  A common place to store information is in text files. There are all kinds of text formats used to store data, like CSV files, JSON, or just plain .txt files.

  We will see how to create, read and write them.
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Persistence
  ## - text files
]
.right-column[
  consider this folder structure.

  project_folder
      |
      \ app.py
        sample.txt

  if you want to open the text file, you can do:

  ```python
  fp = open("sample.txt", "r")
  text = fp.read()
  fp.close()
  print(text)
  ```
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Persistence
  ## - text files
]
.right-column[
  ```python
  fp = open("sample.txt", "r")
  text = fp.read()
  fp.close()
  print(text)
  ```

  `open()` takes the `filepath` as the first arg and the the `mode` as the second.

  `r` - read mode.
  Reference to different file modes: https://docs.python.org/3/library/functions.html#open
]
???
---

<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Persistence
  ## - text files
]
.right-column[
  You can also read files line by line.

  1. To read a single line
  ```python
  fp = open("sample.txt", "r")
  text = fp.readline()
  fp.close()
  print(text)
  ```

  2. To plug the lines as a sequence to for loop


  ```python
  fp = open("sample.txt", "r")
  for line in fp:
      print(line)
  fp.close()
  ```
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Persistence
  ## - text files
]
.right-column[
  After opening an instance of the file and working on it, you should always close it.

  To make matters more easier. Python exposes a handler that will open and close automatically for you. This code pattern is the **context manager** triggered using the **with** statement.

  ```python
  with open("sample.txt", "r") as fp:
      text = fp.read()
      print(text)
  ```
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Persistence
  ## - text files
]
.right-column[
  **problem-1**

  Read this file of Alice in Wonderland and find the histogram of the words in it.

  https://ia801405.us.archive.org/18/items/alicesadventures19033gut/19033.txt
]
???
---

<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Persistence
  ## - text files
]
.right-column[
  Further explore:

  * OS library
  * Jupyter notebooks
  * Beautiful code

]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Dictionary
]
.right-column[
]
???
**Note: some topics to explore next class are, Jupyter notebooks, tuples (week-5 pending), set, introduction to test based development, collections, sorting,  
---
