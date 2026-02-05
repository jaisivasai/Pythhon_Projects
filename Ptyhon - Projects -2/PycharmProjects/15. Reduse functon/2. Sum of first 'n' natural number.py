from functools import reduce
"""finding suno of first n natural of 5 """
r=reduce(lambda x,y: x+y,range(1,6))
print(r)