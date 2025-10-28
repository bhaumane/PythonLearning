text = input("Enter the text:")
randon_letters = input("Enter three random letters separated by spaces:" ).split() [:3]
print(randon_letters)

# Count occurrences of each letter in the text
letter1_count = text.count(randon_letters[0])
letter2_count = text.count(randon_letters[1])
letter3_count = text.count(randon_letters[2])
print(f"The letter '{randon_letters[0]}' occurs {letter1_count} times.")
print(f"The letter '{randon_letters[1]}' occurs {letter2_count} times.")
print(f"The letter '{randon_letters[2]}' occurs {letter3_count} times.")

# Count total number of words in the text
word_count = len(text.split())
print(f"The total number of words in the text is: {word_count}")

# Extract and print the first and last letters of the text
first_letter = text[0]
last_letter = text[-1]
print(f"The first letter of the text is: '{first_letter}'")
print(f"The last letter of the text is: '{last_letter}'")

# Invert and print the text
iverted_text = text[::-1]
print("The inverted text is:", iverted_text)

# Check if the word "python" is in the text (case insensitive)
print("Is python in text:", "python" in text.lower())
