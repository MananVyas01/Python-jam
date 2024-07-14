# For string “Hello, john” skip the vowels in the string and print such as output is “hll, jhn”

text = "Hello, john"
vowels = "aeiouAEIOU"

re_text = []

for char in text : 
    if char not in vowels:
        re_text.append(char)

new_text = "". join(re_text)

print(new_text)