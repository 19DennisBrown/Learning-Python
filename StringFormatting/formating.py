

# PYTHON STRING FORMATTING
"""
F-string was introduced to replace 'format()'
"""


stmt = f"This is a testing statement."
print(f"{stmt}")

# Placeholders and MOdifiers
nation = 254
stmts = f"The nation code is  {nation}"
print(f"stmts")

# Displaying float with two decimals
cost = 59
stmt1 = f"Provide is the {cost:.2f}"
directFormat = f"Here is the value {56:.2f}"

# Operations 
multiply = f"Area of a square is {20*20} units"

# Operations before displaying
price = 34
tax = .25
unitPrice = f"The total price is {price + (price*tax)}"

# if...else
temp = 32
weather = f"It is very {'hot' if temp>35 else 'warm'}"

# Execute functions
touch = 'careress'
feeling = f"It good to {touch.upper()}" #upper converts the string variable to upper-case

# Zeros separator
bills = f"{5000:,}"

