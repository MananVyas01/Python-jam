#Make the list to string [“My”, “name”, “is”, “john”] output is such “My@name@is@john”

text = ["My", "name", "is", "john"]

text = "@".join(text)

print(text)