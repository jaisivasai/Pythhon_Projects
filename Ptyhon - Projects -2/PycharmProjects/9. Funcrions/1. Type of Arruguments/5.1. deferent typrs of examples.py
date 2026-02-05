def fun(a,b,c):
    print(f'a:{a}')
    print(f'b:{b}')
    print(f'c:{c}')
fun(b=10,a=20,c=30)
print('_'*20)
fun(30,b=10,a=20) # error

fun(20,0,b=10)

