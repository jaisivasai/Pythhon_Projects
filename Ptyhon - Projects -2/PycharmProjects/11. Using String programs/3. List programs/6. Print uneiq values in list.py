l=[10,12,12,18,19,18,12,10]
h=[]
for num in l:
    if(l.count(num)!=1):
        if(num not in h):
            h.append(num)
print(h)