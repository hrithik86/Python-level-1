#tuples are same as list but they are immutable
t=(1,2,3)
print(t[0])

t=('a',True,123)
#tuples are same as list but they are immutable
#t[0]='NEW'  #gives error

#   Tuple Unpacking
x=[(1,2),(3,4),(5,6)]
for (a,b) in x:
    print(a)
#1
#3
#5