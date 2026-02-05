class a:
    def __init__(self):
        self.x    =20  # Access modifiers
        self._y   =30  # protected Access modifiers.
        self.__z  =40  # private Access modifiers.
object =a()
print(object.x)
print(object._y)
print(object.__z)