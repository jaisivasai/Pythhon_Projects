# """worldwide useig this only"""
# tuple we return

def fun(*args) :
    print(f'args:{args}')
fun()

print('-'*20) #-------------------

def fun(*args) :
    print(f'args:{args}')
fun(11,12,13)

print('-'*20) #-------------------

def fun(*args) :
    print(f'args:{args}')
fun(11,12,13)
fun(10,20,32)
fun(100,20)
