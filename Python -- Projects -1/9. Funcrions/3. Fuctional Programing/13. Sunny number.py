def sunny(num):
    i=1
    while(i**2<=num+1):
        if (i**2==num+1):
            break
        i=i+1
    return (i**2==num+1)
num=24
print(sunny(num))

print('-'*20)

def sunny(num):
    i=1
    while(i**2<=num+1):
        if (i**2==num+1):
            break
        i=i+1
    return (i**2==num+1)
num=24
if(sunny(num)):
    print('Sunny number')
else:
    print('Not a sunny number')
