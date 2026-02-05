class parent:
    def sample(self):
        print('M1 parent class')
        
class child(parent):
    def sample(self):
        super().sample()
        print('m1 child class')
obj=child()
obj.child()
