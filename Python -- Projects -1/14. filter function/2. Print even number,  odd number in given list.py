"""Even number"""

l=[12,91,14,23,17,16,19]
even=list(filter(lambda n:n%2 == 0,l))
print(even)

print('-'*20)

"""odd number"""

l=[12,91,14,23,17,16,19]
odd=list(filter(lambda n:n%2 != 0,l))
print(odd)

print('-'*20)

"""Even number and odd number"""

l=[12,91,14,23,17,16,19]
even=list(filter(lambda n:n%2 == 0,l))
odd=list(filter(lambda n:n%2 != 0,l))
print(even+odd)

