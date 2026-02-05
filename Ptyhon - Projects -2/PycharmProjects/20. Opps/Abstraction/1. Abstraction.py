from abc import ABC,abstractmethod

class Royalendfield(ABC):  #parent class
    @abstractmethod  # abstract method
    def cc(self):
        pass
    @abstractmethod   # abstract method
    def millage(self):
        pass
    def gear(self):   #Concreate method
        print('4 gears ----')

class continental_gt(Royalendfield):   # Child class
    def cc(self):
        print(650)
    def millage(self):
        print('11-15')

class Interceptor(Royalendfield):   # Child class
    def cc(self):
        print(650)
    def millage(self):
        print('11-15')

class Himalaya(Royalendfield):   # Child class
    def cc(self):
        print(411)
    def millage(self):
        print('11-15')

obj=continental_gt()
obj1=Interceptor()
obj2=Himalaya()

obj.cc()
obj.millage()



