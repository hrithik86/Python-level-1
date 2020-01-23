#Lambda function is used to write the entire function in one line
def times2(var):
    return var*2

d=lambda n: n*2
print(d(5))
#10
#########################################

seq=list(range(1,6))
print(seq)
#[1, 2, 3, 4, 5]
#########################################
a=[]
for num in seq:
    a.append(times2(num))
print(a)
#[2, 4, 6, 8, 10]
#########################################

#using map function
b=list(map(times2,seq))
print(b)
#[2, 4, 6, 8, 10]
#########################################

c=list(map((lambda num: num*2),seq))
print(c)
#[2, 4, 6, 8, 10]
#########################################

evens=list(filter(lambda num: num%2==0,seq))
print(evens)
#[2,4]