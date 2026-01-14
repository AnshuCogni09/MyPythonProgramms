str1 = input("Enter the String: ")
print(str1[::-1])

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: ")) 
print("Before Swapping: ")
a,b = b,a
print("After Swapping: ")
print("First number:", a)
print("Second number:", b)

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

n = int(input("Enter a number to find its factorial: "))
factorial(n)


def fibonacci(n1):
    if n <= 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n1 = int(input("Enter the number of terms in Fibonacci series: "))
fibonacci(n1)


def remove_duplicates(input_list):
    return list(set(input_list)) 

# Write a Python program to count the frequency of each word in a string.
input_string = input("Enter a string: ")
words = input_string.split()
word_frequency = {}
for word in words:
    if word in word_frequency:
        word_frequency[word] += 1
    else:
        word_frequency[word] = 1


def is_palindrome(s):
    return s == s[::-1] 

s = input("Enter a string to check if it's a palindrome: ")
is_palindrome(s)

#Write a function to flatten a nested list.
nested_list = [[1, 2, 3], [4, 5], [6, 7]]
flattened_list = [item for sublist in nested_list for item in sublist]
print(flattened_list) 

