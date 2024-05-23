
# Iterating over a sequence(list)
fruits = ["Mango", "Avocado", "Banana"]
adj = ["red", "big", "tasty"]

for x in fruits:
  print(f"{fruits.index(x)+1}: {x}")

# Lopping through a string
for w in 'people':
  print(f"{w}")

# 'break' keyword.Prints what follows the  target.
for b in fruits:
  if b == 'Banana':
    break
  print(f".............................{b}")

# 'continue' keyword:[rints the preceeds of target
for p in fruits:
  if p == 'Mango':
    continue
  print(f"............................{p}")

# The 'range()' function.
# ✅without start param
for z in range(6):
  print(z)
# with start param
for l in range(1,8):
  print(f"{l}")

# 'Else in for loop'
for f in range(6):
  print(f)
else:
  print('Finished')

for t in adj:
  for u in fruits:
    print(f"{t,u}")


