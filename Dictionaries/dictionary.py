

thisDict = {
  'brand':'Ford',
  'model':'Mustang',
  'year':1964,
  'colors': ['red', 'blue', 'black'],
  'electric?': False
}

# print(thisDict)
# print(thisDict['brand'])
# print("The length is: ",len(thisDict))

"""Creating a new a dictionary using dict keyword"""
newDict = dict(
  name='Books',
  genre='Comic',
  writer='Daniel'
)
print(f"The newly created dictionary is : {newDict}")
# Adding new key:value pair
newDict['size']='A4'
# Updating dictionary
newDict.update(
  {
    'genre':'fictional',
    'name':'Lucas Gray'
  }
)
# Changing  value of a given key
newDict['size']='A5'
# Getting the value of the provided key
print(f"Value of name is : {newDict.get('name')}")
# Getting all the keys
print(f"These are the keys : {newDict.keys()}")
# Getting all the values
print(f"These are the values : {newDict.values()}")
# Getting all the items
print(f"These are the items : {newDict.items()}")

# Checking if key exists
if 'size' in newDict:
  print(f"It exists!! It has a value of {newDict.get('size')}")
else:
  print(f"It does not exist")