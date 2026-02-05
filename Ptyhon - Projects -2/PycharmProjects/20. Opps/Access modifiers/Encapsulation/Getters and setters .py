class a:
    def __init__(self):
        self.__z  =40  # private Access modifiers.

    def getters(self): # getters
        return self.__z
    def setters(self):  # setter
        self.__z = int(input('Enter the value- '))
object =a()
print(object.getters())
object.setters()
print(object.getters())