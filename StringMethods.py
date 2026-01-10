name = "Anshumaan"

# we will be using String Methods

print(name.upper())  # Converts to uppercase
print(name.lower())  # Converts to lowercase
print(name.capitalize())  # Capitalizes the first letter
print(name.find('s'))  # Finds the index of first occurrence of 's'
print(name.replace('a', '@'))  # Replaces 'a' with '@'

print(name.split('u'))  # Splits the string at 'u' , returns a list

print(name.startswith('An'))  # Checks if string starts with 'An'
print(name.endswith('hi'))  # Checks if string ends with 'hi'
print(name.count('a'))  # Counts occurrences of 'a'

print(name.isalpha())  # Checks if all characters are alphabetic
print(name.isdigit())  # Checks if all characters are digits

print(name.strip())  # Removes leading and trailing whitespace

print(name.center(20, '*'))  # Centers the string with '*' padding

print(name.swapcase())  # Swaps case of each character

print(name.title())  # Converts to title case
print(name.encode())  # Encodes the string to bytes

print(name.partition('sh'))  # Partitions the string at 'sh', returns a tuple

print(name.rfind('a'))  # Finds the index of last occurrence of 'a'

print(name.islower())  # Checks if all characters are lowercase
print(name.isupper())  # Checks if all characters are uppercase
print(name.expandtabs())  # Expands tabs to spaces