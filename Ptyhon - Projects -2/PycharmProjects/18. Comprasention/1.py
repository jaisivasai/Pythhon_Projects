x=[i for i in range(4,8)]
print(x)

print('-'*20)

x=[i*10 for i in range(4,8)]
print(x)

print('-'*20)
""" normal method using here """

s1='abc'
s2='xy'
for i in s1:
    for j in s2:
        print(i+j)

print('-'*20)
""" using Comprasention method """
s1='abc'
s2='xy'
x=[i+j for i in s1 for j in s2]
print(x)

