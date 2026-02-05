"""Both even and odd numbers printed using functions"""
def even(num):
    return (num%2 == 0)
def odd(num):
    return (num%2 != 0)
num=[12,91,14,23,17,16,19]
f=list(filter(even,num))+list(filter(odd,num))
print(f)

"""even numbers printed using functions"""
print('-'*20)

def even(num):
    return (num%2 == 0)
num=[12,91,14,23,17,16,19]
f=list(filter(even,num))
print(f)


"""odd numbers printed using functions"""
print('-'*20)

def odd(num):
    return (num%2 != 0)
num=[12,91,14,23,17,16,19]
f=list(filter(odd,num))
print(f)

