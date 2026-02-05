l= [100,20,120,18]
m=list(map(lambda a : a//2 ,l))
print(m)

print('-'*20) # it prints map object id address

l= [100,20,120,18]
m=(map(lambda a : a//2 ,l))
print(m)