We need Python 3 (Miniconda or Anaconda) for this project

We also need jupyter notebook installed. A handy extenstion is RISE, which
enables presenation using ipynbs.

RISE Installation

From the most simple to the most complex one, you have 3 options:

1 - Using conda (recommended):

```
conda install -c damianavila82 rise
```

2 - Using pip (less recommended):

```
pip install RISE
```

and then two more steps to install the JS and CSS in the proper places:

```
jupyter-nbextension install rise --py --sys-prefix
```

and enable the nbextension:

```
jupyter-nbextension enable rise --py --sys-prefix
```