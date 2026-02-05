def fun():
    n=20 #local
    print('local:{}'.format(n))
n=10 #global
fun()
print('global:{}'.format(n))
