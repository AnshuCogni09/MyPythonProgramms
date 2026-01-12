# Functions are used to encapsulate resuable blocks of code.

def calculateGmean(a,b):
    gmean = (a*b)/(a+b)
    print("Geometric Mean is:",gmean)

a=4
b=6
calculateGmean(a,b)

# There are two types of functions:
# 1. Built-in functions: These are pre-defined functions provided by Python, 
# such as print(), len(), type(), etc.

# 2. User-defined functions: These are functions created by users to perform specific tasks, 
# like the calculateGmean function above.

# There are 4 different types
# 1. Default Arguments
# 2. Keyword Arguments
# 3. Variable-length Arguments
# 4. Required Arguments

# Default Arguments:
def name(fname, mname = "Narayan", lname = "Panda"):
    print("Full Name is:", fname, mname, lname)

name("Rudra")

# Keyword Arguments:
def name1(fname, mname, lname):
    print("Full Name is:", fname, mname, lname)

name1(lname="Panda", fname="Rudra", mname="Narayan")

# Variable-length Arguments:
# Two ways to achieve this:
# Arbitrary Arguments:

def name2(*names):
    print("Hello", names[0], names[1], names[2])

name2("Rudra", "Narayan", "Panda")

# Keyword Arbitrary Arguments:

def name3(**names):
    print("Hello", names['fname'], names['mname'], names['lname'])

name3(lname="Panda", fname="Rudra", mname="Narayan")

# Required Arguments:
# These are the arguments that are passed to a function in correct positional order.
def name4(fname, mname, lname):
    print("Full Name is:", fname, mname, lname)

name4("Rudra", "Narayan", "Panda")

# Return Statement:
# The return statement is used to exit a function and return a value to the caller.

def sum(a, b):
    return a + b

result = sum(5, 10)
print("Sum is:", result)