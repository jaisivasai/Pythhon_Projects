def singletone(cls):
    d={}
    def inner():
        if(cls not in d):
            d[cls]=cls()
        return d[cls]
    return inner

@singletone
class KGF:
    def __init__(self):
        self.tickets=300
    def booking(self):
        n=int(input('Enter no.of tickets :- '))
        if self.tickets >= n:
            self.tickets-=n
            print('Tickets booked successfully')
            Phonepay()
        else:
            print('Tickets not booked')

@singletone
class MAHANATI:
    def __init__(self):
        self.tickets=300
    def booking(self):
        n=int(input('Enter no.of tickets :- '))
        if self.tickets >= n:
            self.tickets-=n
            print('Tickets booked successfully')
            Phonepay()
        else:
            print('Tickets not booked')

@singletone
class F1:
    def __init__(self):
        self.tickets=300
    def booking(self):
        n=int(input('Enter no.of tickets :- '))
        if self.tickets >= n:
            self.tickets-=n
            print('Tickets booked successfully')
            Phonepay()
        else:
            print('Tickets not booked')

@singletone
class Junglebook:
    def __init__(self):
        self.tickets=300
    def booking(self):
        n=int(input('Enter no.of tickets :- '))
        if self.tickets >= n:
            self.tickets-=n
            print('Tickets booked successfully')
            Phonepay()
        else:
            print('Tickets not booked')


@singletone
def Phonepay():
    print(""" 
                0. Main-Menu
                1. KGF
                2. MAHANATI 
                3. F1
                4. Junglebook
                """)
    choose = int(input('Choose which Movie Ticket you want :- '))
    if choose == 0:
        obj= Phonepay()
        obj. booking()
    if choose == 1:
       obj =KGF()
       obj.booking()
    elif choose == 2:
        obj =MAHANATI()
        obj.booking()
    elif choose == 3:
        obj = F1()
        obj.booking()
    elif choose == 4:
        obj =Junglebook()
        obj.booking()
    else:
        if choose <= 5:
            print('Please choose above option only....')

Phonepay()




