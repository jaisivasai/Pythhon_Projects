def prime(num):
    count=0
    for p in range(1,num+1):
        if(num % p == 0):
            count+=1
    return count == 2
num=[10,2,6,4,17,22]
print(prime(num))
for i in num:
    print(i)


print('-'*20)#---------------Type1-------------------

"""def prime(num):
    count=0
    for p in range(1,num+1):
        if(num % p == 0):
            count+=1
    return count == 2
print('Prime'if prime(num=2) else 'not a prime')"""