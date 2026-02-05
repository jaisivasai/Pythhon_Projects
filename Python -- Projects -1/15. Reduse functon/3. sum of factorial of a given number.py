from functools import reduce
n=4
"""finding factorial of 4 """
r=reduce(lambda x,y: x*y,range(1,n+1))
print(r)