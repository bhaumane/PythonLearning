#Rounding in Python
#Rounding is the process of reducing the number of significant digits in a number. 
#In Python, there are several ways to round numbers, each serving different purposes.

#1. Using the built-in round() function
num1 = 5.6789
rounded_num1 = round(num1)  # Rounds to the nearest integer
print(rounded_num1)  # Output: 6
rounded_num2 = round(num1, 2)  # Rounds to 2 decimal places
print(rounded_num2)  # Output: 5.68
#Output:
#6
#5.68

#2. Using the math.floor() and math.ceil() functions
import math
num2 = 5.6789
floored_num = math.floor(num2)  # Rounds down to the nearest integer
print(floored_num)  # Output: 5
ceiled_num = math.ceil(num2)  # Rounds up to the nearest integer
print(ceiled_num)  # Output: 6
#Output:
#5
#6