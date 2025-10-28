#Dictionary implementation in Python
"""
In Python, dictionaries are written with curly brackets.
    Dictionaries do not allow duplicate members.
    Dictionaries are used to store data values in key:value pairs.
    Each key-value pair in a dictionary is separated by a comma.
    Dictionaries do not have a indexing system like lists; instead, they use keys to access values.
    Diconaries can store heterogeneous data types as values.
    
    When to use a dictionary:
    1. When you need a logical association between a key:value pair.
    2. When you need fast lookup for your data, based on a custom key.
    3. When you need to store data that is not ordered.
    4. When you need to ensure that keys are unique.
    
    Dictionary Vs List:
    1. Lists are ordered collections of items, while dictionaries are unordered collections of key-value pairs.
    2. Lists allow duplicate values, whereas dictionary keys must be unique.
    3. Lists are accessed via their index positions, while dictionaries are accessed via their keys.
    4. Lists are suitable for ordered data, while dictionaries are ideal for associative arrays or mappings.
    

    Dictionary Methods:
    1. keys() - Returns a view object containing the keys of the dictionary
    2. values() - Returns a view object containing the values of the dictionary
    3. items() - Returns a view object containing the key-value pairs of the dictionary
    4. clear() - Removes all the elements from the dictionary
    5. copy() - Returns a copy of the dictionary
    6. fromkeys() - Returns a dictionary with the specified keys and value
    7. get() - Returns the value of the specified key   
    8. pop() - Removes the element with the specified key
    9. popitem() - Removes the last inserted key-value pair
    10. setdefault() - Returns the value of the specified key; if the key does not exist, insert the key with a specified value
    11. update() - Updates the dictionary with the specified key-value pairs
    
"""

#Example of a dictionary
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
print(person)  # Output: {'name': 'John', 'age': 30, 'city': 'New York'}

#Accessing elements in a dictionary
print(person["name"])  # Output: John
print(person.get("age"))  # Output: 30

#Modifying elements in a dictionary
person["age"] = 31
print(person)  # Output: {'name': 'John', 'age': 31, 'city': 'New York'}

#Adding elements to a dictionary
person["job"] = "Engineer"
print(person)  # Output: {'name': 'John', 'age': 31, 'city': 'New York', 'job': 'Engineer'}

#Removing elements from a dictionary
person.pop("city")
print(person)  # Output: {'name': 'John', 'age': 31, 'job': 'Engineer'}

#Popping elements from a dictionary
"""
Pop method removes the element with the specified key and returns its value.
"""
#Example of pop method
popped_age = person.pop("age")
print(popped_age)  # Output: 31
print(person)  # Output: {'name': 'John', 'job': 'Engineer'}

#Getting keys, values, and items from a dictionary
keys = person.keys()
print(keys)  # Output: dict_keys(['name', 'job'])
values = person.values()
print(values)  # Output: dict_values(['John', 'Engineer'])
items = person.items()
print(items)  # Output: dict_items([('name', 'John'), ('job', 'Engineer')])

#Dictionary with different data types
mixed_dict = {
    "name": "Alice",
    "age": 25,
    "is_student": True,
    "courses": ["Math", "Science"],
    "address": {"city": "Los Angeles", "state": "CA"}
}
print(mixed_dict)  # Output: {'name': 'Alice', 'age': 25, 'is_student': True, 'courses': ['Math', 'Science'], 'address': {'city': 'Los Angeles', 'state': 'CA'}}

#Overriding a dictionary
person.update({"age": 32, "city": "San Francisco"})
print(person)  # Output: {'name': 'John', 'job': 'Engineer', 'age': 32, 'city': 'San Francisco'}

#Printing specific elements of a dictionary
print("Name:", person["name"])  # Output: Name: John
print("State:", mixed_dict["address"]["state"])  # Output: State: CA


