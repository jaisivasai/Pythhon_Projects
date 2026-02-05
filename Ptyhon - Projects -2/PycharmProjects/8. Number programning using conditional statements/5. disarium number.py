num = 89
copy = num
count=len(str(num))
add = 0
while(num!=0):
    reminder = num % 10
    add = add + (reminder ** count)
    num = num // 10
    count=count-1
if(copy == add):
    print('Disarum number')
else:
    print('Not a Disarum number')