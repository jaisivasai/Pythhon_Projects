# print given pattern using for loop. Using format loop

#111111111
# 2222222
#  33333
#   444
#    5

space=0
num =1
for a in range(9,0,-2):
    print("{}{}".format(' '*space,str(num) *a ))
    space+=1
    num+=1
