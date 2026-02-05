import copy

l=[[10,20],[11,12]]
x=copy.copy(l)
l[0]=20
print(x)
print(l)