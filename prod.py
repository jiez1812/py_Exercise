#Practice 2
from functools import reduce

def prod(L):
	def miniProd(x,y):
		return x*y
	return reduce(miniProd,L)

L1 = []
int_n = 0
str_n = ''

while str_n != '':
	str_n = input('Please insert num : ')
	if str_n = '':
		pass
	else:
		int_n = int(str_n)
		L1.append(int_n)
	
L2 = prod(L1)
print(L1)
#for x in L1:
#	if x = L1[-1]:
#		print(L1[x] + '= ', end='')
#	else:
#		print(L1[x] + '* ',end='')