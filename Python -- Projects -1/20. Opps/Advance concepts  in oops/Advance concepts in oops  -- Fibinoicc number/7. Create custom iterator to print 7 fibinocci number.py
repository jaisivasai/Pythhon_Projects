# Create custom iterator to print 7 fibinocci number
class fib:
    def __init__(self,total):
        self.first = 0
        self.last = 1
        self.count = 0
        self.total = total
    def __iter__(self):
        return self
    def __next__(self):
        currentvalue = self.first
        if (self.count == self.total):
            raise StopIteration
        self.count+=1
        self.first,self.last = self.last,self.first+self.last
        return currentvalue

obj = fib(int(input('Enter number:-')))
x = iter(obj)
while True:
    print(next(x))








