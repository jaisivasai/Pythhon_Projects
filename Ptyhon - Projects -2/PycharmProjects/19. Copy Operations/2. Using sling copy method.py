l=[[10,20],[11,12]]
x=l[::-1]
l[0]=20
print(x)
print(l)

print('-'*20)
l=[[10,20],[11,12]]
x=l[::]
l[0][0]='sai'
print(x)
print(l)