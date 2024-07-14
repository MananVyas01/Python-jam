# Remove the duplicates in the list and print the maximum number of the list [1,3,4,423,3,54,3,4,2,3,242]

list1 = [1,3,4,423,3,54,3,4,2,3,242]

new_list = list(set(list1))

print("removed duplicates :",new_list)

front_list = sorted(new_list)

print("sorted list :", front_list)

print("the maximum number in the list is :", front_list[-1])