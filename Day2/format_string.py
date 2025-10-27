#In Python String formatting means inserting variables or expressions into strings to create dynamic text output.
#Each method has its own advantages and use cases, with f-Strings being the most modern and preferred for their readability and efficiency.

#Types of String Formatting in Python

#1. Old Style (%) Formatting
name = "Alice"
age = 30
formatted_string = "Hello, my name is %s and I am %d years old." % (name, age)
print(formatted_string)
#Output: Hello, my name is Alice and I am 30 years old.

#2. str.format() Method
formatted_string = "Hello, my name is {} and I am {} years old.".format(name, age)
print(formatted_string)
#Output: Hello, my name is Alice and I am 30 years old.

#3. f-Strings (Formatted String Literals) - Python 3.6+
formatted_string = f"Hello, my name is {name} and I am {age} years old."
print(formatted_string)
#Output: Hello, my name is Alice and I am 30 years old.

#4. Template Strings (from the string module)
from string import Template
template = Template("Hello, my name is $name and I am $age years old.")
formatted_string = template.substitute(name=name, age=age)
print(formatted_string)
#Output: Hello, my name is Alice and I am 30 years old.

