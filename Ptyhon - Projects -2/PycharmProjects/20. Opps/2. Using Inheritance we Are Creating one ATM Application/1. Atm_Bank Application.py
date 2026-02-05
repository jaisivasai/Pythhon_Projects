"""     Parent - Class will create here"""
class sbiBank_v1:
    bname = 'btm'
    roi = 0.07

    def __init__(self, name, gender, mob, Balance, AccountNumber, pin):
        self.name = name
        self.gender = gender
        self.mob = mob
        self.Balance = Balance
        self.AccountNumber = AccountNumber
        self.pin = pin


    """To Fetch the withdraw Amount -------------------"""
    def withdraw(self):
        if self.pin == self.checkpin():
            print(f'Hi welcome to SBI ATM :) {self.name}')
            n = int(input('Enter the withdraw amount:-'))
            if n <= self.Balance:
                self.Balance -= n
                print('deduction Successful')
                print(f'{self.name} Current Balance is  -- {self.Balance}')
                print()
                print('Successful Logged out')
            else:print('Insufficient balance')
        else:
            print('pin In-correct')
            self.withdraw()

    """To Fetch the Deposit Amount -------------------"""
    def Deposite(self):
        if self.pin == self.checkpin():

            print(f'Hi welcome to SBI ATM :) {self.name}')
            n = int(input('Enter the amount How much amount are Deposit :-'))
            if n <= 100000:
                self.Balance += n
                print(f'Deposit Successful ---:)  Your Current Balance is --{self.Balance}')
                print()
                print('Successful Logged out')
            else:print('Daily limit Over')
        else:
            print('Pin In-correct')
            self.Deposite()

    """To Fetch the check balance  -------------------"""
    def checkbal(self):
        if self.pin == self.checkpin():
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

        # ---- for Changing the ratio we are using class method (' @classmethod ')-----
        # ----- for every custmer it will change.
    @classmethod
    def modifinginterst(cls):
        cls.roi = 0.02
        print(f'{"Your Updated bank interest ratio is "}:- {cls.roi}')


    """Child - Class will create here"""
class sbiBank_v2(sbiBank_v1):

    def __init__(self, name, gender, mob, Balance, AccountNumber, pin, mailId):
        sbiBank_v1.__init__(self, name, gender, mob, Balance, AccountNumber, pin)
        self.mailId = mailId

    """ creating new password """
    def NewPassword(self):
        if self.pin == self.checkpin():
            print(f'Hi welcome to SBI ATM :) {self.name}')
            password1 = int(input('Enter you new pin Here:- '))
            if self.pin != password1:
                password2 = int(input('Re - Enter you pin Here:- '))
                if password2 == password1:
                    self.pin = password1
                    print('New pin Successful Created ')
                else:print('Not Matching...')
                self.NewPassword()
            else:
                print('It Should not match old pin .......  Please Re-enter password')
                self.NewPassword()
        else:print('Pin In-correct')

    """Another Child - Class will create here"""
class sbiBank_v3(sbiBank_v2):

    def __init__(self, name, gender, mob, Balance, AccountNumber, pin, mailId, panNumber, AdhaarNumber):
        sbiBank_v2.__init__(self, name, gender, mob, Balance, AccountNumber, pin,mailId)
        self.panNumber = panNumber
        self.AdhaarNumber=AdhaarNumber

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
            sbiBank_v3.Details(self)


custmer1 =sbiBank_v3('Jaisivasai', 'M', 789654123, 1000, 'AC01245789', 1478, 'sai@gmail.com', 'Pa-0123', 'Adh-14569')
custmer2 =sbiBank_v3('SivaSai', 'M', 789654123, 500, 'AC012345000', 1236, 'sivasai@gmail.com', 'Pa-5555', 'Adh-01212')

custmer1.withdraw()
custmer1.Deposite()
custmer1.checkbal()
