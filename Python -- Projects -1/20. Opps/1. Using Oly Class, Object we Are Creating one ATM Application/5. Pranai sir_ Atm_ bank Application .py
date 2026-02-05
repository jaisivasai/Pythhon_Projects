class sbiBank:
    bname='btm'
    roi=0.02

    def __init__(self,name,gender,mob,bal,acco,pin):
        self.name = name
        self.gender = gender
        self.mob = mob
        self.bal = bal
        self.acco = acco
        self.pin = pin

    def Details(self):
        if self.pin == self.getpin():
            print(f'name :- {self.name}')
            print(f'gender :- {self.gender}')
            print(f'mob :- {self.mob}')
            print(f'bal :- {self.bal}')
            print(f'acco :- {self.acco}')

        else:
            print('pin In-correct')

    def withdraw(self):
        if self.pin == self.getpin():
            print('************** Only 500 and 200 note are Available ***************')
            n=int(input('Enter the amount:-'))
            if n<=self.bal:
                self.bal-=n
                print('Transaction Successful')
                print(f'Current balance is  -- {self.bal}')
            else:
                print('Insufficient balance')
        else:
            print('pin In-correct')

    def Deposite(self):
        if self.pin == self.getpin():
            print('********** Up to 100000 you can Deposite a Day ************')
            n=int(input('Enter the amount :-'))
            if n<=100000:
                self.bal+=n
                print('Transaction Successful')
                print(f'Current balance is  -- {self.bal}')
            else:
                print('Daily limit Over')
                print(f'Current balance is  -- {self.bal}')
        else:
            print('Pin In-correct')

    def checkbal(self):
        if self.pin == self.getpin():
            print(f'Current bal is  -- {self.bal}')
        else:
            print('Pin In-correct')

    @staticmethod
    def getpin():
        f=int(input('Enter your pin:'))
        return f



#---- for Changing the ratio we are using class method (' @classmethod ')-----
#----- for every custmer it will change.
    @classmethod
    def modifinginterst(cls):
        cls.roi= 0.01
        print(f'{"Your Updated bank interest ratio is "}:- {cls.roi}')




custmer1=sbiBank('hari','M',4145789,1000,'HARI7101175',1450)
custmer2=sbiBank('sai','M',14789654,20000,'SAO098765432',2458)

custmer1.Details()


