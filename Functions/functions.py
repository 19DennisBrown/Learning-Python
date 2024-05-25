

def newFunction():
  print(f"New function")
newFunction()

# Arguments

def name(pname):
  print(f"This is {pname}")
name("My name")

# arbitrary arguments: *args
def argsInfo(*kids):
  print(f"Young one is {kids[2]}")
argsInfo('Johan', 'Lev', 'Dafe')

# arbitrary keyword arguments: **kwargs
def kwargsInfo(**children):
  print(f"last name is {children['lname']}")
kwargsInfo(fname='me', lname='you')

# default parameter value
def defParam(country = "Norway"):
  print(f"I love {country}")
defParam("Kenya")

# Passing list as argument
def funcFood(food):
  for c in food:
    print(c)
fruits = ['Apple', 'Banana', 'Cherry']
funcFood(fruits)


# Return values
def funcReturn(c):
  return 6*c

# Pass stmt
def funcPass():
  pass

