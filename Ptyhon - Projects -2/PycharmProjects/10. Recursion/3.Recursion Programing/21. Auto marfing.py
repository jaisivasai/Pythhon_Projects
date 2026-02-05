def Auto(num,Sequare):
    if(num==0):
        return True
    if(num%10!=Sequare%10):
        return False
    return Auto(num//10,Sequare//10)
num=25
print(Auto(num,num**2))

print('-'*20)#-----Type1-------------

def Auto(num,Sequare):
    if(num==0):
        return True
    if(num%10!=Sequare%10):
        return False
    return Auto(num//10,Sequare//10)
num=25
if(Auto(num,num**2)):
    print('Auto-marfing')
else:
    print('Not a Auto-Marfing')