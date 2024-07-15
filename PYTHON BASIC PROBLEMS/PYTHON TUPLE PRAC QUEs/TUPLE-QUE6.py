#Add the value “nividata” in the value of list in a tuple (1,2,3,[4,5],6,7,8) output is (1,2,3,[4,5,”nividata”],6,7,8)

my_tup = (1,2,3,[4,5],6,7,8)

my_tup[3].append("nividata")

print(my_tup)