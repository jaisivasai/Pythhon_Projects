num = 370
copy = num
count=len(str(num))
add = 0
while(num!=0):
    reminder = num % 10
    add = add + (reminder ** count)
    num = num // 10
if(copy == add):
    print('Arm strong number')
else:
    print('Not a Arm strong')