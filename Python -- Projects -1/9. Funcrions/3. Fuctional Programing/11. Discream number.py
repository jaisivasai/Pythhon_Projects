def dis(num,p,copy):
    add=0
    while(num!=0):
        rem=num%10
        add=add+(rem**p)
        num//=10
        p=p-1
    return (add==copy)
num=518
print(dis(num,len(str(num)),num))

print('-'*20)#----------Type1------------

def dis(num,p,copy):
    add=0
    while(num!=0):
        rem=num%10
        add=add+(rem**p)
        num//=10
        p=p-1
    return (add==copy)
num=518
if(dis(num,len(str(num)),num)):
    print('Dicream number')
else:
    print('Not a Dicream number')