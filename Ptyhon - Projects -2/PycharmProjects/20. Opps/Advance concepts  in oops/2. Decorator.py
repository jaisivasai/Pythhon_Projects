def outer(func):
    print('func:{}'.format(func))
    def ineer():
        print('Haii')
    return 100 #(ineer)
@outer
def sample():
    print('Helloworld')
print(sample)