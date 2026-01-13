# Dictionaries:
# A dictionary is a collection of key-value pairs. 
# Each key is unique and is used to access its corresponding value.

dict = {"name": "Alice", "age": 30, "city": "New York"}
print(dict) 

print(dict["name"])
print(dict.keys())
print(dict.values())

dict2 = {2464396:"Anshumaan",
         2464093:"Rudra",
         2463431:"Priyanshu"}

print(dict2.keys())
print(dict2.values())
print(dict2[2464396])

# Dictionary Methods:
# 1. get(): Returns the value for a specified key.
print(dict.get("age")) 

# 2. items(): Returns a view object containing the key-value pairs.
print(dict.items()) 

# 3. update(): Updates the dictionary with elements from another dictionary.
dict.update({"country": "USA"})         
print(dict)

# 4. pop(): Removes the item with the specified key and returns its value.
age = dict.pop("age")
print(age)
print(dict) 

# 5. clear(): Removes all items from the dictionary.
# dict.clear()
# print(dict)

# 6. copy(): Returns a shallow copy of the dictionary.
dict_copy = dict.copy()
print(dict_copy)   

# 7. fromkeys(): Creates a new dictionary with keys from an iterable and values set to a specified value.
keys = ["a", "b", "c"]
new_dict = dict.fromkeys(keys, 0)
print(new_dict)

# 8. setdefault(): Returns the value of a specified key. If the key does not exist, it inserts the key with a specified value.
value = dict.setdefault("age", 25)
print(value)
print(dict)

# 9. popitem(): Removes and returns the last inserted key-value pair as a tuple.
last_item = dict.popitem()
print(last_item)
print(dict)

# 10. len(): Returns the number of items in the dictionary.
length = len(dict)
print(length)
print(dict)

# 11. del: Deletes an item with the specified key.
del dict["city"]
print(dict)