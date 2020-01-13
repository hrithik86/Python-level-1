#indexing from 0
my_string="abcdefg"
print(my_string[0]) #a

#printing last character
print(my_string[-1]) #g

#slicing
print(my_string[2:]) #cdefg

print(my_string[:3]) #abc

print(my_string[2:5]) #cde

print(my_string[::1])   # :: is step size 
                        # abcdefg
print(my_string[::2])   # aceg

x=my_string.upper() #ABCDEFG
print(x)
x=my_string.lower() #abcdefg
print(x)

#splitting
my_string="Hello world"
x=my_string.split()
print(x) # ['Hello', 'world']

x=my_string.split("e")
print(x) # ['H', 'llo world']

#print formatting
x="Insert string here:{}".format("Insert me!")
print(x)    # Insert string here:Insert me!

x="Item 1:{} Item 2:{}".format("dog","cat")
print(x) # Item 1:dog Item 2:cat

x="Item 1:{a} Item 2:{b}".format(b="dog",a="cat")
print(x) # Item 1:cat Item 2:dog