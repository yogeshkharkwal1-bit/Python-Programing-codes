# 1. Concatenation (+)

# Joining two tuples together.

t1 = (1, 2, 3)
t2 = (4, 5)
t3 = t1 + t2
print(t3)   # (1, 2, 3, 4, 5)

# 2. Repetition (*)

# Repeating elements multiple times.

t = (10, 20)
print(t * 3)   # (10, 20, 10, 20, 10, 20)

# 3. Indexing

# Accessing elements by position (just like lists).

t = (5, 10, 15, 20)
print(t[0])   # 5
print(t[-1])  # 20

# 4. Slicing

# Extracting parts of a tuple.

t = (1, 2, 3, 4, 5)
print(t[1:4])   # (2, 3, 4)
print(t[:3])    # (1, 2, 3)

# 5. Membership (in, not in)

# Check if element exists.

t = (10, 20, 30)
print(20 in t)      # True
print(40 not in t)  # True

# 6. Iteration (looping)

# Loop through tuple elements.

t = ('a', 'b', 'c')
for i in t:
    print(i)

# 7. Length (len())

# Find number of elements.

t = (1, 2, 3, 4)
print(len(t))   # 4

# 8. Min / Max / Sum

# (works if all elements are numbers)

t = (5, 8, 2, 10)
print(min(t))   # 2
print(max(t))   # 10
print(sum(t))   # 25

# 9. Nested Tuples

# Tuples inside tuples.

t = (1, (2, 3), (4, 5))
print(t[1])      # (2, 3)
print(t[1][0])   # 2

# 10. Tuple Packing and Unpacking

# Assigning multiple values.

# Packing

t = 1, 2, 3
print(t)   # (1, 2, 3)

# Unpacking
a, b, c = t
print(a, b, c)   # 1 2 3