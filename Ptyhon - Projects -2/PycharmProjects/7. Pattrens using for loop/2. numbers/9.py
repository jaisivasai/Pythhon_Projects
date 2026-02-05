# print given pattern using for loop(outer,inner loop)
#1 2 3 4 5
#1 2 3 4
#1 2 3
#1 2
#1

for x in range(6,1,-1):
    for y in range(1,x):
        print(y,end=' ')
    print()

