import copy
l=[[10,20],[11,12]]
x=copy.deepcopy(l)
l[0][0]='sai'
print(x)
print(l)