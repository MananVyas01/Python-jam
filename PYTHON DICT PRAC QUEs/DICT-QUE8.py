#Using dictionary comprehension make a new dictionary with only if the values is more than 3. {‘a’:1, ‘b’:3, ‘c’:1, ‘d’:4, ‘e’:5, ‘f’:0, ‘g’:6}

d = {'a':1, 'b':3, 'c':1, 'd':4, 'e':5, 'f':0, 'g':6}

new_dict = {k:v for k,v in d.items() if v > 3}

print(new_dict)