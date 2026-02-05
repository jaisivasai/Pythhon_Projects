num = 18
copy=num
rev=0
while(num!=0):
    rev=(rev*10)+num%10
    num=num//10
if(copy!=rev):
    for a in range(2,copy//2 +1):
        if(copy % a ==0):
            print('Not a EMIRP')
            break
    else:
        for b in range(2,rev//2+1):
            if(rev % b ==0):
                print('not a Emirp')
        else:
            print('EMIRP number')
else:
    print('its palidrome')