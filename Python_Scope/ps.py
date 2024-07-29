"""
A variable can only be available from inside the region it is created: scope

Local scope: A var created inside a function can only be used inside that function.
"""

def myFunc():
  x = 300
  print(x)

myFunc()

# Function inside a function.
def thisFunction():
  y = 200
  def thisInnerFunc():
    print(y)
  thisInnerFunc()
thisFunction()

"""
Global scope 
is a variable created in the main body of the python code and belongs to the global scope.
"""
z = 212
def globalFunc():
  print(z)

globalFunc()

# Naming a variable
"""
If one operate with the same variable name inside and outside a function then python will treat them as two separate variables, one local and another global.
"""
c = 345
def sampleFunc():
  c = 32
  print(c)
sampleFunc()
print(c)

# Global keyword
"""
Used to create global variable when the variable is stuck in local, use 'global' keyword
"""
# e = 43
def sampleFunc():
  global e
  e = 32
  print(e)
sampleFunc()
print(e)

# Nonlocal keyword
"""
Used in nested functions, variable is made available to outer function.
"""

def notLocal():
  j = "Jane"
  def localFunc():
    nonlocal j
    j = "Joseph"
  localFunc()
  return j
print(f"Outer function returns {notLocal()}")


