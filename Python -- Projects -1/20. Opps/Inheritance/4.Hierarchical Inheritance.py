class a: #parent class
    pass
class b: #parent class
    pass
class c(a,b): #child class
    pass
class d(a,b): #child class
    pass
class e(c,d): #child class
    pass
print(e.mro())