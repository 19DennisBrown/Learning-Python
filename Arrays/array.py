

cars = ['ford', 'byd', 'tesla']
# accessing the elements
v = cars[0]

# modify the value 
cars[0] = 'Ford'

# The array length
l = len(cars)

# looping array elements
for e in cars:
  print(e)

# Adding array elements
cars.append('Toyota')

# Removing array elements
# 1.pop()
cars.pop(1)
# 2.remove()
cars.remove('byd')

