def Try(num,Cube):
    if(num==0):
        return True
    if(num%10!=Cube%10):
        return False
    return Try(num//10,Cube//10)
num=85
print(Try(num,num**3))

print('-'*20)#-----Type1-------------

def Try(num,Cube):
    if(num==0):
        return True
    if(num%10!=Cube%10):
        return False
    return Try(num//10,Cube//10)
num=85
if(Try(num,num**3)):
    print('Try-marfing')
else:
    print('Not a Try-Marfing')