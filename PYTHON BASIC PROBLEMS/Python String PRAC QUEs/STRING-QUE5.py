#Remove all duplicates from string “My name is John and my age is 43”

main_string = "My name is john and my age is 43"

print("before operation : ", main_string)

new_string = main_string.split()

new_string = "".join(new_string)

new_string = set(new_string)

new_string = "".join(new_string)

print(new_string)