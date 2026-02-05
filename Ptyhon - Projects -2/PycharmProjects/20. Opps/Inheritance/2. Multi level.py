class sai: # PARENT class crating
    a=10

class b:  # child class crating
    b=20

class c(b):
    pass
obj= sai() # child class crating
obj1= b()
print(obj1.b)


