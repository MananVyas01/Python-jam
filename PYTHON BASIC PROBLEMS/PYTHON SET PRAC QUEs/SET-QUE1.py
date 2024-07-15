# Remove all the duplicates in the string “Hello my name is john” and print the output of the string in one line. The characters can unordered using set in built function

main_string = "Hello my name is john"

print("before operation : ", main_string)

new_string = set(main_string)

new_string = "".join(new_string)

print(new_string)