def Niven(num):
    if(num==0):
        return 0
    return (num%10)+Niven(num//10)
num=126
print(Niven(num%Niven(num))==0)

print('-'*20)

def Niven(num):
    if(num==0):
        return 0
    return (num%10)+Niven(num//10)
num=126
if(Niven(num%Niven(num))==0):
    print('Niven number')
else:
    print('Not a Niven number')
