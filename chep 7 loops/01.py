# Loops in python
for i in range(1,11):
    print(i*26)
"""Loops are used to repeat a block of code multiple times until a specific condition is met.
They help in reducing code repetition and make programs shorter and easier to read.

🧾 Types of Loops in Python
1️⃣ for Loop

Used when you know how many times you want to repeat the block of code.

Works with range(), lists, tuples, strings, dictionaries, etc. (iterables).

Syntax:

for variable in sequence:
    # code block


✅ Example:

for i in range(5):
    print(i)


🔹 Prints numbers from 0 to 4.

2️⃣ while Loop

Used when you don't know how many times you need to repeat.

Runs until a condition becomes False.

Syntax:

while condition:
    # code block


✅ Example:

i = 1
while i <= 5:
    print(i)
    i += 1

3️⃣ Nested Loops

A loop inside another loop.

Commonly used for patterns and working with 2D data.
✅ Example:

for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")

🛑 Loop Control Statements

break → Stops the loop immediately.

continue → Skips the current iteration and moves to next.

pass → Does nothing, just a placeholder.

🎯 Advantages of Loops

Reduces code repetition

Makes programs shorter and more readable

Useful for automation, data processing, and pattern printing"""
