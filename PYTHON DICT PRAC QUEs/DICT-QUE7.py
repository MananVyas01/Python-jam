#Make a dictionary with the key as number and the power of the number as it value using dictionary comprehension. List [1,2,3,4,5]. For example {1:1, 2:4, 3:9}

my_list = [1,2,3,4,5]

my_dict = {i:i**2 for i in my_list}

print(my_dict)