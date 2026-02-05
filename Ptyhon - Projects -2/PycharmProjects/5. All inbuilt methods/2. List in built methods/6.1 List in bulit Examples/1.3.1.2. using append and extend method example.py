l = [[11,14,12,100],'i am gost']
l[0][0]=l[-1][-1]
l[0].extend({1,2})
l.extend(l[1][2])
l[0].append('sai')
l.append(l[-1].split())
print(l)
