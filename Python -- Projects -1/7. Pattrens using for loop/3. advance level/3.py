# print given pattern using 2-for loop.(0r)
# use if and else statements.


#   *
#  ***
# *****
#*******
# *****
#  ***
#   *

space=3
for a in range(1,8,2):
    print("{}{}".format(' '*space,'*' * a))
    space-=1
space=1
for b in range(5,0,-2):
    print("{}{}".format(' '*space,'*' * b))
    space+=1



print('------------------------Both Code are Correct Use any One-------------------------------')

space =3
star =1
for i in range(1,8):
    print("{}{}".format(' ' * space,'*' * star))
    if(i<4):
        space -=1
        star +=2
    else:
        space += 1
        star -= 2
