

a = "Hello"
print(a)

# Multiline string, use three single or double quotes
b = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(b)

# strings in arrays
c = "Hello, World!"
print(c[0])

# Looping through a string
for x in "banana":
  print(x)

# Finding string length
d = "Hello, World!"
print(len(d))

# Checking for constituents presence
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
# Checking for constituents absence
  stmt = "The best things in life are free!"
print("expensive" not in stmt)

# SLICING
# from given point
e = "Hello, python!"
print(e[2:7])
# from the start
f = "Hello, World!"
print(f[:5])
# slicing to the end
g = "Hello, World!"
print(g[2:])

# Negative indexing
h = "Hello, World!"
print(h[-5:-2])

# MODIFYING STRINGS
# To upper case
i = "Hello, World!"
print(i.upper())
# To lower case
j = "Hello, World!"
print(j.lower())
# 
# Removing white spaces
k = " Whats, up! "
print(k.strip()) # returns "Whats, up!"

# Replacing strings
l = "Hello, World!"
print(l.replace("H", "J"))

# Splitting strings
m = "Hello, World!"
print(m.split(",")) # returns ['Hello', ' World!']

# CONCATENATION
n = "Hello"
o = "World"
p = n + o
print(p)

#   FORMAT 
# Use the format() method to insert numbers into strings:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

# The escape character allows you to use double quotes when you normally would not be allowed:

txt = "We are the so-called \"Vikings\" from the north."