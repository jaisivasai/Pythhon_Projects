s='ENGINEERING'
l=[]
for x in s:
    if(s.count(x)!=1):
        if (x not in l):
            print(x)
            l.append(x)
