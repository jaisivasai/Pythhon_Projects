def Happy(num):
    while(num>9):
        add=0
        while(num!=0):
            rem=num%10
            add = add+(rem**2)
            num//=10
        num=add
    return (num==1)
num=23
print(Happy(num))