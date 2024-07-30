"""
Python Dates

A date in Python is not a data type of its own, but it can be used by import a module 'datetime' so as to work with dates as date objects

"""

import datetime
dt = datetime.datetime.now()
print(f"The year is {dt.year}")
print(f"The day is {dt.strftime("%C")}") #the name of the century
print(f"The local time is {dt.strftime("%X")}") #local time.
print(f"The day is {dt.strftime("%A")}") #the name of the week
print(f"The time is {dt.strftime("%H")}: {dt.strftime("%M")} : {dt.strftime("%S")}") #time 

# Creating date objects

create_date = datetime.datetime(2024, 7, 30)
print(create_date)

