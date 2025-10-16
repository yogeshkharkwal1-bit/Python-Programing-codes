name="yogesh" 

lenght =len(name) 
print(lenght)

nameshort=name[0:3]  
nameshort1=name[0:4]
nameshort2=name[2:6] 
nameshort3=name[0:]
nameshort4=name[ :5]
nameshort5=name[-5:-2]

print(nameshort) 
print(nameshort1)
print(nameshort2)
print(nameshort3)
print(nameshort4)
print(nameshort5)
 
# 2nd method to print the substring 

print(name[0:3]) 
print(name[0:4]) 
print(name[2:6]) 
print(name[0:]) 
print(name[:3]) 
print(name[:]) 
print(name[-4:-1])

#skip concepts of a string

a="123456789"
print(a[1:7:3])   # out=25 idx1 to idx 7=1234567  1idx=2 and after 2 jumps 4rth idx val=5

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

