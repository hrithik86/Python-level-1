s='django'
print(s[1:4])   # including index 1, excluding index 4
                # jan
#reverse s
print(s[::-1])  # ognajd

l=[3,7,[1,4,'hello']]
l[2][2]='goodbye'
print(l)

#print hello for the following dictionaries
d1={'simple_key':'hello'}
print(d1['simple_key'])
d2={
    'k1':{
        'k2':'hello'
    }
}
print(d2['k1']['k2'])
d3={
    'k1':[
        {
            'nest_key':['this is deep',['hello']]
        }
    ]
}
print(d3['k1'][0]['nest_key'][1][0])

age=4
name='bosco'
print("hello my dog name is {a} and he is {b}.".format(a=name,b=age))