# Give two dictionary a = {‘name’: ‘nividata consultancy’ , ‘state’: ‘gujrat’,
#‘city’:’ahmedabad’} b= {‘a’:1, ‘b’:3, ‘c’:1, ‘d’:4, ‘e’:5, ‘f’:0, ‘g’:6} merge the two dictionary
#into a single dictionary using inbuit function

a = {'name': 'nividata consultancy','state': 'gujrat', 'city': 'ahmedabad'}

b = {'a':1, 'b':3, 'c':1, 'd':4, 'e':5, 'f':0, 'g':6}

c = {**a, **b}

print("the give dict A is : ", a)
print("the give dict B is : ", b)
print("merged dict is : ", c)