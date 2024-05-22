

myFamily = {
  "child1":{
    "name":"Emil",
    "year":2004
  },
  "child2":{
    "name":"Tobias",
    "year":2007
  },
  "child3":{
    "name":"Linus",
    "year":2011
  }
}
print(myFamily["child1"]["name"])
print(myFamily["child1"])
for child, obj in myFamily.items():
  print('.........................')
  print(child)
  for data in obj:
    print(f"{data} : {obj[data]}")

first={
    "name":"Emil",
    "year":2004
  }
second={
    "name":"Tobias",
    "year":2007
}
third={
    "name":"Linus",
    "year":2011
  }
table = {
  "first":first,
  "second":second,
  "third":third,
}
#  __LOOPING THROUGH DICTIONARIES__
for position, obj in table.items():
  print('_____________________')
  print(position)
  for data in obj:
    print(f"{data} : {obj[data]}")
