<img src="../img/logo.jpg" width="16%" align="right">
#  List

---
layout: false
<img src="../img/logo.jpg" width="16%" align="right">


**Problem-1**

_level: easy_

*Find the minimum number in the given list*

Use the following code to generate a random list of numbers from 1 to 100
```
x = [random.randint(1, 100) for x in range(20)]
print(x)

# find the minimum number in the list by traversing the list
```
???
---
layout: false
<img src="../img/logo.jpg" width="16%" align="right">


**Problem-2**

_level: intermediate_

*Windowed average*

Given a list with length N, and a window size W, such that W < N

make a list of size N - W + 1, using a moving window to average the numbers

Sample output:
```
>>> numbers = [2, 4, 6, 8, 10]    # N = 5
>>> W = 2
>>> #then the averages would be as follows
>>> averages = [3, 5, 7, 9]    # length = N - W + 1
```
???
---
