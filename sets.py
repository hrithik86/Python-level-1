#set is an unordered collection(not necessarily sorted) of unique elements
x=set()
x.add(1)
x.add(2)
x.add(4)
x.add(0.1)
print(x)    # {0.1, 1, 2, 4}

y=set()
y.add(3)
y.add(1)
y.add(1)
y.add(4)
y.add(4)
print(y)    # {1, 3, 4}

converted=set([1,1,1,2,2,2,2,2,3,3,3,3,3])
print(converted) # {1, 2, 3}