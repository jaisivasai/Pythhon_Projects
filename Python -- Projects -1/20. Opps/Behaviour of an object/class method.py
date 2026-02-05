class sample:
    c=100
    @classmethod
    def l(cls):
        m=200
        print(m)
obj1=sample()
obj1.l()  # using object name
sample.l()  # using class name

