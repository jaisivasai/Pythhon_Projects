class A:
    def __init__(self,starting,ending):
        self.starting = starting
        self.ending = ending
    def __iter__(self):
        return self
    def __next__(self):
        currentvalue = self.starting
        if (currentvalue > self.ending):
            raise StopIteration
        self.starting+=2
        return currentvalue **2

obj = A(2,10)
x = iter(obj)
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))








