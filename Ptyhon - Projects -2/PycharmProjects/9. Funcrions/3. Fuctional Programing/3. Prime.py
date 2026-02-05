def prime(num):
    count=0
    for p in range(1,num+1):
        if(num % p == 0):
            count+=1
    return count == 2
print(prime(num=2))

print('-'*20)#---------------Type1-------------------

def prime(num):
    count=0
    for p in range(1,num+1):
        if(num % p == 0):
            count+=1
    return count == 2
print('Prime'if prime(num=2) else 'not a prime')