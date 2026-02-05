# print given pattern using for loop(outer,inner loop)
#5 4 3 2 1
#5 4 3 2
#5 4 3
#5 4
#5

for x in range(0,5):
    for y in range(5,x,-1):
        print(y,end=' ')
    print()

