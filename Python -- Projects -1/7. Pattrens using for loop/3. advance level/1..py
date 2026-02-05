# print given pattern using 2-for loop.(0r)
# use if and else statements.

#*
#* *
#* * *
#* * * *
#* * *
#* *
#*


for a in range(1,5):
    print('* ' * a)
for b in range(3,0,-1):
    print('* ' * b)

print('------------------------Both Code are Correct Use any One-------------------------------')

star =1
for a in range(0,7):
    print('* ' * star)
    if(a<3):
        star+=1
    else:
        star-=1