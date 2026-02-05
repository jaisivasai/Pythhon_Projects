def pro(num):
    n=1
    while(n*(n+1)<=num):
        if (n*(n+1)==num):
            break
        n=n+1
    return (n*(n+1)==num)
num=12
print(pro(num))

print('-'*20)

def pro(num):
    n=1
    while(n*(n+1)<=num):
        if (n*(n+1)==num):
            break
        n=n+1
    return (n*(n+1)==num)
num=12
if(pro(num)):
    print('pronic')
else:
    print('not a pronic')
