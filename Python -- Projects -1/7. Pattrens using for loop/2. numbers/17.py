# print given pattern using for loop(outer,inner loop)
#12345
# 1234
#  123
#   12
#    1

space = 0
for a in range(6,1,-1):
    print(' '*space,end='')
    for b in range(1,a):
        print(b,end='')
    print()
    space+=1