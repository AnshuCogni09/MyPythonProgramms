# Sets:
# A set is an unordered collection data type and has no duplicate elements.
# Sets are mutable.
# Sets are defined by values separated by commas inside curly braces {}.
# Sets sort the elements in an ascending order by default.

set1 = {1,2,5,3,8,4}
print("Set 1:", type(set1) ,set1)

set2 = {1,"apple", 3.5, True}
print("Set 2:", type(set2), set2)

for i in set1:
    print(i , end=" ")


# Set Methods:
# Union() - Returns a set that contains all items from both sets, duplicates are excluded.

set3 = set1.union(set2)
print("\nUnion of Set 1 and Set 2:", set3)

# Intersection() - Returns a set that contains the similarity between two or more sets.
print(set1.intersection(set2))

# Symmetric Difference() - Returns a set that contains all items from both sets, except items that are present in both sets.
print(set1.symmetric_difference(set2))

# Disjoint() - Returns True if two sets have a null intersection.
print(set1.isdisjoint(set2))

# Subset() - Returns True if all items in the set exists in the specified set.
print(set1.issubset(set3))

# Superset() - Returns True if all items in the specified set exists in the original set.
print(set3.issuperset(set1))

# remove() - Removes the specified item from the set.
set1.remove(3)
print("Set 1 after removing 3:", set1)

# pop() - Removes and returns an arbitrary set item.
removed_item = set1.pop()
print("Removed item:", removed_item)
print("Set 1 after pop:", set1)