# print given pattern using for loop(outer,inner loop)
#12345
# 2345
#  345
#   45
#    5

space = 0
for a in range(1,6):
    print(' '*space,end='')
    for b in range(a,6):
        print(b,end='')
    print()
    space+=1