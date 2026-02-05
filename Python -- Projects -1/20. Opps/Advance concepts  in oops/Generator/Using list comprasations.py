l= [i**2 for i in range(1,10000)]
g= (i**2 for i in range(1,10000))
print(l.__sizeof__())
print(g.__sizeof__())
