def Arm(num,power):
    if(num==0):
        return 0
    return (num%10)**power+Arm(num//10,power)
num=370
if Arm(num,len(str(num)))==num:
    print('Arm strong number')
else:
    print('Nota a Arm strong number')

print('-'*20)

def Arm(num,power):
    if(num==0):
        return 0
    return (num%10)**power+Arm(num//10,power)
num=370
print(Arm(num,len(str(num)))==num)


