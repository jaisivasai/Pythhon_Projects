def palin(num):
    rev=0
    copy=num
    while(num!=0):
        rev=(rev * 10)+num%10
        num//=10
    return (rev == copy)
print(palin(num=12321))



print('-'*20)#---------------Type1-------------------

def palin(num,copy):
    rev=0
    while(num!=0):
        rev=(rev * 10)+num%10
        num//=10
    return (rev == copy)
num=12321
print(palin(num,num))


print('-'*20)#----------------Type2------------------

def palin(num):
    rev=0
    copy=num
    while(num!=0):
        rev=(rev * 10)+num%10
        num//=10
    return (rev == copy)
print('palindrome' if palin(num=12321) else 'not a palindrome')


