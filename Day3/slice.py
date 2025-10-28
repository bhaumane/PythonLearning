#Slicing in Python

# This script demonstrates various ways to slice string / sentance in Python.
text = "Hello, welcome to the world of Python programming!"
# Slicing from index 0 to 5
slice1 = text[0:5]
print("Slice from index 0 to 5:", slice1)
# Slicing from index 7 to 14
slice2 = text[7:14]
print("Slice from index 7 to 14:", slice2)
# Slicing with a step of 2
slice3 = text[::2]
print("Slice with a step of 2:", slice3)
# Slicing the last 10 characters
slice4 = text[-10:]
print("Last 10 characters:", slice4)
# Slicing to get every second character from index 5 to 20
slice5 = text[5:20:2]
print("Every second character from index 5 to 20:", slice5)
# Reversing the string using slicing
slice6 = text[::-1]
print("Reversed string:", slice6)
# Slicing from index 10 to the end
slice7 = text[10:]
print("Slice from index 10 to the end:", slice7)
# Slicing from the start to index 15
slice8 = text[:15]
print("Slice from the start to index 15:", slice8)
# Slicing with negative step to get every second character in reverse
slice9 = text[20:5:-2]
print("Every second character from index 20 to 5 in reverse:", slice9)
# Slicing the first 20 characters
slice10 = text[:20]
print("First 20 characters:", slice10)
# Slicing the middle part of the string
slice11 = text[10:30]
print("Middle part of the string (index 10 to 30):", slice11)

#Slicing the list
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Slicing from index 2 to 5
list_slice1 = numbers[2:6]
print("List slice from index 2 to 5:", list_slice1)
# Slicing with a step of 3
list_slice2 = numbers[::3]
print("List slice with a step of 3:", list_slice2)
# Slicing the last 4 elements
list_slice3 = numbers[-4:]
print("Last 4 elements of the list:", list_slice3)
# Reversing the list using slicing
list_slice4 = numbers[::-1]
print("Reversed list:", list_slice4)
# Slicing from index 4 to the end
list_slice5 = numbers[4:]
print("List slice from index 4 to the end:", list_slice5)
# Slicing from the start to index 7
list_slice6 = numbers[:7]
print("List slice from the start to index 7:", list_slice6)
# Slicing with negative step to get every second element in reverse
list_slice7 = numbers[8:2:-2]
print("Every second element from index 8 to 2 in reverse:", list_slice7)
# Slicing the first 5 elements
list_slice8 = numbers[:5]
print("First 5 elements of the list:", list_slice8)
# Slicing the middle part of the list
list_slice9 = numbers[3:8]
print("Middle part of the list (index 3 to 8):", list_slice9)