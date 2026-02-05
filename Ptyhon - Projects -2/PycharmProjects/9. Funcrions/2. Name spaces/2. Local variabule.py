def fun():
    n = 100
    print('local:{}'.format(n))

fun()
print('global:{}'.format(n))