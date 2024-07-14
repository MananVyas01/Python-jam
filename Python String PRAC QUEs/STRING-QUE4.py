#Remove spaces from string “My name is John      and my age  is     43” using python built in functions

s = "My name is John      and my age  is     43"

new_s = s.split()

new_s = " ".join(new_s)

print(new_s)

