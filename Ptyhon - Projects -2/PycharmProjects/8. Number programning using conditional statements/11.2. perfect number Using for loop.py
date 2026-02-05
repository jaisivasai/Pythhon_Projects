num=28
add =0
for i in range(1,num):
    if(num % i ==0):
        add+=i
if(add==num):
    print('perfect number')
else:
    print('not a perfect number')

