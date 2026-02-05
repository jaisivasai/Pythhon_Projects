def compsite(num):
    count=0
    for p in range(1,num+1):
        if(num % p == 0):
            count+=1
    return count > 2
print(compsite(num=12))

print('-'*20)#---------------Type1-------------------

def prime(num):
    count=0
    for p in range(1,num+1):
        if(num % p == 0):
            count+=1
    return count > 2
print('Composite'if prime(num=12) else 'not a Composite')