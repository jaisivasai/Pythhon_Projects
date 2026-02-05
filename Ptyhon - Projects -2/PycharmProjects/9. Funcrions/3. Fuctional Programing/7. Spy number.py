def sum(num):
    add=0
    while(num!=0):
        rem=num%10
        add=add+rem
        num//=10
    return add
def multi(num):
    mul=1
    while(num!=0):
        rem=num%10
        mul=mul*rem
        num//=10
    return mul
num=4121
if(sum(num)==multi(num)):
    print('spy number')
else:
    print('not a spy number')