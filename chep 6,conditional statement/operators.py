# ============================
# Python Operators Example 🚀
# ============================

# 1️⃣ Arithmetic Operators
print("=== Arithmetic Operators ===")
a = 10
b = 3
print(a + b)  # Addition -> 13
print(a - b)  # Subtraction -> 7
print(a * b)  # Multiplication -> 30
print(a / b)  # Division -> 3.33
print(a // b) # Floor Division -> 3
print(a % b)  # Modulus (remainder) -> 1
print(a ** b) # Exponentiation (a^b) -> 1000

# 2️⃣ Relational / Comparison Operators
print("\n=== Comparison Operators ===")
print(a == b)  # Equal to -> False
print(a != b)  # Not equal to -> True
print(a > b)   # Greater than -> True
print(a < b)   # Less than -> False
print(a >= b)  # Greater than or equal to -> True
print(a <= b)  # Less than or equal to -> False

# 3️⃣ Logical Operators
print("\n=== Logical Operators ===")
x = True
y = False
print(x and y)  # AND -> False (both must be True)
print(x or y)   # OR -> True (at least one True)
print(not x)    # NOT -> False (reverse the result)

# 4️⃣ Assignment Operators
print("\n=== Assignment Operators ===")
c = 5
c += 3   # c = c + 3
print(c) # 8
c -= 2   # c = c - 2
print(c) # 6
c *= 4   # c = c * 4
print(c) # 24
c /= 6   # c = c / 6
print(c) # 4.0
c //= 2  # c = c // 2
print(c) # 2.0
c %= 2   # c = c % 2
print(c) # 0.0
c = 2
c **= 3  # c = c ** 3
print(c) # 8

# 5️⃣ Bitwise Operators
print("\n=== Bitwise Operators ===")
p = 5  # binary: 0101
q = 3  # binary: 0011
print(p & q)  # AND -> 1 (0001)
print(p | q)  # OR  -> 7 (0111)
print(p ^ q)  # XOR -> 6 (0110)
print(~p)     # NOT -> -6 (flip bits)
print(p << 1) # Left shift -> 10 (1010)
print(p >> 1) # Right shift -> 2 (0010)

# 6️⃣ Membership Operators
print("\n=== Membership Operators ===")
name = "apple"
print("a" in name)      # True ('a' is present)
print("z" not in name)  # True ('z' is not present)

# 7️⃣ Identity Operators
print("\n=== Identity Operators ===")
list1 = [1, 2, 3]
list2 = list1
list3 = [1, 2, 3]
print(list1 is list2)      # True (same memory location)
print(list1 is list3)      # False (different objects)
print(list1 is not list3)  # True (not same object)
