# print given pattern using for loop
#----5
#---44
#--333
#-2222
#11111

a = 5
b = 1
for space in range(4,-1,-1):
    print("{}{}".format('-'*space,str(a)*b))
    a-=1
    b+=1