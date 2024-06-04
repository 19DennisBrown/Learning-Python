

# creating class
class newClass:
  standard = 5

# create objects
value = newClass()
print(value.standard)

class Car:
# The __init__() function
  def __init__(car, brand, model, year):
    car.brand = brand
    car.model = model
    car.year = year
  
# The __str__() function
  def __str__(car):
    return car.brand +" "+car.model
  # Object methods.
  def saluteCar(car):
    print(f"Can you identify {car.brand}")

carOne = Car('Tesla', 'Model x', 2020)
carOne.year = 2019
del carOne.year
del carOne
# print(f"{carOne.year} was a better year.")
print(carOne)
carOne.saluteCar()

# The pass statement
class Person:
  pass