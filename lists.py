myList=[1,2,3]
myList=['stringfafa',1,2,3,32.33,True,'dada',[1,2,3]]
print(len(myList))
myList=['a','b','c']
print(myList[0])
print(myList[-1])
print(myList)

myList[0]='New Item'
print(myList)

myList.append("NEW ITEM") # ['New Item', 'b', 'c', 'NEW ITEM']
print(myList)

listTwo=['x','y','z']
myList.append(listTwo)  #['New Item', 'b', 'c', 'NEW ITEM', ['x', 'y', 'z']]
print(myList)

myList.extend(listTwo)  #['New Item', 'b', 'c', 'NEW ITEM', 'x', 'y', 'z']
print(myList) 

# pop() method is used to remove an item from the list
myList=['a','b','c','d']
item=myList.pop()
print(myList)   #['a', 'b', 'c']
print(item)     #d

item=myList.pop(0)
print(myList)       #['b', 'c']

myList.reverse()    #it is in place
print(myList)       #['c', 'b']

myList=[10,26,3,1,4,2]
myList.sort()
print(myList)

myList=[1,2,['x','y','z']]
print(myList[2][1]) # y

matrix=[[1,2,3],[4,5,6],[7,8,9]]
#list comprehension
first_col=[row[0] for row in matrix]
print(first_col)