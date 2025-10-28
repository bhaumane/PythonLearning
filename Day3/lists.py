#List in Python
""" 
    A list is a collection which is ordered and changeable. 
    In Python, lists are written with square brackets.
    Lists allow duplicate members.

    When to use a list:
    1. When you need an ordered collection of items.
    2. When you need to modify the collection (add, remove, or change items).
    3. When you need to store multiple items in a single variable.
    4. When you need to access items by their index positions.

    Sort function in lists:
    The sort() method sorts the list in ascending order by default.
    You can also sort the list in descending order by setting the reverse parameter to True.
        1. fruits.sort() - Sorts the list in ascending order
        2. fruits.sort(reverse=True) - Sorts the list in descending order
        3. sorted(fruits) - Returns a new sorted list from the elements of any iterable

    
    List Methods:
    1. append() - Adds an element at the end of the list
    2. insert() - Adds an element at the specified position
    3. remove() - Removes the first item with the specified value
    4. pop() - Removes the element at the specified position
    5. clear() - Removes all the elements from the list
    6. index() - Returns the index of the first element with the specified value
    7. count() - Returns the number of elements with the specified value
    8. sort() - Sorts the list in ascending order
    9. reverse() - Reverses the order of the list
    10. copy() - Returns a copy of the list
    11. extend() - Adds the elements of a list (or any iterable), to the end of the current list
    12. sorted() - Returns a new sorted list from the elements of any iterable
"""
#Example of a list
fruits = ["apple", "banana", "cherry"]
print(fruits)  # Output: ['apple', 'banana', 'cherry']
#Accessing elements in a list
print(fruits[0])  # Output: apple
print(fruits[1])  # Output: banana
#Modifying elements in a list
fruits[1] = "blueberry"
print(fruits)  # Output: ['apple', 'blueberry', 'cherry']
#Adding elements to a list
fruits.append("orange")
print(fruits)  # Output: ['apple', 'blueberry', 'cherry', 'orange']
#Removing elements from a list
fruits.remove("cherry")
print(fruits)  # Output: ['apple', 'blueberry', 'orange']
#Popping elements from a list
"""
Pop method removes the element at the specified position. If no index is specified, 
the last element is removed and returned.
"""
#Example of pop method
#Removing the last element
popped_fruit = fruits.pop()
print(popped_fruit)  # Output: orange
print(fruits)  # Output: ['apple', 'blueberry']
#Removing the element at index 0
popped_fruit = fruits.pop(0)
print(popped_fruit)  # Output: apple
print(fruits)  # Output: ['blueberry']

#Sorting a list
fruits = ["banana", "apple", "cherry"]
fruits.sort()
print(fruits)  # Output: ['apple', 'banana', 'cherry']
#Reversing a list
fruits.reverse()
print(fruits)  # Output: ['cherry', 'banana', 'apple']
#Copying a list
fruits_copy = fruits.copy()
print(fruits_copy)  # Output: ['cherry', 'banana', 'apple']
#Extending a list
more_fruits = ["kiwi", "mango"]
fruits.extend(more_fruits)
print(fruits)  # Output: ['cherry', 'banana', 'apple', 'kiwi', 'mango']
#Using sorted() to sort a list
numbers = [5, 2, 9, 1]
sorted_numbers = sorted(numbers)
print(sorted_numbers)  # Output: [1, 2, 5, 9]
print(numbers)  # Output: [5, 2, 9, 1] (original list remains unchanged)
#Counting occurrences of an element
fruits = ["apple", "banana", "apple", "cherry"]
apple_count = fruits.count("apple")
print(apple_count)  # Output: 2
#Finding the index of an element
banana_index = fruits.index("banana")
print(banana_index)  # Output: 1
#Clearing a list
fruits.clear()
print(fruits)  # Output: []

#What does the sort() function return for the list 
social_networks = ["YouTube","Facebook", "Twitter", "Whatsapp"]
social_networks.sort()
print(social_networks)  # Output: ['Facebook', 'Twitter', 'Whatsapp', 'YouTube']
#The sort() method sorts the list in place and returns None.