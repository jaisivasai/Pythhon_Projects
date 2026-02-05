num= 327
seq=str(num*1)+str(num*2)+str(num*3)
for a in range (1,10):
    if(str(a) not in seq):
        print('not a Fascinating')
        break
else:
    print('Fascinating')