#1
thistuple = ("apple", "banana", "cherry")
print(thistuple)
#2
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))
#3
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
#4
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))
#5
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)
#6
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
#7
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")
#8
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)
#9
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
#10
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
#11
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)
#12
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)
#13
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
#14
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])
#15
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1
#16
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)
#17
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)
