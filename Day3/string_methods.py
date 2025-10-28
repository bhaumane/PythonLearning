#String Methods in Python

"""
    upper(): Converts all characters in a string to uppercase.
    lower(): Converts all characters in a string to lowercase.
    split(): Splits a string into a list of substrings based on a specified delimiter.
    join(): Joins a list of strings into a single string with a specified delimiter.
    find(): Searches for a substring within a string and returns the index of its first occurrence.
    replace(): Replaces occurrences of a specified substring with another substring.
    strip(): Removes leading and trailing whitespace from a string.
    startswith(): Checks if a string starts with a specified substring.
    endswith(): Checks if a string ends with a specified substring.
    count(): Counts the occurrences of a substring in a string.
    format(): Formats a string by replacing placeholders with specified values.
    isalpha(): Checks if all characters in a string are alphabetic.
    isdigit(): Checks if all characters in a string are digits.
    isspace(): Checks if all characters in a string are whitespace.
    capitalize(): Capitalizes the first character of a string.
    title(): Converts the first character of each word in a string to uppercase.
    center(): Centers a string within a specified width by padding it with spaces.
    ljust(): Left-justifies a string within a specified width by padding it with spaces.
    rjust(): Right-justifies a string within a specified width by padding it with spaces.

"""
text = "Hello, welcome to the world of Python programming!"
# Using upper() method
upper_text = text.upper()
print("Uppercase:", upper_text)
# Using lower() method
lower_text = text.lower()
print("Lowercase:", lower_text)
# Using split() method
split_text = text.split(" ")
print("Split text:", split_text)
# Using join() method
joined_text = "-".join(split_text)
print("Joined text with '-':", joined_text)
# Using find() method
find_index = text.find("Python")
print("Index of 'Python':", find_index)
# Using replace() method
replaced_text = text.replace("Python", "Java")
print("Replaced text:", replaced_text)