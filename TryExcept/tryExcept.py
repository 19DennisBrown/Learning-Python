
"""
TRY block lets one test a block of code for errors.
EXCEPT blocks lets one handle the error.
ELSE block lets one execute code when there is no error.
FINALLY blocks lets one execute the code regardless of try-except block.
"""


try:
  print(x)
except NameError:
  print(f"Variable x is undefined")
else:
  print(f"Nothing went wrong.")
finally:
  print(f"The 'try-except' is finished.")

# Xsample in openning a file that does not exist

try:
  f = open("deme.txt")
  try:
    f.write("Test writing this file.")
  except:
    print(f"Writing has failed")
  finally:
    f.close()
except:
  print(f"Writing the file failed")


# Raising an exception
x = -1
if x < 0:
  raise Exception("No numbers are below zero.") #Error type is not defined.

x = "hello"
if not type(x) is int:
  raise TypeError("Only integers are allowed") #Error type has been defined.
