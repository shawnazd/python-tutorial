x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)


def myfunc():
  global y
  y = "fantastic"

myfunc()

print("Python is " + y)