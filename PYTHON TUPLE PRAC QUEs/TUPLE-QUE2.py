#Remove the duplicates of the tuple (1,3,4,423,3,54,3,4,2,3,242)

my_list = (1,3,4,423,3,54,3,4,2,3,242)

unique_list = tuple(dict.fromkeys(my_list))

print(unique_list)

