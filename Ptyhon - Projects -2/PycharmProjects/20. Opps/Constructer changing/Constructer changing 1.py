class A:
    a=10
class B(A):
    a=20
    super().__init__()

obj1=A()


print(obj1.a)