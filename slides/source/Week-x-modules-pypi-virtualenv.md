<img src="../img/logo.jpg" width="16%" align="right">
# Modules, Packages, Virtualenv and Pypi


<img src="../img/code_pack_ship.png" width="100%" align="center">
---
layout: false
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Class Goals

]
.right-column[
    * Create your modules and packages.

    * How to work with virtual environments?

    * How to upload your package on Pypi? So that you can share what you create with the world
]
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Modules
]
.right-column[
  Any `.py` file you make is a module. Basically, if you store your python code, you are creating modules. Simple.

  This thing about modules are they are reusable. Check this out

  ```python
  # module: area.py
  def square(length):
      return length**2

  def triangle(base, height):
      return 0.5*base*height
  ```
]
???
---

<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Modules
  ## - Reuse modules
]
.right-column[
  *How to reuse a module?*

  You can import a module by firing up the python interpreter in that directory and `import`ing the module using the module name.

  The module name is the filename without the `.py` extension.

  ```python
  >>> import area
  >>> l = 20
  >>> A = area.square(l)
  >>> print("Area: ", A)
  'Area: 400'
  ```
]
???
---

<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Modules
  ## - Reuse modules
]
.right-column[
  Each module has an attribute `__name__` associated with it that's set to the name of the module. Like:

  ```python
  >>> import area
  >>> area.__name__
  'area'
  ```
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Modules
  ## - Reuse modules
  ## - Commandline arguments
]
.right-column[
  You can execute modules as a script by using the following pattern

  ```python
  # module: area.py
  def ...

  if __name__ == "__main__":
      import sys
      if sys.argv[1] == "square":
          l = int(sys.argv[2])
          print("Area: ", square(l))
      elif sys.argv[1] == "triangle":
          b = int(sys.argv[2])
          h = int(sys.argv[3])
          print("Area: ", triangle(b, h))
      else:
          ...
  ```
  A module's `__name__` attr is set to `"__main__"` when run as a script
]
???
---

<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Modules
  ## - Reuse modules
  ## - Commandline arguments
]
.right-column[
  You can run this script from a command prompt or terminal like this:

  ```shell
  /path/to/module $ python area.py square 20
  Area: 400
  ```
]
???
---

<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Modules
  ## - Reuse modules
  ## - Commandline arguments
]
.right-column[
  when we import a module, the interpreter searches in the following order:

  1. If there is a built-in module of the same name
  2. If this module is present in `sys.path`
     `sys.path` is initialize from these locations:
     a. The directory containing a script which imports the module
     b. Or the current working directory if we are importing from the python commandline
     c. In any location from `PYTHONPATH` environment variable
     d. If the module is installed, then a installation dependent location might be searched for.
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Modules
  ## - Reuse modules
  ## - Commandline arguments
]
.right-column[
  You can use the `dir()` function to find out which names a module defines.

  ```shell
  >>> import area
  >>> dir(area)
  ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'square', 'triangle']
  ```

  Note that it lists all types of names: variables, modules, functions, etc.
]
???
If you want to list builtins, try `dir(__builtins__)`
---

<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Modules
  ## - Reuse modules
  ## - Commandline arguments
  ## Packages
]
.right-column[
  If you want to better structure your code, so that you can access multiple modules, under one module name, by using `dot` notation, you need a package.

  Packages are collection of modules. Like this:

  ```
  sound/                          Top-level package
      __init__.py               Initialize the sound package
      formats/                  Subpackage for file format conversions
              __init__.py
              wavread.py
              wavwrite.py
              ...
      effects/                  Subpackage for sound effects
              __init__.py
              echo.py
              surround.py
              ...
      filters/                  Subpackage for filters
              __init__.py
              equalizer.py
              vocoder.py
              ...
    ```
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Packages
]
.right-column[
  The `__init__.py` file just asks the interpreter to treat the directory as a package.

  The `__init__.py` simply can be empty, or it can have some initialization code that needs to be run before the `import` of the package.

  ```
  sound/                          Top-level package
      __init__.py               Initialize the sound package
      formats/                  Subpackage for file format conversions
              __init__.py
              wavread.py
              wavwrite.py
              ...
      effects/                  Subpackage for sound effects
              __init__.py
              echo.py
              surround.py
              ...
      filters/                  Subpackage for filters
              __init__.py
              equalizer.py
              vocoder.py
              ...
    ```
]
???
---

<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Packages
  ## - Accessing package elements
]
.right-column[
  You can access code from any module in a package by using the dot notation like this:

  ```
  import sound.effects.echo
  ```

  Another variation is:

  ```
  >>> from sound.effects.echo import echofilter
  >>> echofilter(input, output, delay=0.7, atten=4)
  ```
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Packages
  ## - Accessing package elements
  ## `from package import *`
]
.right-column[
  `from package import *`

  asks the interpreter to import ALL from the package. But as we would hope, it will not import ALL submodules in a package level module. Infact, if will only import all the modules that are specified in the `__all__` attribute set in `__init__.py` of the package.

  For example, the `file sound/effects/__init__.py` could contain the following code:

  `__all__ = ["echo", "surround", "reverse"]`
]
???
---

