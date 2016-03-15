name = ['Adam','Alex','Amy','Bob','Boom','Candy','Chris','David','Jason','Jasonstatham','Bill']
i_name = input("Please input name: ").title()
wname = []
for n in name:
    if n[:len(i_name)] == i_name:
        wname.append(n)
        
if len(wname)!=0:
    print('Do you want to find {0}'.format(wname))
else:
    print('{0} not find'.format(wname))