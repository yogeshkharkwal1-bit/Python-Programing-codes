# 1. Concatenation (+)

t1 = (1, 2, 3)
t2 = (4, 5)
t3 = t1 + t2
print(t3)   # (1, 2, 3, 4, 5)

# 2. Repetition (*)

t = (10, 20)
print(t * 3)   # (10, 20, 10, 20, 10, 20)

# 3. Indexing

t = (5, 10, 15, 20)
print(t[0])   # 5
print(t[-1])  # 20

# 4. Slicing

t = (1, 2, 3, 4, 5)
print(t[1:4])   # (2, 3, 4)
print(t[:3])    # (1, 2, 3)

# 5. Membership (in, not in)

t = (10, 20, 30)
print(20 in t)      # True
print(40 not in t)  # True

# 6. Iteration (looping)

t = ('a', 'b', 'c')
for i in t:
    print(i)

# 7. Length (len())

t = (1, 2, 3, 4)
print(len(t))   # 4

# 8. Min / Max / Sum

t = (5, 8, 2, 10)
print(min(t))   # 2
print(max(t))   # 10
print(sum(t))   # 25

# 9. Nested Tuples

t = (1, (2, 3), (4, 5))
print(t[1])      # (2, 3)
print(t[1][0])   # 2

# Assigning multiple values.

# Packing

t = 1, 2, 3
print(t)   # (1, 2, 3)

# Unpacking
a, b, c = t
print(a, b, c)   # 1 2 3