#dictionaries are python version of hash tables
#they allow us to create a mapping with key value pairs
my_stuff={
    'name':'hrithik',
    'age':19,
    'key3':{
        '123':[1,2,'grabMe']
    }
}
print(my_stuff)
print(my_stuff['name'])

print(my_stuff['key3']['123'][-1])      #grabMe

my_stuff={
    'lunch':'pizza',
    'bfast':'eggs'
}
print(my_stuff['lunch'])
my_stuff['lunch']='burger'
print(my_stuff['lunch'])
my_stuff['dinner']='pasta'
print(my_stuff)