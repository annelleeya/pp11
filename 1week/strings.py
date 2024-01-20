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
