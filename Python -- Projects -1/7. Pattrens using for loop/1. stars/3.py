# print given pattern using for loop
#----*
#---**
#--***
#-****
#*****

star=1
for space in range(4,-1,-1):
    print("{}{}".format(' ' * space,'*' * star))
    star+=1