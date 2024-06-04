

# Inheritance 

# Base class.
class Citizen:
  def __init__(details, name, age):
    # methods that can be inherited.
    details.name = name
    details.age = age
  def voteDetails(voter):
    print(f"This is the voter name, {voter.name}")
citizenOne = Citizen('Jacob', 34)
citizenOne.voteDetails()
# Derived class
class Foreign(Citizen):
  def __init__(data, name, age, originCountry):
    # The super() function to inherit properties
    super().__init__(name, age)
    data.originCountry = originCountry
  def foreigner(foreign):
    print(f"{foreign.name}'s Country of origin is {foreign.originCountry}")
ForeignOne = Foreign('Jacob', 34, 'Norway')
ForeignOne.foreigner()