# print given pattern using for loop(outer,inner loop)
#1
#2 1
#3 2 1
#4 3 2 1
#5 4 3 2 1

for x in range(1,6):
    for y in range(x,0,-1):
        print(y,end=' ')
    print()

