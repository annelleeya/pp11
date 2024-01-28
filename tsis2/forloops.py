#1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
#2
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) 
  if x == "banana":
    break
#3
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
#4
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
#5
for x in range(6):
  print(x)
#6
for x in range(2, 6):
  print(x)
#7
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")
#8
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
  for y in fruits:
    print(x, y)
#9
for x in [0, 1, 2]:
  pass
