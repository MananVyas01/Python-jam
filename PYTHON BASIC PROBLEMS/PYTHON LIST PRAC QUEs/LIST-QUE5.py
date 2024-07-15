#Create a new list of even numbers using list comprehension till range 100

even_list = [i for i in range(1,101) if i%2 is 0]

print(even_list)


odd_list = [i for i in range(1,101) if i%2 is not 0]

print(odd_list)