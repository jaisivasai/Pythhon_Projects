l=[2,4,5,1,7,1,8]
for i in range(0,3):
    l[i],l[-i-1]=l[-i-1],l[i]
print(l)
