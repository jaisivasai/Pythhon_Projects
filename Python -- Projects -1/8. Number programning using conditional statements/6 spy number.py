num = 1421
add = 0
mul = 1
while(num!=0):
    reminder = num % 10
    add = add + reminder
    mul = mul * reminder
    num = num // 10
if(add == mul):
    print('Spy number')
else:
    print('Not a spy number')