# print given pattern using for loop(outer,inner loop)
#1
#1 2
#1 2 3
#1 2 3 4
#1 2 3 4 5

for x in range(2,7):
    for y in range(1,x):
        print(y,end=' ')
    print()

