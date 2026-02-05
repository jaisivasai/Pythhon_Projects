num = 28
add = 0
i = 1
while(i != num//2+1):
    if(num % i == 0):
        add=add+i
    i+=1
if(add==num):
    print('perfect number')
else:
    print('not a perfect number')
