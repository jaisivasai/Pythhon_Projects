l=[7,0,1,15,1,10,18]
user = int(input('Enter the num:- '))
l.sort()
print(l)
low = 0
high = len(l)-1
while low<= high and l[low] <= user <= l[high]:
    mid= (low + high)//2
    if l[mid] < user:
        low = mid + 1
    elif l[mid] > user:
        high = mid -1
    elif l[mid] == user:
        print(f'Elements is found :- {mid}')
        break
else:
    print(-1)
