from functools import reduce
l=[15,20,25,30]
r=reduce(lambda x,y: x if (x>y) else y,l)
print(r)