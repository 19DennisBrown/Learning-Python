"""
A module is a code library.
It is a file containing a set of functions one wants to include in the application.
"""

# Using a module stored in 'createModule.py'
from createModule import favClub
from createModule import Kenyan
import platform

favClub("Chelsea")

print(f"{Kenyan["age"]}")

print(f"{platform.system()} OS") #Identifies the OS
# print(f"{dir(platform.system())}")