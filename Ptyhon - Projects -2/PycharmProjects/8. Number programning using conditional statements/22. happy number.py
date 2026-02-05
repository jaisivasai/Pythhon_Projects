num = 94
while(num>9):
    add = 0
    while(num!=0):
        rem = num%10
        add = add+(rem**2)
        num=num//10
    num=add
if(num == 1):
    print('Happy')
else:
    print('not a Happy')
