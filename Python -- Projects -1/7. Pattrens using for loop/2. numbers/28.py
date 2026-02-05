# print given pattern using for loop(outer,inner loop)
#    5
#   54
#  543
# 5432
#54321

space = 4
for a in range(4,-1,-1):
    print(' '*space,end='')
    for b in range(5,a,-1):
        print(b,end='')
    print()
    space-=1