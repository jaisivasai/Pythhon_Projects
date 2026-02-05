def prime(num):
    if(num>1):
        for i in range(2,num//2+1):
            if(num%i == 0):
                return False
    return True
num=1
f=list(filter(prime,range(2,21)))
print(f)