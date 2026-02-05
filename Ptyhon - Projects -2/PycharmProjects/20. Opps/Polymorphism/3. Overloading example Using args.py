"""using *args"""

class cal:
    def add(selfs,*args):
        return sum(args)
obj=cal()
print(obj.add(1,2,3,4))
print(obj.add(1, 2, 3, 4,5))
print(obj.add(1, 2))