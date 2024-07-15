#Make the string ““My@name@is@john” to a list [“My”, “name”, “is”, “john”]

text = "My@name@is@john"

new_text = text.replace("@", " ")

new_text = new_text.split()

print(new_text)