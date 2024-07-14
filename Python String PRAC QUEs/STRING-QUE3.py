#In the string “My name is John and my age is 43”. Please remove the “n” character from name so out put is “My ame is John and my age is 43” using string built in functions

main_string = "My name is john and my age is 43"

print("before operation : ", main_string)

new_string = main_string.replace("n","")

print("after operation : ", new_string)