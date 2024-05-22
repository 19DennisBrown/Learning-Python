
a = 33
b = 20
c = 23
if b > a:
  print(f"b is greater than a ")
elif a == b:
  print(f" a and  b are equal.")
else:
  print(f"a is greater than b")

# ___short hand if...
if a > b: print("a is greater than b.")
# ___short hand if...else...
print(f"a, {a}, is bigger than b, {b}") if a > b else print(f"b, {b}, is bigger than a, {a}")
# 
print(f"a, {a}, is bigger than b, {b}") if a > b else print(f"b, {b}, is equal to a, {a}") if (a==b) else print(f"b, {b}, is bigger than a, {a}")
# ____AND
if a>b and b>c: print(f"Both conditions are true.")
# OR
if a>b or b>c: print(f"Atleast one condition is true.")
# NOT
if not b>c: print(f"a is not greater than b")


# _____NESTED IF
x = 41
if x > 10:
  print("Above ten.")
  if x > 20:
    print('and also above 20')
  else:
    print('but not  above 20.')

# ___The pass statement.
if b>a:
  pass


