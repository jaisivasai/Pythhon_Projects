l = [[11,12,13],'we are groot']
l[0][0]=l[-1][-1]
l.append(l[-1].split())
l[0].extend(l[-1][0])
l[-1].append(l[0][0])
print(l)