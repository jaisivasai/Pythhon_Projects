fib_l=[0,1]
while len(fib_l)!=5:
    fib_l.append(fib_l[-1]+fib_l[-2])
print(fib_l)