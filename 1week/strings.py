#1
print("Hello")
print('Hello')

#2
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#3
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

#4
a = "Hello, World!"
print(a[1])

#5
for x in "banana":
  print(x)

#6
a = "Hello, World!"
print(len(a))

#7
txt = "The best things in life are free!"
print("free" in txt)

#8
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

#9
txt = "The best things in life are free!"
print("expensive" not in txt)

#10
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

#11
b = "Hello, World!"
print(b[2:5])

#12
b = "Hello, World!"
print(b[:5])

#13
b = "Hello, World!"
print(b[-5:-2])

#14
a = "Hello, World!"
print(a.upper())

#15
a = "Hello, World!"
print(a.replace("H", "J"))

#16
a = "Hello, World!"
print(a.split(","))

#17
a = "Hello"
b = "World"
c = a + b
print(c)

#18
a = "Hello"
b = "World"
c = a + " " + b
print(c)

#19
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

#20
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

#21
txt = "We are the so-called \"Vikings\" from the north."

#22
