# print given pattern using for loop
#*****
#-****
#--***
#---**
#----*

star=5
for space in range(0,5):
    print("{}{}".format(' ' * space,'*' * star))
    star-=1