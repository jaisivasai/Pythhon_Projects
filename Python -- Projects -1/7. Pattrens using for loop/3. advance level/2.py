# print given pattern using 2-for loop.(0r)
# use if and else statements.

#  *
# **
#***
# **
#  *

space=2
for a in range(1,4):
    print("{}{}".format(' '*space,'*' * a))
    space-=1
sp=1
for b in range(2,0,-1):
    print("{}{}".format(' '*sp,'*' * b))
    sp+=1

print('------------------------Both Code are Correct Use any One-------------------------------')

space =2
star =1
for a in range(1,6):
    print("{}{}".format(' ' * space,'*' * star))
    if(a<3):
        space -=1
        star +=1
    else:
        space += 1
        star -= 1
