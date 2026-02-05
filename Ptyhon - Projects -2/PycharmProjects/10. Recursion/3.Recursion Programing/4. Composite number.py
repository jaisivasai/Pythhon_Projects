def comp(num,i):
    if(i==num+1):
        return 0
    return (1 if (num%i==0)else 0)+comp(num,i+1)
num=12
if(comp(num,1))>2:
    print('Composite number')
else:
    print('Not a Composite number')