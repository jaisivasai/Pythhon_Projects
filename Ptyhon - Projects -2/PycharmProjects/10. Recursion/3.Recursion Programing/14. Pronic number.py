def pronic(num,n):
    if(n*(n+1)>num):
        return False
    if(n*(n+1)==num):
        return True
    return (pronic(num,n+1))
num=12
if(pronic(num,1)):
    print('Pronic number')
else:
    print('Not a Pronic number')

print('-'*20)#--------Type1-----------

def pronic(num,n):
    if(n*(n+1)>num):
        return False
    if(n*(n+1)==num):
        return True
    return (pronic(num,n+1))
num=12
print(pronic(num,1))