# Tuples :
# Tuples are immutable sequences in Python that can store a collection of items.
# Tuples are written with round brackets ().

mytuple = (1, 2, "Apple", 3.4, True)
print(mytuple)

# Tuple Slicing:
print(mytuple[1])  # Prints element at index 1

# Check immutability:
try:
    mytuple[1] = "Banana"  # Attempting to change an element (will raise an error)
except TypeError as e:
    print("Error:", e)

# Tuple Comprehension (using generator expression):
nums = (1, 2, 3, 4, 5)
nums = tuple(i * 2 for i in nums)
print(nums)


# tuple manipulation:
# Since tuples are immutable, we can convert them to a list to perform modifications
nums1 = (1, 2, 3, 4, 5)
nums1 = list(nums1)  # Convert tuple to list
nums1.append(6)  # Adds an element at the end of the list
nums1.sort()    # Sorts the list
nums1.insert(2,3)
nums1 = tuple(nums1)  # Convert back to tuple

print(nums1)

# Tuple Methods:
mytuple2 = (1, 2, 3, 2, 4, 2)
res = mytuple2.count(2)  # Returns the number of occurrences of the specified value
print(res)