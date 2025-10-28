#Indexing in Python

"""
Types of Indexing:
Python supports two types of indexing:
    1. Positive Indexing
        - Starts from 0 on the leftmost element.
        - Used to access elements from the beginning.
    2. Negative Indexing
        - Starts from -1 on the rightmost element.
        - Used to access elements from the end.

-Accessing a single element with an invalid index → ❌ IndexError.
-But slices don’t throw errors — they just return an empty list or valid subset.
-You cannot use float or string as an index.

Slicing in Python:
Slicing allows you to extract a portion of a sequence (like a list, string, or tuple) by specifying a start index, an end index, and an optional step. 
The syntax for slicing is: sequence[start:end:step]
- start: The index where the slice starts (inclusive). Default is 0.
- end: The index where the slice ends (exclusive). Default is the length of the sequence.
- step: The interval between each index in the slice. Default is 1.

rindex() Method:
    rindex() is a string method that searches for a substring inside another string 
    — just like find() or index() — but it searches from the right (end).
    It returns the highest index (rightmost position) where the substring is found.

"""

my_list = ['apple', 'banana', 'cherry', 'date']
# Accessing elements using positive indexing
first_item = my_list[0]  # 'apple'
second_item = my_list[1] # 'banana'
# Accessing elements using negative indexing
last_item = my_list[-1]  # 'date'
second_last_item = my_list[-2] # 'cherry'
print(f"First item: {first_item}, Second item: {second_item}")
print(f"Last item: {last_item}, Second last item: {second_last_item}")

# Slicing in Python
sub_list = my_list[1:3]  # ['banana', 'cherry']
print(f"Sliced list (index 1 to 2): {sub_list}")
# Demonstrating slicing with step
step_list = my_list[0:4:2]  # ['apple', 'cherry']
print(f"Sliced list with step (index 0 to 3 with step 2): {step_list}")

# String indexing
my_string = "Hello, World!"
first_char = my_string[0]  # 'H'
last_char = my_string[-1]  # '!'
print(f"First character: {first_char}, Last character: {last_char}")
# String slicing
greeting = my_string[0:5]  # 'Hello'
print(f"Greeting from string slicing: {greeting}")
# Demonstrating slicing with step in strings
step_string = my_string[0:13:2]  # 'Hlo ol!'
print(f"Sliced string with step (index 0 to 12 with step 2): {step_string}")
# Demonstrating full string slicing
full_string = my_string[:]  # 'Hello, World!'
print(f"Full string using slicing: {full_string}")
# Demonstrating slicing with omitted start and end
omitted_slice = my_list[::2]  # ['apple', 'cherry']
print(f"Sliced list with omitted start and end (step 2): {omitted_slice}")
# Demonstrating reverse slicing
reverse_list = my_list[::-1]  # ['date', 'cherry', 'banana', 'apple']
print(f"Reversed list using slicing: {reverse_list}")   
# Demonstrating slicing with omitted start and end
omitted_string_slice = my_string[::3]  # 'Hl r!'
print(f"Sliced string with omitted start and end (step 3): {omitted_string_slice}")
# Demonstrating reverse slicing for strings
reverse_string = my_string[::-1]  # '!dlroW ,olleH'
print(f"Reversed string using slicing: {reverse_string}")   

#Find and display the index of the first occurrence of the word "practice" in the following sentence:
#"In theory, theory and practice are the same. In practice, they are not."
sentence = "In theory, theory and practice are the same. In practice, they are not."
index_of_practice = sentence.index("practice")
print(f"The index of the first occurrence of the word 'practice' is: {index_of_practice}")
#output: The index of the first occurrence of the word 'practice' is: 22

#Find and display the index of the last occurrence of the word "practice" in the following sentence:
#"In theory, theory and practice are the same. In practice, they are not."
last_index_of_practice = sentence.rindex("practice")
print(f"The index of the last occurrence of the word 'practice' is: {last_index_of_practice}")
#output: The index of the last occurrence of the word 'practice' is:  48