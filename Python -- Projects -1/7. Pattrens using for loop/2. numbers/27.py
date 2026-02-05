# print given pattern using for loop(outer,inner loop)
#    1
#   12
#  123
# 1234
#12345

space = 4
for a in range(2,7):
    print(' '*space,end='')
    for b in range(1,a):
        print(b,end='')
    print()
    space-=1