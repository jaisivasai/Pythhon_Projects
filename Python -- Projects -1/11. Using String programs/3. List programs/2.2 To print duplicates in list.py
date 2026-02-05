l=[10,12,1,2,12,18,19,18,12,10]
h=[]
for i in l:
    if(l.count(i)!=1):
        if(i not in h):
            h.append(i)
print(h)

print('-'*20)

l=[10,12,1,2,12,18,19,18,12,10]
h=[]
for i in l:
    if(l.count(i)!=1):
        if(i not in h):
            print(i)
            h.append(i)
