#else
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")

#
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")


try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")

#exception
x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")
