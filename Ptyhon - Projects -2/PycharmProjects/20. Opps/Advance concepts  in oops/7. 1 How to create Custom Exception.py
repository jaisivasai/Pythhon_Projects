class student(Exception):
    def __init__(self,msg=''):
        self.msg = msg
    def __str__(self):
        return self.msg
raise student('Understand the logic first')