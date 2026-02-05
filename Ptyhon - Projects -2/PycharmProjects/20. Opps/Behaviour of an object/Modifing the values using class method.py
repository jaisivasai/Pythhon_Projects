class sample:
    @classmethod
    def l(cls,x):
        m=200
        cls.m=x
obj1=sample()
obj1.l(400)  # using object name

print(sample.m) # using class name
print(obj1.m)


