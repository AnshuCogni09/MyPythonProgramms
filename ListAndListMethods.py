# Lists:
# A list is a collection which is ordered and changeable. Allows duplicate members.
# Lists are written with square brackets []. 

mylist = [1,2,"Apple",3.4,True]
print(mylist)

# List slicing:
print(mylist[1])  # Prints elements from index 1 
print(mylist[0:3])  # Prints elements from index 0 to 2
print(mylist[2:])   # Prints elements from index 2 to end

# List Comprehension:

nums = [1,2,3,4,5]
nums = [i*2 for i in nums]
print(nums) 

# List Methods:
nums1 = [1,2,3,4,5]

nums1.append(6)  # Adds an element at the end of the list
nums1.sort()    # Sorts the list
nums1.reverse() # Reverses the list
nums1.insert(2 , 3)  # Inserts an element at a specified position  (2 is the index, 3 is the value)
nums1.index(1)  # Returns the index of the first element with the specified value

print(nums1.count(3))  # Returns the number of elements with the specified value
print(nums1)