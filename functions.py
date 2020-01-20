def my_func(p='default'):
    """
    this is the docstring
    """
    print('function executed')

my_func()

def func2(p='jake'):
    print("name is {}".format(p))

func2() # name is jake
func2('hrithik') # name is hrithik

def hello():
    print("hello")
    
hello()

def hello1():
    return "hello"

x=hello1()
print(x)

#type keyword tells us the datatype of the variable
def add(n1,n2):
    if(type(n1)==type(n2)==type(10)):
        return n1+n2
    else:
        print("Sorry these are not integers")
res=add("2","3")
print(res)

#Lambda Expression
myList=[1,2,3,4,5]
def even_bool(num):
    return num%2==0
evens=filter(even_bool,myList) #filter function returns those items which are true
print(list(evens))  #[2, 4]

evens=filter(lambda num: num%2==0,myList)
print(list(evens))

#####################################################
print('x' in [1,2,3,4,'x']) #True
print('x' in [1,2,3,4])     #False

 