"""1. print prime factors for the given number in list."""
n=350
i=2
L=[]
while i<=n:
    if n%i==0:
        L.append(i)
        n//=i
    else:
        i+=1
print(L)