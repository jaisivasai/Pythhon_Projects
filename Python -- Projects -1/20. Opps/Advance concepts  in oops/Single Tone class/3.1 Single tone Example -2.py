# cls    ---------  To store class address
# cls()  ---------  To store Object address

def singletone(cls):
    d={}    # Create Empty dic in Non-local Space.
    def inner():
        if(cls not in d):
            d[cls]=cls()
        return d[cls]
    return inner

@singletone
class a:
    def __init__(self):
        print('hi')

obj1 = a()   # ---- Inner Function
obj2 = a()   # ---- Inner Function
obj3 = a()   # ---- Inner Function
