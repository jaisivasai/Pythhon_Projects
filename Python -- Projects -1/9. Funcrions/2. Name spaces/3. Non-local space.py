def outer():
    x=200
    print(f'non-local:{x}')
    def inner():
        global x
        x=300
        print(f'local:{x}')
    inner()
    print(f'non-local:{x}')
x=100
outer()
print(f'global:{x}')

