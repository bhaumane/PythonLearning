#Operators in Python
#Operators are special symbols or keywords that perform operations on one or more operands (values or variables) to produce a new value. Python supports a variety of operators, which can be categorized into several types:

#1. Arithmetic Operators
a = 10
b = 3
print(a + b)  # Addition: 13
print(a - b)  # Subtraction: 7
print(a * b)  # Multiplication: 30
print(a / b)  # Division: 3.3333...

print(a // b) # Floor Division: 3
print(a % b)  # Modulus: 1
print(a ** b) # Exponentiation: 1000
#Output:
#13
#7
#30
#3.3333333333333335
#3
#1
#1000

#2. Comparison Operators
x = 5
y = 10
print(x == y)  # Equal to: False
print(x != y)  # Not equal to: True
print(x > y)   # Greater than: False
print(x < y)   # Less than: True
print(x >= y)  # Greater than or equal to: False
print(x <= y)  # Less than or equal to: True
#Output:
#False
#True
#False
#True
#False
#False

#3. Logical Operators
p = True
q = False
print(p and q) # Logical AND: False
print(p or q)  # Logical OR: True
print(not p)   # Logical NOT: False
#Output:
#False
#True
#False

#4. Assignment Operators
c = 5
c += 3  # Equivalent to c = c + 3
print(c)  # Output: 8
c *= 2  # Equivalent to c = c * 2
print(c)  # Output: 16
#Output:
#8
#16

#5. Bitwise Operators
m = 6  # Binary: 110
n = 3  # Binary: 011
print(m & n)  # Bitwise AND: 2 (Binary: 010)
print(m | n)  # Bitwise OR: 7 (Binary: 111)
print(m ^ n)  # Bitwise XOR: 5 (Binary: 101)
print(~m)     # Bitwise NOT: -7 (Binary: ...11111001
print(m << 1) # Left Shift: 12 (Binary: 1100)
print(m >> 1) # Right Shift: 3 (Binary: 011)
#Output:
#2
#7
#5
#-7
#12
#3

#6. Membership Operators
list1 = [1, 2, 3, 4, 5]
print(3 in list1)    # True
print(6 not in list1) # True
#Output:
#True
#True

#7. Identity Operators
a = [1, 2, 3]
b = a
c = a[:]
print(a is b)  # True, because b references the same object as a
print(a is c)  # False, because c is a new object with the same content
print(a == c)  # True, because a and c have the same content
#Output:
#True
#False
#True