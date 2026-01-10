# Anything written in the double quotes is considered a string in Python.
name = "Anshumaan"
print("Hello, " + name)

# Double quotes cannot be used inside double quotes directly.
# tripple quotes can be used as an multiline string delimiter.
quote = '''The only limit to our realization of tomorrow
is our doubts of today.'''

print(quote)

for char in name:
    print(char, end=' ')