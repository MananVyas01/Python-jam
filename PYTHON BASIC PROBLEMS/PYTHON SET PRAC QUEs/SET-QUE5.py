#Find the missing and the additional values in 2 list using set built in methods
#A = [1,3,4,5,6]
#B = [3,2,4,5,2,7,8,9]

A = [1,3,4,5,6]
B = [3,2,4,5,2,7,8,9]

print(set(A) - set(B))
print(set(B) - set(A))