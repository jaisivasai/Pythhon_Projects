class sbiBank:
    bname='btm'
    roi=0.02

    def __init__(self,name,gender,mob,Balance,acco,pin):
        self.name = name
        self.gender = gender
        self.mob = mob
        self.Balance = Balance
        self.acco = acco
        self.pin = pin

    def Details(self):

        print(f'name :- {self.name}')
        print(f'gender :- {self.gender}')
        print(f'mob :- {self.mob}')
        print(f'Balance :- {self.Balance}')
        print(f'acco :- {self.acco}')
        print()
        print('Successful Logged out')


    def withdraw(self):
        print(f'Hi :) {self.name}')
        n=int(input('Enter the amount:-'))
        if n<=self.Balance:
            self.Balance-=n
            print('Transaction Successful')
            print(f'Current Balance is  -- {self.Balance}')
            print()
            print('Successful Logged out')
        else:
            print('Insufficient Balance')


    def Deposite(self):
        print(f'Hi :) {self.name}')
        n=int(input('Enter the amount :-'))
        if n<=100000:
            self.Balance+=n
            print('Transaction Successful')
            print(f'Current balance is  -- {self.Balance}')
            print()
            print('Successful Logged out')
        else:
            print('Daily limit Over')


    def NewPassword(self):
        if self.pin == self.checkpin():
            password1 = int(input('Enter you new pin Here:- '))
            if self.pin != password1:
                password2 = int(input('Re - Enter you pin Here:- '))
                if password2 == password1:
                    self.pin=password1
                    print('New pin Successful Created ')
                else:print('Not Matching...')
            else:
                print('It Should not match old pin ...............')
                print('Please Re-enter password')
                self.NewPassword()
        else:
            print('Pin In-correct')


    def checkbal(self):
        print(f'Hi :) {self.name}')
        print()
        print(f'Current Balance is  -- {self.Balance}')
        print()
        print('Successful Logged out')

    @staticmethod
    def checkpin():
        f = int(input('Enter your pin :'))
        return f

    #@staticmethod
    def getpin(self):
        if self.pin == self.checkpin():
            self.Atm_all()
        else:
            print('Enter correct pin')
            self.checkpin()

    def Atm_all(self):
        print(f'Hi welcome to SBI ATM :)')
        print(""" 
            0. Details
            1. withdraw 
            2. Deposit
            3. check-bal
            4. Changing-pin
            """)
        choose = int(input('Choose which you want Here ...'))
        if choose == 1:
            sbiBank.withdraw(self)
        elif choose == 2:
            sbiBank.Deposite(self)
        elif choose == 3:
            sbiBank.checkbal(self)
        elif choose == 0:
            sbiBank.Details(self)
        elif choose == 4:
            sbiBank.NewPassword(self)
            self.getpin()

        else:
            if choose <= 5:
                print('Please choose above option only....')




custmer1=sbiBank('hari','M',4145789,1000,'HARI7101175',1450)
custmer2=sbiBank('sai','M',14789654,20000,'SAO098765432',2458)

custmer1.getpin()
