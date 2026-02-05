s= 'we are in class'
l=s.split()
i=[]
for a in l:
    i.append(a[::-1])
print(' '.join(i))