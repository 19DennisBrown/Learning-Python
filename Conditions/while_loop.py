
# The 'while statement'
a = 5
while a < 10:
  print(f"Printing a for the {a} nth time.")
  a += 1

# 'break' keyword: ends iteration.
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
# 'continue' keyword:Skips the selected condition point.
p = 0
while p < 6:
  p += 1
  if p == 3:
    continue
  print(f"This is what look out, {p}")

  # 'else' statement: satisfies the other side of the condition.
b = 0
while b <= 7:
  print(f"This is, {b}")
  b += 1
else:
  print(f"Out of iteration condition.")