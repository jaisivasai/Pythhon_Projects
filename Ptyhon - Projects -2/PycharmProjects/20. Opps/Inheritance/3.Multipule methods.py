class a: # PARENT class crating
    def __init__(self):
        print('parent class a created')

class b:  # PARENT class crating
    def __init__(self):
        print('parent class b created')

class c(b,a):  # child class crating
    def __init__(self):
        a.__init__(self)
        b.__init__(self)
        print('chlid class c created')

obj= c()