<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Packages
  ## - Accessing package elements
  ## `from package import *`
  ## Relative imports
]
.right-column[
  When packages are structured into subpackages, you can use absolute imports to refer to submodules of siblings packages.

  `from sound.effects import echo.`

  You can also write relative imports

  ```python
  from . import echo
  from .. import formats
  from ..filters import equalizer
  ```
  Here `.` means *current*, `..` means *higher directory*. You can also use `...` if the package has so much depth.


]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Virtualenv
]
.right-column[
  virtualenv is a tool to create *isolated Python environments*

  virtualenv creates a folder which contains all the necessary executables to use the packages that a Python project would need.

  *Its a good practice to create virtual environments for all your major projects, and maintain seperate packages list*
]
???
---

<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Virtualenv
]
.right-column[
  To install `virtualenv` do:

  `pip install virtualenv`

  Test the installation using

  `virtualenv --version`

]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Virtualenv
]
.right-column[
  To create a new virtual environment, open a terminal and

  ```shell
  cd project_folder
  virtualenv env_name
  ```
  If you want to specify a python interpreter to be used, do:

  ```
  virtualenv -p /usr/bin/python2.7 env_name
  ```
  This will create a virtualenv with the python 2.7 interpreter
]
???
---

<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Virtualenv
]
.right-column[
  To work with a virtualenv you need to activate it.

  open a terminal and go to the project folder.

  Then you can do

  ```
  $ source env_name/bin/activate
  (env_name) $
  ```
  When you see `(env_name)` in front of the $ sign, you know that you are in the environment. You can now do normal stuff like `(env_name) $ python script.py` to execute your script.

  To deactivate, simple type `deactivate` :

  `(env_name) $ deactivate`
]
???
---

<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Virtualenv
]
.right-column[
  To add any dependency of your project, simply do `pip install <package-name>` from inside the virtualenv.

  Also, after you are done with your project, you can collect the list of dependencies in a text file using the command

  `pip freeze > requirements.txt`

  This helps your user setup their environment easily. They can install all the dependencies in one go using the command:

  `pip install -r requirements.txt`

  Just a tip:
  > Make sure you never add the virtualenv files to your version control.

]
???
virtualenvwrapper provides a set of commands which makes working with virtual environments much more pleasant
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Pypi
]
.right-column[
  Pypi is PYthon Package Index, and is where `pip` searches for the package you request to be installed.

  The cool thing is you can also submit your packages to Pypi free of cost.

  There is also a testPypi which can be used to test our package on the python index, without messing up with the real index. Let's go ahead and submit our `area.py` module to testPypi
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Pypi
]
.right-column[
  Let's get started. Keep your package ready. I made up a `volume.py` along with `area.py` in a package called `shapes`.

  ```
  shapes /
    __init__.py
    area.py
    volume.py
  ```

  Once that's ready, go to [https://testpypi.python.org/pypi](https://testpypi.python.org/pypi) and register for an account.
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Sumbitting package to Pypi
  ## - Getting started
]
.right-column[
  Create a `.pypirc` file. (On windows, use PyCharm or your python text editor to do this)

  ```
  [distutils]
  index-servers =
    pypi
    pypitest

  [pypi]
  repository=https://pypi.python.org/pypi
  username=your_username
  password=your_password

  [pypitest]
  repository=https://testpypi.python.org/pypi
  username=your_username
  password=your_password
  ```
  You need not have the `password=your_password` keypair in this file, for the sake of security. You will be asked for the password when the actual upload will take place later.
]
???
On linux do chmod 600 ~/.pypirc
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Sumbitting package to Pypi
  ## - Getting started
  ## - Preparing your package
]
.right-column[
  Every package on Pypi needs a `setup.py` file in the root of the package directory.

  This is how the `setup.py` should look like:

  ```
  from distutils.core import setup
  setup(
    name = 'mypackage',
    packages = ['mypackage'], # this must be the same as the name above
    version = '0.1',
    description = 'A random test lib',
    author = 'Peter Downs',
    author_email = 'peterldowns@gmail.com',
    url = 'https://github.com/peterldowns/mypackage', # use the URL to the github repo
    download_url = 'https://github.com/peterldowns/mypackage/archive/0.1.tar.gz', # I'll explain this in a second
    keywords = ['testing', 'logging', 'example'], # arbitrary keywords
    classifiers = [],
  )
```
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Sumbitting package to Pypi
  ## - Getting started
  ## - Preparing your package
]
.right-column[
  You need to tell Pypi where your README document is. Which can be a `README.rst` file created in the root of the package.

  OR

  You can create a `README.md` file if you prefer Markdown over rst, but you will have to add another text file `setup.cfg` which points to `README.md`, like this:

  ```
  [metadata]
  description-file = README.md
  ```
]
???
---

<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Sumbitting package to Pypi
  ## - Getting started
  ## - Preparing your package
]
.right-column[
  You will also have to add a `LICENSE.txt` file in the root of the package. This file should contain the LICENCE terms such as the text from [MIT LICENSE](https://opensource.org/licenses/MIT)
]
???
---

<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Sumbitting package to Pypi
  ## - Getting started
  ## - Preparing your package
  ## - Upload your package
]
.right-column[
```
python setup.py register -r pypitest
```
This will attempt to register your package against PyPI's test server, just to make sure you've set up everything correctly.

now run:

```
python setup.py sdist upload -r pypitest
```
You should get no errors, and should also now be able to see your library in the [test PyPI repository](https://testpypi.python.org/pypi).

The steps to upload to the live PyPi is similar.

```
python setup.py register -r pypi
python setup.py sdist upload -r pypi
```
and you're done! Congratulations on successfully publishing your first package!
]
???
You can also use Twine to upload a pypi package
---
