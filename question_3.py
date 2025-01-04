#5.	Write a Python program that asks the user to enter a text and return a dictionary whose keys are the words of the text entered and the values are the lengths of the words that make up the text.
#Example for the text T = "Python is a programming language", the program must return the dictionary:
#d = {'Python': 6, 'is': 2, 'a': 1, 'language': 8, 'de': 2, 'programming': 13}

user_input = input("Enter a text: ")
lengths = {}
for word in user_input.split():
    lengths[word] = len(word)
print(lengths)
