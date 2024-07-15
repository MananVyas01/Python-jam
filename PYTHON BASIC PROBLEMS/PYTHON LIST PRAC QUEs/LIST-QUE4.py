#Remove the vowels in the string using list comprehension, “My name is john, i am a software developer”

main_string = "My name is john, i am a software developer"

vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

new_string = ''.join([i for i in main_string if i not in vowels])

print(new_string)