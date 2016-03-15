#Practice 1 -- map()

def normalize(name):
	return name.title()

L1=[]
str_name=''

while str_name != 'end':
	str_name = input("Please insert name (type \'end\' if finish insert name: ")
	L1.append(str_name)

L1.pop(-1)
L2 = list(map(normalize,L1))
print(L1)
print(L2)