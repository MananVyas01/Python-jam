#Update the values of the key company from nividata to nividata consultancy in dictionary
#{“company”: {“name”: “nividata”}”, “state”: “gujrat”, “city”: “ahmedabad”, “country”: “india”}
#using dictionary built in functions. Also Remove the key country from the dictionary

dict1 = {"company": {"name": "nividata"}, "state": "gujrat", "city": "ahmedabad", "country": "india"}

dict1["company"]["name"] = "nividata consultancy"

print(dict1)
