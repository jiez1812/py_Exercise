L = [('Bob',75), ('Adam',92), ('Bart',66), ('Lisa',88)]

L2 = sorted(L, key = lambda s:s[0])
L3 = sorted(L, key = lambda s:s[1], reverse = 1)

print(L2)
print(L3)