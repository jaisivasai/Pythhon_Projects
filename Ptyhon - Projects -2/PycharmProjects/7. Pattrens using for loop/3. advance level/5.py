# print given pattern using for loop.Using format loop

#    5
#   444
#  33333
# 2222222
#111111111

space=4
num =5
for a in range(1,10,2):
    print("{}{}".format(' '*space,str(num) *a ))
    space-=1
    num-=1
