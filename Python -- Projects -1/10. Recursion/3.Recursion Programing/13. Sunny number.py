def sunny(num,i):
    if(i**2>num):
        return False
    if(i**2==num):
        return True
    return (sunny(num,i+1))
num=24
if(sunny(num+1,1)):
    print('Sunny number')
else:
    print('Not a Sunny number')

print('-'*20)#--------Type1-----------

def sunny(num,i):
    if(i**2>num):
        return False
    if(i**2==num):
        return True
    return (sunny(num,i+1))
num=24
print(sunny(num+1,1))