l = ['abc xyz mno']
l.append(l[0].split())
l[0]=l[1]
l.extend(l[0])
l[0].append(l[-1])
l[1].append(l[0][-1])
l.extend(l[-1])
print(l)