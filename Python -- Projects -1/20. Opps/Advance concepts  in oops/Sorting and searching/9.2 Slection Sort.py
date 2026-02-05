l=[25,17,20,28,10]
for i in range(len(l)-1):
    s=i
    for j in range(i+1,len(l)):
        if l[s] > l[j]:
            s= j
        l[s],l[i] = l[i],l[s]
print(l)
