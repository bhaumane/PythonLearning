#Tuples in Python
"""
In Python, tuples are written with round brackets.
    Tuples allow duplicate members.
    Tuples are used to store multiple items in a single variable.
    Each item in a tuple is separated by a comma.
    Tuples are ordered and unchangeable (immutable).
    Tuples can store heterogeneous data types as values.
    
    When to use a tuple:
    1. When you need an ordered collection of items that should not change.
    2. When you want to ensure data integrity by preventing modification.
    3. When you need to use tuples as keys in dictionaries (since they are immutable).
    4. When you want to group related data together.

    Tuple Vs List:
    1. Tuples are immutable, while lists are mutable (can be changed).
    2. Tuples use parentheses (), while lists use square brackets [].
    3. Tuples can be used as keys in dictionaries, while lists cannot.
    4. Tuples are generally faster than lists for certain operations due to their immutability.

    Tuple Methods:
    1. count() - Returns the number of times a specified value occurs in a tuple
    2. index() - Searches the tuple for a specified value and returns its position
"""
#Example of a tuple
fruits = ("apple", "banana", "cherry")
print(fruits)  # Output: ('apple', 'banana', 'cherry')

#Accessing elements in a tuple
print(fruits[0])  # Output: apple
print(fruits[1])  # Output: banana

#Tuples are immutable, so we cannot modify elements in a tuple
#The following line would raise an error if uncommented
# fruits[1] = "blueberry"  # This will raise a TypeError

#Tuples can be concatenated to create a new tuple
more_fruits = ("orange", "grape")
all_fruits = fruits + more_fruits
print(all_fruits)  # Output: ('apple', 'banana', 'cherry', 'orange', 'grape')

#Counting occurrences of an element in a tuple
count_banana = all_fruits.count("banana")
print(count_banana)  # Output: 1

#Finding the index of an element in a tuple
index_cherry = all_fruits.index("cherry")
print(index_cherry)  # Output: 2

#Single element tuple
single_fruit = ("apple",)
print(single_fruit)  # Output: ('apple',)
print(type(single_fruit))  # Output: <class 'tuple'>

#Tuple unpacking
fruit1, fruit2, fruit3 = fruits
print(fruit1)  # Output: apple
print(fruit2)  # Output: banana
print(fruit3)  # Output: cherry

#Nested tuples
nested_tuple = (("apple", "banana"), ("cherry", "date"))
print(nested_tuple)  # Output: (('apple', 'banana'), ('cherry', 'date'))
print(nested_tuple[0])  # Output: ('apple', 'banana')
print(nested_tuple[0][1])  # Output: banana

#Tuple length
print(len(all_fruits))  # Output: 5