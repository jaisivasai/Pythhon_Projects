def evil(num):
    count=0
    while(num!=0):
        rem=num%2
        if(rem==1):
            count+=1
        num//=2
    return (count%2==0)
num=18
print(evil(num))
