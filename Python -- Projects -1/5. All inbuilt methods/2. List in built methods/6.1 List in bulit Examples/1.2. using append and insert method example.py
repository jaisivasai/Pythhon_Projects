L = ['i am groot',[11,12]]
L[0]=L[0].split()
L.append(L[0][-1][-1])
L[1].insert(1,L[0][1])
print(L)