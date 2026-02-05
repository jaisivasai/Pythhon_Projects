# To find user input/given number is present are not
l=[0,1,7,8,4,5,9,8,7]
user = 7
for i in l:
    if i==user:
        print('Iterm found')
        break
else:
    print('Iterm not found')

print('-'*20) #----------------------------

l=[0,1,7,8,4,5,9,8,7]
user = int(input('Enter the num:- '))
for i in l:
    if i==user:
        print('Iterm found')
        break
else:
    print('Iterm not found')

