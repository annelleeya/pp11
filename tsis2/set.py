#1
thisset = {"apple", "banana", "cherry"}
print(thisset)
#2
thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset)
#3
thisset = {"apple", "banana", "cherry"}
print(len(thisset))
#4
myset = {"apple", "banana", "cherry"}
print(type(myset))
#5
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)
#6
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)
#7
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)
#8
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)
#9
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)
#10
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)
#11
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)
#12
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)
#13
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)
#14
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)
#15
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)
#16
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)
#17
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)
