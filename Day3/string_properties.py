#String Properties in Python
"""
    Slicing: Extracting a portion of a string or list using indices.
    Indexing: Accessing individual characters in a string or elements in a list using their position.
    Immutability: Strings are immutable, meaning they cannot be changed after creation, while lists are mutable.
    Length: The number of characters in a string or elements in a list can be determined using the len() function.
    Concatenation: Combining strings or lists using the + operator.
    Membership: Checking if a substring exists within a string or an element exists within a list using the 'in' keyword.
    Iteration: Looping through each character in a string or each element in a list using loops.
    multiline strings: Strings that span multiple lines, created using triple quotes .
    immutable: Strings cannot be changed after they are created, while lists can be modified.
    multipilable: Strings can be multiplied by an integer to repeat them, e.g., "abc" * 3 results in "abcabcabc".
    check content:To check the content of a string using "is in" and "not in" keywords.
"""
text = "Hello, welcome to the world of Python programming!"
#Immutability example
try:
    text[0] = "h"
except TypeError as e:
    print("Immutability Error:", e)
#Multipilable example
repeated_text = text * 2
print("Repeated text:", repeated_text)
#Length example
length = len(text)
print("Length of the text:", length)
#Concatenation example
concatenated_text = text + " Enjoy coding!"
print("Concatenated text:", concatenated_text)
#Membership example
is_in = "Python" in text
print("Is 'Python' in text?:", is_in)
is_not_in = "Java" not in text
print("Is 'Java' not in text?:", is_not_in)
#Iteration example
print("Characters in the text:")
for char in text:
    print(char, end='')
print()
#Multiline string example
multiline_text = """This is a multiline string.
It spans multiple lines."""
print("Multiline string:", multiline_text)