

# Polymorphism

class Machines:
  def __init__(machine, brand, model):
    machine.brand = brand
    machine.model = model
  def move(self):
    print(f"moves")
class Car(Machines):
  def move(self):
    print(f"drive")
class Boat(Machines):
  def move(self):
    print(f"Sail")
class Plane(Machines):
  def move(self):
    print(f"Flies")

carOne = Car('Totoya', 'sienta')      
boatOne = Boat('Yokohama', 'brwazz')      
planeOne = Plane('Boeng', '765')      

for props in (carOne, boatOne, planeOne):
  print(props.brand)
  props.move()