num= 9
seq = num ** 2
add = 0
while(seq!=0):
    rem = seq % 10
    add = add+rem
    seq = seq//10
if(num == add):
    print('Neon')
else:
    print('not a Neon')