

"""
JSON is a syntax for storing and exchanging data.
It is a text, written with javascript object notation

Python has an in-built package 'json'
"""

import json

# converting json to python

# some json
person = {
    "name":"Jere",
    "age":23,
    "city":"Orlando"
    }

# parse person
parsedPerson = json.loads(person)
# convert to json
dumpedPerson = json.dumps(person)

# It results to a python dictionary
print(f"{parsedPerson["name"]}")
print(f"{dumpedPerson}")