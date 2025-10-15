
# Creating a set
fruits = {"apple", "banana", "cherry"}
print("Original Set:", fruits)

# 1. add() → adds a single element
fruits.add("mango")
print("After add:", fruits)

# 2. update() → adds multiple elements (from list, tuple, set etc.)
fruits.update(["grapes", "orange"])
print("After update:", fruits)

# 3. remove() → removes element, error if not present
fruits.remove("banana")
print("After remove banana:", fruits)

# 4. discard() → removes element, no error if not present
fruits.discard("pineapple")  # not in set, but no error
print("After discard pineapple:", fruits)

# 5. pop() → removes and returns a random element
removed = fruits.pop()
print("Randomly removed:", removed)
print("After pop:", fruits)

# 6. clear() → removes all elements
temp = fruits.copy()   # making copy before clearing
temp.clear()
print("After clear:", temp)

# 7. copy() → returns shallow copy of set
fruits_copy = fruits.copy()
print("Copied Set:", fruits_copy)

# ------------------------------
# Set Operations
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# 8. union() → A ∪ B
print("Union:", A.union(B))

# 9. intersection() → A ∩ B
print("Intersection:", A.intersection(B))

# 10. difference() → A - B
print("Difference (A-B):", A.difference(B))
print("Difference (B-A):", B.difference(A))

# 11. symmetric_difference() → elements in A or B but not both
print("Symmetric Difference:", A.symmetric_difference(B))

# ------------------------------
# Set Relationship methods
C = {1, 2}
D = {1, 2, 3, 4}

# 12. issubset() → C ⊆ D
print("Is C subset of D?", C.issubset(D))
print(D.issubset(C))
# 13. issuperset() → D ⊇ C
print("Is D superset of C?", D.issuperset(C))

# 14. isdisjoint() → True if sets have no common elements
E = {7, 8}
print("Are D and E disjoint?", D.isdisjoint(E))
