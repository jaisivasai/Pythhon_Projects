# Print first 10  fibinocci number []
fib_l=[0,1]
while len(fib_l)!=10:
    fib_l.append(fib_l[-1]+fib_l[-2])
print(fib_l)