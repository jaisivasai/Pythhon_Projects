def singletone(cls):
    d={}
    def inner():
        if(cls not in d):
            d[cls]=cls()
        return d[cls]
    return inner

@singletone
class f1:
    def __init__(self):
        self.tickets=300
    def booking(self):
        n=int(input('Enter no.of tickets :- '))
        if self.tickets >= n:
            self.tickets-=n
            print('Tickets booked successfully')
        else:
            print('Tickets not booked')


def Phonepay():
    obj = f1()
    obj.booking()

Phonepay()
Phonepay()
Phonepay()



