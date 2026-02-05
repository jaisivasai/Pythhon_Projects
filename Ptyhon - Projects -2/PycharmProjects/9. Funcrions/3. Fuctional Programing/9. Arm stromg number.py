def Arm(num,p,copy):
    add=0
    while(num!=0):
        rem=num%10
        add=add+(rem**p)
        num//=10
    return (add==copy)
num=370
print(Arm(num,len(str(num)),num))

print('-'*20)#----------Type1------------

def Arm(num,p,copy):
    add=0
    while(num!=0):
        rem=num%10
        add=add+(rem**p)
        num//=10
    return (add==copy)
num=370
print('Arm strong number' if (Arm(num,len(str(num)),num)) else 'Not a Arm strong number ')