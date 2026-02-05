def fun(a=1,b=2,c=3):
    print(f'a:{a}')
    print(f'b:{b}')
    print(f'c:{c}')
fun()

print('-'*20) #-------------------

def fun(a,b=2,c=3):
    print(f'a:{a}')
    print(f'b:{b}')
    print(f'c:{c}')
fun(10)

print('-'*20) #-------------------

def fun(a,b,c=3):
    print(f'a:{a}')
    print(f'b:{b}')
    print(f'c:{c}')
fun(10,20)

print('-'*20) #-------------------

def fun(a,b,c):
    print(f'a:{a}')
    print(f'b:{b}')
    print(f'c:{c}')
fun(10,20,30)

print('-'*20) #-------------------

def fun(a,b,c='none'):
    print(f'a:{a}')
    print(f'b:{b}')
    print(f'c:{c}')
fun(10,20)



