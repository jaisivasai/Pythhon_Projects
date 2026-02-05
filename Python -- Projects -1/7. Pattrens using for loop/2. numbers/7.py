# print given pattern using for loop
#----1
#---22
#--333
#-4444
#55555

num = 1
for space in range(4,-1,-1):
    print("{}{}".format('-'*space,str(num)*num))
    num+=1