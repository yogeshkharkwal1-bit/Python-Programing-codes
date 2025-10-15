# functions of stringh
name="yogesh"
print(len(name))  # len=6 

print(name.endswith("sh")) #true 
print(name.endswith("shaa")) #false
print(name.startswith("Yo")) #false
print(name.startswith("yo")) #true
print(name.capitalize()) #Yogesh

# Create a sample string
s = "  Hello World 123  "
t = "python"

# 1. Changing case
print(s.upper())       # "  HELLO WORLD 123  " → all uppercase
print(s.lower())       # "  hello world 123  " → all lowercase
print(s.title())       # "  Hello World 123  " → each word capitalized
print(s.capitalize())  # "  Hello world 123  " → only first char capital
print(s.swapcase())    # "  hELLO wORLD 123  " → swap case

# 2. Removing spaces
print(s.strip())       # "Hello World 123" → removes both sides
print(s.lstrip())      # "Hello World 123  " → left side only
print(s.rstrip())      # "  Hello World 123" → right side only

# 3. Searching
print(s.find("World"))   # 8 → first index of substring
print(s.rfind("l"))      # 11 → last index of 'l'
print(s.index("World"))  # 8 → like find(), but error if not found
# print(s.index("XYZ"))  # ValueError if not found
print(s.count("l"))      # 3 → count occurrences

# 4. Checking start/end
print(s.startswith("  He"))  # True
print(s.endswith("123  "))   # True

# 5. Splitting & Joining
print(s.split())          # ['Hello', 'World', '123'] → split by spaces
print(s.split("o"))       # ['  Hell', ' W', 'rld 123  '] → split by "o"
print(".".join(["a","b","c"]))  # "a.b.c" → join list with "."

# 6. Replace
print(s.replace("World", "Python"))  # "  Hello Python 123  "

# 7. Alignment
print(t.center(10, "-"))   # "--python--"
print(t.ljust(10, "*"))    # "python****"
print(t.rjust(10, "*"))    # "****python"
print("42".zfill(5))       # "00042" → pad with zeros

# 8. Checks (boolean)
print("hello".isalpha())   # True → only letters
print("12345".isdigit())   # True → only digits
print("abc123".isalnum())  # True → letters + digits
print("   ".isspace())     # True → only spaces
print("Hello".istitle())   # True → each word starts with capital
print("hello".islower())   # True → all lowercase
print("HELLO".isupper())   # True → all uppercase

# 9. Encoding & Formatting
print("hello".encode())    # b'hello' → byte object
print("{:>10}".format("hi"))   # "        hi" → right align
print("{:.3}".format("Python")) # "Pyt" → precision cut

