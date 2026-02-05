# print given pattern using for loop(outer,inner loop)
#54321
# 5432
#  543
#   54
#    5

space = 0
for a in range(0,5):
    print(' '*space,end='')
    for b in range(5,a,-1):
        print(b,end='')
    print()
    space+=1