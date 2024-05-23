

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