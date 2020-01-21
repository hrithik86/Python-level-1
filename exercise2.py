#Given a list of integers, return true if the sequence of numbers 1,2,3 appears in the list somewhere
#   [1,1,2,3,1] True
#   [1,1,2,4,1] False
#   [1,1,2,1,2,3]   True

def arrayCheck(nums):
    for i in range(len(nums)-2):
        if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
            return True
    return False

arr1=[1,1,2,3,1]
arr2=[1,1,2,4,1]
arr3=[1,1,2,1,2,3]
print(arrayCheck(arr1))
print(arrayCheck(arr2))
print(arrayCheck(arr3))

#given a string, return a new string made of every other character starting with the first
#"Hello" yields "Hlo"


def stringBits(s):
    res=""
    for i in range(len(s)):
        if i%2==0:
            res=res+s[i]
    print(res)

stringBits("Hello")

#given 2 strings,return true if either of the strings appear at the very end of the other string,
#ignoring upper/lower case differences.
# end_other('Hiabc','abc') ->True
# end_other('AbC','HiaBc') ->True
# end_other('abc','abXabc') ->True

def end_other(a,b):
    a=a.lower()
    b=b.lower()
    
    #return(b.endswith(a) or a.endswith(b))
    return a[-len(b):]==b or a==b[-len(a):]
    
print(end_other('Hiabc','abc'))

#given a string, return a string where for every char in the original, there are 2 chars.

def doubleChar(s):
    res=""
    for i in range(len(s)):
        res=res+(2*s[i])
        #res=res+s[i]
    print(res)

doubleChar("AAbb")      #AAAAbbbb
doubleChar("Hi-There")  #HHii--TThheerree

def fix_teen(n):
    if n==15 or n==16:
        return n
    elif n>=13 and n<=19:
        return 0
    else: 
        return n
 
def no_teen_sum(a,b,c):
    a=fix_teen(a)
    b=fix_teen(b)
    c=fix_teen(c)
    return a+b+c

print(no_teen_sum(1,2,3))
print(no_teen_sum(2,13,1))
print(no_teen_sum(2,1,14))
