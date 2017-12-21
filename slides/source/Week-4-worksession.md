<img src="../img/logo.jpg" width="16%" align="right">
#  Iteration and Strings - Worksession

---
layout: false
<img src="../img/logo.jpg" width="16%" align="right">


**Problem-1**

_level: easy_

*Write a function that checks whether an input string is a palindrome*

```
Spec:
Build a function
input parameters: s
output: True/False

example:
>>> is_palindrome("anna")
>>> True
>>> is_palindrome("racecar")
>>> True
>>> is_palindrome("hello")
>>> False
```
???
basic implementation
def is_palindrome(s):
    s1 = ""
    for c in s:
        s1 = c + s1

    return s == s1

advanced implementation
def is_palindrome(s):
    return s == s[::-1]

---
layout: false
<img src="../img/logo.jpg" width="16%" align="right">


**Problem-2**

_level: intermediate_

*Check if a number is a prime number or not*

```
Spec:
Build a function
input parameters: x
output: True/False

Example:
n = 409
out = True
"409 is a prime number"

n = 407
out = False
"407 is not a prime number. 11 times 37 is 407"
```
???
num = 407

if num > 1:
   # check for factors
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           print(i,"times",num//i,"is",num)
           break
   else:
       print(num,"is a prime number")

else:
   print(num,"is not a prime number")

---
layout: false
<img src="../img/logo.jpg" width="16%" align="right">


**Problem-3**

_level: intermediate_

*Purple rain*

Make daniel shiffmans purple rain on pyprocessing.


???
---
