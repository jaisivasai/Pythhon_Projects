class a: #parent class
    pass
class b(a): #child class
    pass
class c(a): #child class
    pass
class d(b,c): #parent class
    pass
print(d.mro())