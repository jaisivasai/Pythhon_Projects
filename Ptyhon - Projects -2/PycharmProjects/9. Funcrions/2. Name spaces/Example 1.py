# Can you modefiy global variable in local space?
# yes
def fun():
    global n
    n=n+10
    print('local:{}'.format(n))
n=10
fun()
print('global:{}'.format(n))
