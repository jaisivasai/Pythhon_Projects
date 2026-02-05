def outer(func):  # Address Stored decorator function.
    def ineer(x,y):
        if(x>y):
            func(x,y)    # Sub function Class
        else:
            func(y,x)    # Address of sub
    return ineer
@outer
def sub(a,b):
    print(a-b)

sub(10,20)
sub(7,5)
sub(10,15)

@outer
def div(a,b):
    print(a/b)

div(20,5)
div(10,500)