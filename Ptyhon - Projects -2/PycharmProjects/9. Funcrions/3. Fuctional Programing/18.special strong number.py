def strong(num,copy):
    add=0
    while(num!=0):
        rem=num%10
        fact=1
        for a in range(1,rem+1):
            fact=fact*a
        add=add+fact
        num//=10
    return (copy==add)
num=145
print(strong(num,num))

