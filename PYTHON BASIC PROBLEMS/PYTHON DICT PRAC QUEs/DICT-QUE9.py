#Given in a list, create a dictionary with a list of unique keys, if a key already exists in a
#dictionary then do not update the value. List [[‘name’, ‘nividata consultancy’], [‘state’, 'gujrat’], [‘name’, ‘nividata’], [‘city’,’ahmedabad’]]

list1 = [['name', 'nividata consultancy'], ['state', 'gujrat'], ['name', 'nividata'], ['city', 'ahmedabad']]
dict1 = {}
for i in list1:
    if i[0] not in dict1:
        dict1[i[0]] = i[1]
print(dict1)