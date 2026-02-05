# print given pattern using for loop(outer,inner loop)
#    1
#   21
#  321
# 4321
#54321

space = 4
for a in range(1,6):
    print(' '*space,end='')
    for b in range(a,0,-1):
        print(b,end='')
    print()
    space-=1