s='engineering'
l=[]
for a in s:
    if(a not in l):
        print('{}={}'.format(a,s.count(a)))
        l.append(a)