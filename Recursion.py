# Recursion:
# It is the process in which a function calls itself directly or indirectly.

def factorial(n):
    if n==1 or n==0:
        return 1
    else:
        return n*factorial(n-1)

num = int(input("Enter a number to find its factorial: "))
result = factorial(num)
print(f"The factorial of {num} is {result}")


def fibonacci(n):
    if n<=0:
        return 1
    elif n==1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

num1 = int(input("Enter a number to find its Fibonacci value: "))
result1 = fibonacci(num1)
print(f"The Fibonacci value at position {num1} is {result1}")