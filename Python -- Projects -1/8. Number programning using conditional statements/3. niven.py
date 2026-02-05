num = 123
copy = num
add = 0
while(num!=0):
    reminder = num % 10
    add = add + reminder
    num = num // 10
if(copy % add == 0):
    print('Niven number')
else:
    print('Not a Niven number')