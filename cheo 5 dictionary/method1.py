# Creating a dictionary
student = {
    "name": "Rahul",
    "age": 20,
    "course": "BCA"
}

print("Original Dictionary:", student)

# 1. keys() → returns all keys
print("Keys:", student.keys())

# 2. values() → returns all values
print("Values:", student.values())

# 3. items() → returns all key-value pairs as tuples
print("Items:", student.items())

# 4. get(key) → safely access value, returns None if key not found
print("Get name:", student.get("name"))
print("Get grade (not exist):", student.get("grade"))

# 5. update({...}) → add/update multiple key-value pairs
student.update({"age": 21, "grade": "A"})
print("After update:", student)

# 6. pop(key) → removes key and returns its value
removed = student.pop("course", "Not Found")  # safe removal
print("Removed:", removed)
print("After pop:", student)

# 7. popitem() → removes last inserted key-value pair
last_item = student.popitem()
print("Last item removed:", last_item)
print("After popitem:", student)

# 8. setdefault(key, default) → returns value of key, 
#    if key not exist adds it with default value
print("Setdefault grade:", student.setdefault("grade", "B"))
print("Setdefault city:", student.setdefault("city", "Almora"))
print("After setdefault:", student)

# 9. copy() → returns a shallow copy of dictionary
student_copy = student.copy()
print("Copied Dictionary:", student_copy)

# 10. clear() → removes all items from dictionary
student.clear()
print("After clear:", student)  # {}
