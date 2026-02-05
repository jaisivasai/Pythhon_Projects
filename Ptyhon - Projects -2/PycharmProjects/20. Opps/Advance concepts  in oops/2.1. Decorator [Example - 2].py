def outer(func):
    def ineer():
        print('Haii')
        func()
    return ineer #(ineer)
@outer
def sample():
    print('Helloworld')

sample()