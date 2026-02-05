# print given pattern using for loop(outer,inner loop)
#1 2 3 4 5
#2 3 4 5
#3 4 5
#4 5
#5

for x in range(1,6):
    for y in range(x,6):
        print(y,end=' ')
    print()

