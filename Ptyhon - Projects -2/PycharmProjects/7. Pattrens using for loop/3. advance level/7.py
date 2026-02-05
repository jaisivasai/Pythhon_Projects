# print given pattern using for loop.

#4444444
# 33333
#  222
#   1

space=0
num =4
for a in range(7,0,-2):
    print("{}{}".format(' '*space,str(num) *a ))
    space+=1
    num-=1
