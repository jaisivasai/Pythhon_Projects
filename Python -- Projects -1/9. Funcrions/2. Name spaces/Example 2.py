def fun(num):
    num=num+10
    print('local:{}'.format(num))
num=10
fun(num)
print('global:{}'.format(num))
