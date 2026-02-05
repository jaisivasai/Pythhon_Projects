from functools import reduce
l=[15,20,25,35]
"""Sum of value in given list """
r=reduce(lambda x,y: x+y,l)
print(r)