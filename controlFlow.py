#FOR LOOPS

seq=[1,2,3,4,5,6,7,8]
for item in seq:
    print(item)

d={
    'sam':1,
    'dam':2
}
for i in d:
    print(i)    #prints all keys

for k in d:
    print(d[k]) #print the values

myPairs=[(1,2),(3,4),(5,6)]
for item in myPairs:
    print(item) 
#   (1, 2)
#   (3, 4)
#   (5, 6)

#tuple unpacking
for (tup1,tup2) in myPairs:
    print(tup1)
    print(tup2)

###########################################################
# WHILE LOOPS

i=0
while i<5:
    print("i is:{}".format(i))
    i=i+1

# range function
#>>> list(range(0,5))
#[0, 1, 2, 3, 4]
#>>> list(range(0,20,2))
#[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
#>>> list(range(0,21,2))
#[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

for item in range(10):
    print(item) #prints numbers 0 to 9


#list comprehension
x=[1,2,3,4]
out=[]
for num in x:
    out.append(num**2)
print(out) #[1, 4, 9, 16]
## it can be written in one statement like
out=[num**2 for num in x]
print(out)