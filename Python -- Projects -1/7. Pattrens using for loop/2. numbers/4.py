# print given pattern using for loop
#55555
#-4444
#--333
#---22
#----1

i = 5
for space in range(0,5):
    print("{}{}".format('-' * space, str(i)*i))
    i-=1