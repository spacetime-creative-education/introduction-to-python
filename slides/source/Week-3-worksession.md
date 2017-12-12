<img src="../img/logo.jpg" width="16%" align="right">
# Conditionals, Recursion and a little bit of Iteration
### Lather, rinse, repeat

---
layout: false
<img src="../img/logo.jpg" width="16%" align="right">


**Problem-1**

_level: intermediate_

*Exponential of x: Computes the result of x raised to the power of n.*

```
Spec:
Build a function
input parameters: x, n
output: x**n
```
???
Basic implementation
def exp(x, n):
    if n == 0:
        return 1
    else:
        return x * exp(x, n-1)

Faster computation
def fast_exp(x, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return fast_exp(x*x, n/2))
    else:
        return x * fast_exp(x, n-1)
---
layout: false
<img src="../img/logo.jpg" width="16%" align="right">


**Problem-2**

_level: intermediate_

*define a function `fib(n)` that computes the nth term of a fibonacci series.*

```
Spec:
Build a function
input parameters: n
output: n'th fibonacci series term

Example:
n = 5
out = 8
```
???
Basic implementation
def fib(n):
    if n is 0 or n is 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

---
layout: false
<img src="../img/logo.jpg" width="16%" align="right">


**Problem-3**

_level: intermediate_

*Recursive circles using processing*

https://processing.org/examples/recursion.html


???
---
