# Lecture notes

# Strings and Regular Expressions
# see https://thartmanoftheredwoods.github.io/CIS-12/week_8py.html

city = "Eureka"
first_letter = city[0]  # Accessing first character
second_letter = city[1]  # Accessing second character
print("First letter:", first_letter)
print("Second letter:", second_letter)

# Negative index
last_letter = city[-1]
print("Last letter:", last_letter)

# Slicing

sentence = "Programming is fun!"
print("First 11 characters:", sentence[:11])
print("Characters from index 5 to 9:", sentence[5:9])
print("Last 3 characters:", sentence[-3:])

# Immutability

greeting = "Goodbye"
# Attempting to change the first letter results in an error
# greeting[0] = 'H'

# So the correct way is to create a new string using slicing.
new_greeting = "H" + greeting[1:]
print("New greeting:", new_greeting)

# String Comparison

def compare_to_word(word):
    if word < "apple":
        print(f"{word} comes before apple.")
    elif word > "apple":
        print(f"{word} comes after apple.")
    else:
        print("It's apple!")

compare_to_word("Banana")
compare_to_word("pineapple")

# String Methods

message = "Hello, World!"
print("Uppercase:", message.upper())
print("Lowercase:", message.lower())
print("Position of 'World':", message.find("World"))
print("Replacing 'World' with 'Universe':", message.replace("World", "Universe"))

# Reading and Writing Files

# Writing to a file
with open("resources/greeting.txt", "w") as writer:
    writer.write("Hello, World!\nWelcome to Python programming.")

# Reading from a file
with open("resources/greeting.txt", "r") as reader:
    for line in reader:
        print(line.strip())

# Regular Expressions

import re

text = "Welcome to the world of Python programming!"
pattern = r"\bworld\b"  # Matches 'world' as a whole word \b is a word boundary
match = re.search(pattern, text)
if match:
    print("Found 'world' at index:", match.start())
else:
    print("'world' not found")

# String Substitution with Regex

text = "The color of the sky is colorless."
pattern = r"\bcolor\b"
new_text = re.sub(pattern, "colour", text)
print("Modified text:", new_text)

# Exercises

# Slice and Reorder

def half_mirror(str_in):
    half = str_in[:len(str_in)//2]
    mirror = half[::-1]
    return mirror

print(half_mirror('PythonProgramming'))

# Find and Count Patterns

def count_pattern_occurrences(text, pattern):
    match_s = re.findall(pattern, text, re.IGNORECASE)
    print(f'The pattern is seen {len(match_s)} times.')

count_pattern_occurrences('The cat chased the mouse.', 'the')

# File Content Reader

def replace_all(in_file, out_file, pattern, word):
    with open(in_file,'r', encoding = 'utf-8') as in_f, open(out_file, 'w', encoding = 'utf-8') as out_f:
        for line in in_f:
            line = re.sub(pattern, word, line, flags=re.IGNORECASE)
            out_f.write(line)

replace_all('resources/colossus-original.txt', 'resources/colossus-meddled.txt', 'homeless', 'opulent')

# Lists
# see https://thartmanoftheredwoods.github.io/CIS-12/week_8ch9py.html

# Exercises

# Combine and Modify

def join_list_wo_dups(list1, list2):
    new_list = list1 + list2
    return list(set(new_list))

a = [1, 2, 3]
b = ['a', 2, 'c']
print(join_list_wo_dups(a,b))

# List Reversal Without reverse()   TODO not yet finished

def reverse_list(list3):
    elements = list3.split()
    return elements

c = ['no', 1, 2, 'yes']
# print(reverse_list(c))
