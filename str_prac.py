# -*- coding: utf-8 -*-

old = float(input('Previos Result : '))
new = float(input('Now Result : '))
res = (new - old)/new*100
print('''Old Result : %2.1f%%
New Result : %2.1f%%
Improve %% : %2.1f%%'''%(old, new, res))