#Remove the nested tuple from the tuple (1,2,3,(4,5),6,7,8). Hint check “isinstance” in python

my_tuple = (1, 2, 3, (4, 5), 6, 7, 8)

result_tuple = []
for element in my_tuple:
    if not isinstance(element, tuple):
        result_tuple.append(element)
    else:
        result_tuple.extend(element)

result_tuple = tuple(result_tuple)
print(result_tuple)