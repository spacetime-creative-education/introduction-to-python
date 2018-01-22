![logo](../img/logo.jpg)

# Assignment - Week 1
The blocks we saw so far are functions like `print(), input(), help(), type(), int(), str(), bool()` etc. We also saw how strings have `methods` inbuilt that help us manipulate string data.

keywords: datatype, string, math ops

# 1. Temperature converter
*Level: Easy*

Ask user to enter temperature in celcius and print the converted temperature in Farenheit.

*Sample run*

  Enter Temperature (celcius): 20
  Temperature in Farenheit: 68

# 2. Repeat word
*Level: Easy*

1. Ask user to enter any word
2. Ask user the number (N) of times they want the word repeated
3. print the word N times

Sample Output:

  Enter a word: blah
  Repeat for N times: 4
  Output:
  blahblahblahblah

# 3. Economic Order Quantity
*Level: Hard*

Economic Order Quantity is a model to determine the order quantity to optimize your inventory level in production scheduling. It states that this optimal quantity is dependent on fixed setup/ordering cost (S), holding cost (H), and quantity demanded of that product (D). To be more specific: Optimal quantity equals to the square root of (2*D*S)/H. Create a method to calculate this! Note: Round your answer to the nearest integer.

use the below template code and edit it to achieve the solution.

  ```
  import math

  # to find square root of any number, feed it to math.sqrt() and retrieve the result
  # example
  # x = math.sqrt(4)
  # x == 2 would be True

  S = input('Enter fixed setup/ordering cost: ')
  D = input('Enter quantity demanded of that product: ')
  S = input('Enter holding cost: ')

  # Convert the above inputs to the right datatypes and create a formula to compute the result.
  # Print the result to the user
  ```

# 4. Triangle test
*Level: Intermediate*

Create a program that takes three numbers as inputs and returns True or False depending on whether those three numbers can form a triangle. Three numbers can form a triangle if the sum of any two sides is greater than the third side.
