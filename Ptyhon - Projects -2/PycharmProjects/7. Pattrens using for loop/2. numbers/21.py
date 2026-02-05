# print given pattern using for loop(outer,inner loop)
#54321
# 4321
#  321
#   21
#    1

space = 0
for a in range(5,0,-1):
    print(' '*space,end='')
    for b in range(a,0,-1):
        print(b,end='')
    print()
    space+=1