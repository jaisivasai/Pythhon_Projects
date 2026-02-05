# To find Index position input/given number.

l=[0,2,5,9,4,7,8,8,10]
user = 8
l.sort()
print(l)
for i in range(len(l)):
    if l[i] == user:
        print(f'Index position is:- {i}')
        break
else:
    print(-1)

print('-'*20) #----------------------------

l=[0,2,5,9,4,7,8,8,10]
user = int(input('Enter the num:- '))
l.sort()
print(l)
for i in range(len(l)):
    if l[i] == user:
        print(f'Index position is:- {i}')
        break
else:
    print(-1)

