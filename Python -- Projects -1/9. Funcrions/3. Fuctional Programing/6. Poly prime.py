def revnumber(num):
    rev=0
    while(num!=0):
        rem=num%10
        rev=(rev*10)+rem
        num//=10
    return rev
def prime(num):
    count=0
    for p in range(1,num+1):
        if(num%p==0):
            count+=1
    return count == 2
num=101
if(num==revnumber(num))and prime(num):
    print('Polyprime')
else:
    print('not a polyprime')


print('-'*20)#----------Type1------------

def revnumber(num):
    rev=0
    while(num!=0):
        rem=num%10
        rev=(rev*10)+rem
        num//=10
    return rev
def prime(num):
    count=0
    for p in range(1,num+1):
        if(num%p==0):
            count+=1
    return count == 2
num=101
print(num==revnumber(num))and prime(num)