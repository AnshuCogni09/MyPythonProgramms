# Implement a program to find the largest element in a list using max()

my_numbers = [1, 9, 3, 7]
result = max(my_numbers) 

# Write a program to merge two dictionaries.
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
merged_dict = dict1.update(dict2)
print(merged_dict)

# How do you sort a list of tuples by the second element?
data = [("Apple", 50), ("Banana", 20), ("Cherry", 30)]
sorted_data = sorted(data, key=lambda x: x[1])
print(sorted_data)

# Write a Python program to find the intersection of two lists.
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
intersection = list(set(list1) & set(list2))
print(intersection)

# Implement a function to check if two strings are anagrams.
def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
are_anagrams(str1, str2)

# Write a program to find the second largest number in a list.
numbers = [10, 20, 4, 45, 99]
numbers.sort()
second_largest = numbers[-2]
print("The second largest number is:", second_largest)

# How do you reverse the order of words in a sentence using Python?
sentence = "Hello My Name is Anshumaan"
reversed_sentence = ' '.join(sentence.split()[::-1])
print(reversed_sentence)

# Write a program to generate a random password of length n.


# Implement a program to find the sum of digits of a number.
num3 = int(input("Enter a number: "))
while num3 > 0:
    digit = num3 % 10
    sum += digit
    num3 = num3 // 10
print("Sum of digits:", sum)

# Write a function to remove vowels from a string
def remove_vowels(s):
    vowels = "aeiouAEIOU"
    return ''.join([char for char in s if char not in vowels])

s = input("Enter a string: ")
remove_vowels(s)

# How do you check if a given year is a leap year in Python?
year = int(input("Enter a year: "))
if(year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")