# Local Variable
def my_function():
    x = 10  # Local variable
    print("Local variable x:", x)
my_function()

# Global Variable
y = 20  # Global variable
def another_function():
    print("Global variable y:", y)
another_function()

# Using both local and global variables
z = 30  # Global variable
def combined_function():
    a = 5  # Local variable
    print("Local variable a:", a)
    print("Global variable z:", z)
combined_function()
# print(a) -> Compile time Error: NameError: name 'a' is not defined
print("Global variable z outside function:", z)
