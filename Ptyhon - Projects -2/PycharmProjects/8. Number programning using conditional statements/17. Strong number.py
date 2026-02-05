num = 145
copy = num
add = 0
while(num!=0):
    reminder = num%10
    factorial = 1
    for i in range(1,reminder+1):
        factorial=factorial*i
    add=add+factorial
    num=num//10
if(copy == add):
    print('strong number')
else:
    print('not a strong number')