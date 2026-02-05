"""even numbers"""
l=[11,12,13,14,15]
n=[i for i in l if i%2 == 0]
print(n)

print('-'*20)
"""odd numbers"""
l=[11,12,13,14,15]
n=[i for i in l if i%2 != 0]
print(n)

print('-'*20)
""" even , odd number """
l=[11,13,12,17,8,19,10,4,2]
even=[i for i in l if i%2 == 0]
odd=[j for j in l if j%2 == 0]
print(even+odd)

print('-'*20)
""" print even numbers in assiding order , odd number in decending order """
l=[11,13,12,17,8,19,10,4,2]
even=[i for i in l if i%2 == 0]
even.sort()
odd=[j for j in l if j%2 == 0]
odd.sort(reverse=True)
print(even+odd)
