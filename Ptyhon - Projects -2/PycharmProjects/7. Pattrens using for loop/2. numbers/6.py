# print given pattern using for loop
#11111
#-2222
#--333
#---44
#----5

a = 1
b = 5
for space in range(0,5):
    print("{}{}".format('-'*space,str(a)*b))
    a+=1
    b-=1