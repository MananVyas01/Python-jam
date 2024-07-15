#Convert and print the string “My name is John” to “John is name My” using string built in functions

s = "My name is John"
splited_s = s.split() #it will convert the string to list of words
reverse_splited = splited_s[::-1] #the list words are become reverse
reverse_splited = " ".join(reverse_splited) # now the list become one single string

print(reverse_splited)