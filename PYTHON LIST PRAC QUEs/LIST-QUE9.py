#Remove the duplicates of the list and Sort the list in ascending and descending order.[1,3,4,423,3,,54,3,4,2,3,242]

main_list = [1,3,4,423,3,54,3,4,2,3,242]

print("before operation : ", main_list)

main_list = list(set(main_list))

front_list = sorted(main_list)

print(front_list)

back_list = sorted(main_list, reverse = True)

print(back_list)