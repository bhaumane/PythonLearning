#Sets in Python
"""
In Python, sets are written with curly brackets {} or the set() function.
    For Example: set1 = {"apple", "banana", "cherry"} or set2 = set(["apple", "banana", "cherry"])
    Sets do not allow duplicate members.
    Sets are used to store multiple items in a single variable.
    Each item in a set is separated by a comma.
    Sets are unordered and unindexed.
    Sets can store heterogeneous data types as values.
    
    When to use a set:
    1. When you need to store unique items.
    2. When you need to perform mathematical set operations like union, intersection, difference, and symmetric difference.
    3. When you want to eliminate duplicate values from a collection.
    4. When you need fast membership testing.

    Set Vs List:
    1. Sets do not allow duplicate values, while lists allow duplicates.
    2. Sets are unordered collections, while lists are ordered collections.
    3. Sets are optimized for membership testing, while lists are not.
    4. Sets support mathematical set operations, while lists do not.
    5. List would not be supported data type for sets because lists are mutable and unhashable.

    Set Methods:
    1. add() - Adds an element to the set
    2. remove() - Removes the specified element from the set
    3. discard() - Removes the specified element from the set if it is present
    4. pop() - Removes and returns an arbitrary element from the set
    5. clear() - Removes all the elements from the set
    6. union() - Returns a set containing the union of sets
    7. intersection() - Returns a set containing the intersection of sets
    8. difference() - Returns a set containing the difference of sets
    9. symmetric_difference() - Returns a set containing the symmetric difference of sets
    10. issubset() - Returns True if the set is a subset of another set
    11. issuperset() - Returns True if the set is a superset of another set
"""

#Example of a set
fruits = {"apple", "banana", "cherry"}
print(fruits)  # Output: {'banana', 'cherry', 'apple'}

#Adding elements to a set
fruits.add("orange")
print(fruits)  # Output: {'banana', 'cherry', 'orange', 'apple'}

#Removing elements from a set
fruits.remove("banana")
print(fruits)  # Output: {'cherry', 'orange', 'apple'}

#Popping an arbitrary element from a set
popped_fruit = fruits.pop()
print(popped_fruit)  # Output: (arbitrary element, e.g., 'cherry')
print(fruits)  # Output: (remaining elements, e.g., {'orange', 'apple'})

#Union of two sets
set1 = {"apple", "banana"}
set2 = {"cherry", "date"}
union_set = set1.union(set2)
print(union_set)  # Output: {'banana', 'cherry', 'date', 'apple'}

#Intersection of two sets
set3 = {"apple", "banana", "cherry"}
set4 = {"banana", "cherry", "date"}
intersection_set = set3.intersection(set4)
print(intersection_set)  # Output: {'banana', 'cherry'}

#Difference of two sets
difference_set = set3.difference(set4)
print(difference_set)  # Output: {'apple'}

#Symmetric difference of two sets
symmetric_difference_set = set3.symmetric_difference(set4)
print(symmetric_difference_set)  # Output: {'apple', 'date'}

#Checking subset and superset
set5 = {"apple", "banana"}
set6 = {"apple", "banana", "cherry", "date"}
is_subset = set5.issubset(set6)
print(is_subset)  # Output: True

is_superset = set6.issuperset(set5)
print(is_superset)  # Output: True

#Clearing a set
fruits.clear()
print(fruits)  # Output: set()

#Creating a set from a list (eliminating duplicates)
numbers_list = [1, 2, 2, 3, 4, 4, 5]
numbers_set = set(numbers_list)
print(numbers_set)  # Output: {1, 2, 3, 4, 5}
#Set length
print(len(numbers_set))  # Output: 5

#Membership testing
print(3 in numbers_set)  # Output: True
print(6 in numbers_set)  # Output: False

#Dicarding an element from a set
numbers_set.discard(2)
print(numbers_set)  # Output: {1, 3, 4, 5}
#Trying to discard an element not present in the set (no error)
numbers_set.discard(10)
print(numbers_set)  # Output: {1, 3, 4, 5}

#Discard vs Remove
# Using remove() on an element not present will raise a KeyError
# numbers_set.remove(10)  # This will raise a KeyError

#Example of a frozen set (immutable set)
frozen_fruits = frozenset(["apple", "banana", "cherry"])
print(frozen_fruits)  # Output: frozenset({'banana', 'cherry', 'apple'})
#Trying to add an element to a frozen set (will raise an error if uncommented)
# frozen_fruits.add("orange")  # This will raise an AttributeError


