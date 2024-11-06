# Strings are immutable - they don't change

# Creating strings with single and double quotes
single_quote = 'Single quotes are great'
double_quote = "So are double quotes"
print(single_quote)
print(double_quote)

# Multi-line string using triple quotes
multi_line = """This is a 
string that
spans multiple lines!"""
print("\nMulti-line String:")
print(multi_line)

# String indexing
word = "Coding Temple"
print("\nString Indexing:")
print(word[0])
print(word[1])  
print(word[-1])
print(word[-2])

# Concatenation of strings
greeting = "Why hello"
name = "George"
full_greeting = greeting + ", " + name + "!"
print("\nConcatenation:")
print(full_greeting)
print(1 + 2)
print("1" + "2")

# Repeat strings with *
laugh = "Ha" * 3 + "!"
print("\nString Repetition:")
print(laugh) 
print("-" * 20)

# Finding the length of a string
phrase = "I'm not lazy, I'm on energy-saving mode."
length_of_phrase = len(phrase)
print("\nLength of Phrase:")
print(length_of_phrase) 

# String slicing (substrings)
language = "Slice me up!"
print("\nString Slicing Examples:")
print(language[0:4]) 
print(language[3:])   
print(language[3:9])  
print(language[-5:])  

# Convert to uppercase and lowercase
message = "Hello, Python!"
print("\nUppercase and Lowercase:")
print(message.upper()) 
print(message.lower())  


# Remove whitespace from start and end of a string
# check out lstrip and rstrip if you want!
whitespace_string = "   Trim this!   "
print("\nstrip() removes whitespace:")
print(whitespace_string.strip())  

# Replace part of a string
text = "I love Java!"
print("\nReplace Example:")
print(text.replace("Java", "Python"))
print(text)

# Split and join
sentence = "Python rocks our world"
words = sentence.split()
print("\nSplit Example:")
print(words)
print(words[0])

joined_sentence = ",".join(words)
print("\nJoin Example:")
print(joined_sentence)


# Check if a string starts or ends with a specific substring
filename = "super_secret_file.txt"
print("\nStartswith and Endswith:")
print(filename.startswith("my"))  
print(filename.startswith("super"))  
print(filename.endswith(".txt"))  


# String formatting with .format()
name = "Fred"
age = 99
print("\nString Formatting with .format():")
print("My name is {} and I am {} years old.".format(name, age))

# String formatting with f-strings
game_genre = "action-adventure"
game = "The Last of Us"
print("\nString Formatting with f-strings:")
print(f"My favorite game in the {game_genre} genre is \"{game}\".") 

# More string methods: finding a substring and counting occurrences
long_text = "Python is powerful. Python is versatile. Python is everywhere!"
print("\nFind and Count Examples:")
print(long_text.find("Python"))   
print(long_text.count("Python"))

# Using slicing and immutability demonstration
original_text = "Jython"
fixed_text = "P" + original_text[1:]
print("\nFixing Strings by Slicing:")
print(f"Original text: {original_text}")
print(f"Fixed text: {fixed_text}")

# title and capitalize
text = "hello world"
print("\nTitle and Capitalize:")
print(text.capitalize())  
print(text.title())       

# isdigit - Check if a string consists only of digits, 
text = "12345"
print("\nisdigit example:")
print(text.isdigit())      