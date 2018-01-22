![logo](../img/logo.jpg)

# Assignment - Week 4
We now know about iteration and string indexing

keywords: indexing, slicing, iteration

# 1. Fizz buzz
*Level: Easy*

Let's warm up a bit.

"Fizz buzz" is a word game we will use to teach the robots about division. Let's learn computers.

You should write a function that will receive a positive integer and return:
"Fizz Buzz" if the number is divisible by 3 and by 5;
"Fizz" if the number is divisible by 3;
"Buzz" if the number is divisible by 5;
The number as a string for other cases.

Input: A number as an integer.

Output: The answer as a string.

![robot_division](../img/robot_division.png)

src: [https://py.checkio.org/mission/fizz-buzz/](https://py.checkio.org/mission/fizz-buzz/)

# 2. Digits multiplication
*Level: Easy*

You are given a positive integer. Your function should calculate the product of the digits excluding any zeroes.

For example: The number given is 123405. The result will be 1*2*3*4*5=120 (don't forget to exclude zeroes).

Input: A positive integer.

Output: The product of the digits as an integer.

src: [https://py.checkio.org/mission/digits-multiplication/](https://py.checkio.org/mission/digits-multiplication/)

# 3. Guess the number
*Level: Hard*

Play guess the number with computer.

Rules: The computer will choose a number from 1 to 100, and ask you to guess it.
For each guess, the computer says either

"Your guess is low"
or
"Your guess is high"
and finally
"You got it right! Congrats"

You only get 7 chances to guess the number, if you don't guess it in 7 steps its "Game over".

If you guess it right, you "win". Remember to exit the program after you declared the user to be a winner.

Sample run:
```
Hello, what's your name?
Prashanth

Hi, Prashanth. I have a number from 1 to 100 in my mind. You get 7 chances to guess it. Go.

23
Your guess is low
75
Your guess is high
24
Congrats Prashanth! You got it right in 3 chances.
Game over.
```

In a case when user fails to guess in 7 chances display

```
You lose.
Game over.
```
