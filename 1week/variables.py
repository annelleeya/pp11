#1
x = 5
y = "John"
print(x)
print(y)

#2
x = 4
x = "Sally"
print(x)

#3
x = str(3)
y = int(3)
z = float(3)

#4
x = 5
y = "John"
print(type(x))
print(type(y))

#5
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#6Variable names with more than one word
myVariableName = "John" #Camel Case
MyVariableName = "John" #Pascal Case
my_variable_name = "John" #Snake Case

#7
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#8
x = y = z = "Orange"
print(x)
print(y)
print(z)

#9
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#10
x = "Python is awesome"
print(x)

#11
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

#12
x = 5
y = 10
print(x + y)

#13
x = 5
y = "John"
print(x, y)

#14
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()


#15
x = "awesome"
def myfunc():
  x = "fantastic"
  print("Python is " + x)
myfunc()
print("Python is " + x)

#16
def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)

