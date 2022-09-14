from itertools import permutations

value = int(input("how many number u want to add"))

arr = []

for n in range(value):
    arr.append(input("Enter value"))
comb = permutations(arr, value)
print(comb)
for k in comb:
    print(k)



