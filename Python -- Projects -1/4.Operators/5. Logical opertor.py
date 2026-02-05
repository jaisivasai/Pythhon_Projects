# 1---n -True
# 0-Flase

#Here using and operator.
a = 1 and 3       # True and True =True
b = 0 and 55      # False and True =False
c = 12 and 0      # True and False =False
d = (1,) and 9

#Here using not operator.
e = 5            # it's 1 is a true, But using 'not operator' it will reverse o/p True ony it print False

print(a)
print(b)
print(c)
print(d)
print(not e)

#Here using or operator.
x= 1 or 3    # True or True =True
y = 0 or 4   # False or True =True
z = 5 or 0   # True or False =True
n = (1,) or 9

#Here using not operator.
g = 0             # it's 1 is a False, But using 'not operator' it will reverse o/p False ony it print True

print(x)
print(y)
print(z)
print(n)
print(not g)
