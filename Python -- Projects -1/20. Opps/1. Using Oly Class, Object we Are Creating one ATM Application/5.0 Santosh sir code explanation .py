"""  Class will create here"""

class sbiBank:
    bname = 'btm'
    roi = 0.07

    def __init__(self, name, gender, mob, Balance, AccountNumber, mailId, panNumber, AdhaarNumber, pin):
        self.name = name
        self.gender = gender
        self.mob = mob
        self.Balance = Balance
        self.AccountNumber = AccountNumber
        self.mailId = mailId
        self.panNumber = panNumber
        self.AdhaarNumber = AdhaarNumber
        self.pin = pin

    """To Fetch the customer Details-------------------"""

    def Details(self):
        if self.pin == self.checkpin():

            print(f'AccountNumber :- {self.AccountNumber}')
            print(f'name :- {self.name}')
            print(f'gender :- {self.gender}')
            print(f'mob :- {self.mob}')
            print(f'mailId :- {self.mailId}')
            print(f'panNumber :- {self.panNumber}')
            print(f'AdhaarNumber :- {self.AdhaarNumber}')
            print()
            print('Successful Logged out')
        else:
            print('pin In-correct')
            sbiBank.Details(self)

    """To Fetch the withdraw Amount -------------------"""

    def withdraw(self):
        if self.pin == self.checkpin():
            print(f'Hi welcome to SBI ATM :) {self.name}')
            n = int(input('Enter the amount:-'))
            if n <= self.Balance:
                self.Balance -= n
                print('deduction Successful')
                print(f'{self.name} Current Balance is  -- {self.Balance}')
                print()
                print('Successful Logged out')
            else:
                print('Insufficient balance')
        else:
            print('pin In-correct')
            sbiBank.withdraw(self)

    """To Fetch the Deposit Amount -------------------"""

    def Deposite(self):
        if self.pin == self.checkpin():
            print(f'Hi welcome to SBI ATM :) {self.name}')
            n = int(input('Enter the amount :-'))
            if n <= 100000:
                self.Balance += n
                print('Deposit Successful')
                print(f'Current Balance is  -- {self.Balance}')
                print()
                print('Successful Logged out')
            else:
                print('Daily limit Over')
        else:
            print('Pin In-correct')
            self.Deposite()


    """To Fetch the check balance  -------------------"""

    def checkbal(self):
        if self.pin == self.checkpin():
            print(f'Hi welcome to SBI ATM :) {self.name}')
            print()
            print(f'Current Balance is  -- {self.Balance}')
            print()
            print('Successful Logged out')
        else:
            print('Pin In-correct')
            self.checkbal()

    """It will check current pin and input pin correct are not it will check  -------------------"""

    @staticmethod
    def checkpin():
        f = int(input('Enter your pin :'))
        return f




    def NewPassword(self):
        if self.pin == self.checkpin():
            print(f'Hi welcome to SBI ATM :) {self.name}')
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


    # ---- for Changing the ratio we are using class method (' @classmethod ')-----
    # ----- for every custmer it will change.
    @classmethod
    def modifinginterst(cls):
        cls.roi = 0.02
        print(f'{"Your Updated bank interest ratio is "}:- {cls.roi}')




""" object we are created Here """

custmer1 = sbiBank('JaiSivaSai', 'M', 4145789, 1000, 'Jai7101175', 'g.jaisivasai@gmail.com', 'Pyd-12455', 861054798778,1450)
custmer2 = sbiBank('sai', 'M', 14789654, 20000, 'SAO098765432', 'sivasai@gmail.com', 'Pyd-01255', 861087522222,2458)


custmer1.Deposite()

