def outer(cls):
    def inner():
        print('hi')
        x=cls()
        return x
    return inner

@outer
class a:
    def __init__(self):
        print('Helloworld')

n=a()
print(a)