import re

story = """Tony Stark, also known as Iron Man, can be contacted at tony@starkindustries.com or at 123-456-7890.
Steve Rogers, aka Captain America, can be reached via email steve@shield.gov or on his office number 987-654-3210.
Thor's email is thor@asgard.com and his phone number is 555-123-4567.
Bruce Banner's contact info: email: bruce@hulk.com, phone: 666-777-8888.
Natasha Romanoff uses the email blackwidow@shield.com and her phone number is 111-222-3333.
"""

# [ ]: Matches any one character within the brackets.
# a-z: It matches a range of lowercase alphabetic character from a to z.
lowercase_letters = re.findall(r'[a-z]', story)
print("\nLowercase letters found:", lowercase_letters)


# Using the raw string (r"") to avoid escape character issues
# if we didn't use r we would have to do '\\d{3}-\\d{3}-\\d{4}'
# \d: Matches any digit from 0 to 9. 
# {3}: Specifies that exactly 3 digits in a row should be matched
# The hyphen - is treated as a literal character
# findall() - searches a given string for all matches to a specified regular 
#   expression pattern and return them as a list
raw_pattern = r'\d{3}-\d{3}-\d{4}'
phone_matches = re.findall(raw_pattern, story)
print("\nPhone numbers that matched pattern:", phone_matches)


# \w: matches any "word character" - Lower and uppercase letters (a-zA-Z) | Digits (0-9) | The underscore (_).
# +: means "one or more" of the preceding element. So, \w+ matches one or more word characters.
# Lookahead assertion (?=...) - Check for words followed by a specific pattern 
#   - So it's basically matching words that come before the '@' symbol (email usernames)
lookahead_pattern = re.findall(r'\w+(?=@)', story)
print("\nWords before '@':", lookahead_pattern)

# [a-zA-Z0-9._%+-]: this matches any one of the characters inside the square brackets:
#   a-z: lowercase letters | A-Z: uppercase letters | 0-9: digits | .: a literal dot (.) 
#   _: underscore | %: percent sign | +: plus sign | -: hyphen.
# +: one or more of the characters inside the brackets must appear
# @: The literal @ symbol
# 
# [a-zA-Z0-9.-]: matches:
#   a-zA-Z0-9: letters and digits.
#   .: literal dot, which separates subdomains in domain names.
#   -: hyphen, often used in domain names
# +: This quantifier means one or more of the characters from the above set
# 
# \.: A literal dot. 
#   In regular expressions, a dot is a special character that matches any character. 
#   The backslash \ escapes it
# 
# [a-zA-Z]: A character class that matches uppercase and lowercase letters.
# {2,}: This quantifier means that at least 2 letters are required. 
#   This matches: .com, .org, .net, .uk, .us, etc. 
#   The {2,} ensures that TLDs like .uk (2 characters) or .info (4 characters) are matched
#                          fred        @google         .  com
emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', story)
print("\nEmails found:", emails)


# re.search() - finds the first occurrence of the regex pattern anywhere in the 
#   string and returns a match object. If no match is found, it returns None.
# Tony Stark: looking for the actual string "Tony Stark" in side of story
# .: Matches any single character (except newline characters).
# *: Means "zero or more" of the preceding character (in this case, any character).
# Because the phone number pattern is in parenthesis (\d{3}-\d{3}-\d{4}) 
#   that means it is captured in a group, so you can extract it with .group(1) after a successful match.  
search_result = re.search(r'Tony Stark.*(\d{3})-(\d{3})-(\d{4})', story)
if search_result:
    print(f"\nTony Stark's full group: {search_result.group(0)}")
    print(f"Tony Stark's phone number pulled from a group: {search_result.group(1)}")
    print(f"Tony Stark's phone number pulled from a group: {search_result.group(2)}")
    print(f"Tony Stark's phone number pulled from a group: {search_result.group(3)}")
    
# re.match() - determines if a regular expression pattern matches at the beginning of a string
match_result = re.match(r'Tony Stark', story)
if match_result:
    print("\nStory begins with \"Tony Stark\"", match_result.group())
else:
    print("\nStory doesn't begin with \"Tony Stark\"")
    
    
# re.sub() - finds pattern matches and replaces them with provided string and 
#   returns a new string with the matched parts replaced by the replacement string.
updated_story = re.sub(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', '[email protected]', story)
updated_story = re.sub(r'\d{3}-\d{3}-\d{4}', '[phone redacted]', updated_story)
print("\nUpdated Story (Emails and Phone Numbers replaced):\n", updated_story)


# re.split() - splits a string and returns a list of substrings based on the 
#   matches of a regular expression pattern
split_story = re.split(r'\d{3}-\d{3}-\d{4}', story)
print("\nStory split by phone numbers:", split_story)


############## BONUS STUFF BELOW

# Anchoring with ^ and $ - Check if a string starts or ends with a pattern
start_match = re.search(r'^Tony', story)  # Starts with 'Tony'
if start_match:
    print("\nStory starts with:", start_match.group())

end_match = re.search(r'Natasha$', story)  # Ends with 'Natasha'
if end_match:
    print("\nStory ends with:", end_match.group())
    
    

# Character Classes: \d, \D, \w, \s - Find all digits, non-digits, words, and whitespace
digits = re.findall(r'\d', story)  # Match digits
print("\nDigits found:", digits)

non_digits = re.findall(r'\D', story)  # Match non-digits
print("\nNon-digits found:", non_digits)

words = re.findall(r'\w+', story)  # Match words
print("\nWords found:", words)

whitespaces = re.findall(r'\s+', story)  # Match whitespaces
print("\nWhitespace characters:", whitespaces)


# The first capturing group: (\b[A-Z][a-z]+)
# \b: A word boundary.  Defines where a word begins or ends.
# [A-Z]: matches a single uppercase letter from A to Z. This is the first letter of the word.
# [a-z]:matches a lowercase letter (from a to z)
# +: means one or more occurrences of lowercase letters following the initial uppercase letter.
# ( and ): parentheses are used to capture the matched part of the string into a group.
# The literal space between the two words ensures that there is at least one space separating the two words.

# The second capturing group (\b[A-Z][a-z]+):
# This is identical to the first capturing group
# finditer() - find all matches of a pattern in a string, returning an iterator 
#   that produces match objects for each match found.
pattern = r'(\b[A-Z][a-z]+) (\b[A-Z][a-z]+)'
print("\nFirst and Last Names Found:")
for match in re.finditer(pattern, story):
    print(f"First Name: {match.group(1)}, Last Name: {match.group(2)}")