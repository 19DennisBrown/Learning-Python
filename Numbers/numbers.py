

x = 1    # int
y = 2.8  # float
z = 1j   # complex

print(f'{x, y, z}')
print(type(z))
# ====
c = complex(y)
print(type(c), c)
# ============

# Random numbers
import random
randomNo = random.randrange(1,6)
print(randomNo)

# Casting = specifying a variable type at declaration using constructor.

x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'