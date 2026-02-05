# print given pattern using for loop
#*******
#-*****
#--***
#---*

star=7
for space in range(0,4):
    print("{}{}".format('-' * space,'*' * star))
    star-=2