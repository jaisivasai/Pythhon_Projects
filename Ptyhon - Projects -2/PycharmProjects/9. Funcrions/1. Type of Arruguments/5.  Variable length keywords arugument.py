# """worldwide useig this only"""
# dict we return

def fun(**Kwargs) :
    print(f'Kwargs:{Kwargs}')
fun()

print('-'*20) #-------------------

def fun(**Kwargs) :
    print(f'Kwargs:{Kwargs}')
fun(a=11,b=12,c=13)

print('-'*20) #-------------------

def fun(**Kwargs) :
    print(f'Kwargs:{Kwargs}')
fun(x=11,y=12,z=3)
fun(p=10,q=20,v=32)
fun(l=100,n=20)
