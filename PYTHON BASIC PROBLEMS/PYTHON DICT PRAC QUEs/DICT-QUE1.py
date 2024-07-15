#Find maximal character count using dictionary “my name is John my age is 34, i am a software developer”

main_string = input("add your string")

print("the string is: ", main_string)

main_string = main_string.replace(",", "").replace(".", "").lower().split()
char_count_dict = {}


for i in main_string:
    if i in char_count_dict:
        char_count_dict[i] += 1
    else:
        char_count_dict[i] = 1 

# Find the maximum count and the corresponding character
max_count = 0
max_char = None
for char, count in char_count_dict.items():
    if count > max_count:
        max_count = count
        max_char = char

print("The character '{}' appears the most with a count of {}.".format(max_char,max_count))