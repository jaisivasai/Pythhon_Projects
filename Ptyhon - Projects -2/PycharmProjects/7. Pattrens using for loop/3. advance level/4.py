# print given pattern using for loop.Using format loop

#   1
#  222
# 33333
#4444444


space=3
num = 1
for a in range(1,8,2):
    print("{}{}".format(' '*space,str(num) *a ))
    space-=1
    num+=1
