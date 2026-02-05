def sum(num):
    add,mul = 0,1
    while(num!=0):
        rem=num%10
        add=add+rem
        mul=mul*rem
        num//=10
    return (add==mul)
num=1421
print(sum(num))
