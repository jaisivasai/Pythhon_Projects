def Dic(num,power):
    if(num==0):
        return 0
    return (num%10)**power+Dic(num//10,power-1)
num=518
if Dic(num,len(str(num)))==num:
    print('Dicream number')
else:
    print('Nota a Dicream number')

print('-'*20)


def Dic(num,power):
    if(num==0):
        return 0
    return (num%10)**power+Dic(num//10,power-1)
num=518
print(Dic(num,len(str(num)))==num)
