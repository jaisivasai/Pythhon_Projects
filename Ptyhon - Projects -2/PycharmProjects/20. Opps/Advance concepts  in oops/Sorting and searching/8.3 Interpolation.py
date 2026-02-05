l=[7,0,1,15,10,18]
user = int(input('Enter the num:- '))
l.sort()
print(l)
low = 0
high = len(l)-1
while low<= high and l[low] <= user <= l[high]:
    index = int(low+((low - high)/(l[low] - l[high])) *(user - l[low]))

    if l[index] < user:
        low = index + 1
    elif l[index] > user:
        high = index -1
    elif l[index] == user:
        print(f'Elements is found :- {index}')
        break
else:
    print(-1)
