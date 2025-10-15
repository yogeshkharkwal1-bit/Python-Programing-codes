# Creating a dictionary
student = {
    "name": "Rahul",
    "age": 20,
    "course": "BCA"
}

print(student["name"])   # Access value → Rahul
print(student.get("age")) # Another way → 20

# Adding new key-value pair
student["grade"] = "A"

# Updating value
student["age"] = 21

# Removing key
del student["course"]

print(student)

print(student.items())

print(student.keys())

print(student.values())

student.update({"name":"yogi","age":18,"name1":"shubh","age1":19})

print(student)

