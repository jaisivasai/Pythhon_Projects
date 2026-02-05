# print given pattern using for loop(outer,inner loop)
#    5
#   45
#  345
# 2345
#12345

space = 4
for a in range(5,0,-1):
    print(' '*space,end='')
    for b in range(a,6):
        print(b,end='')
    print()
    space-=1