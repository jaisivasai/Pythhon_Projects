num =18
count =0
while(num!=0):
    reminder=num % 2
    if(reminder == 1):
        count=count+1
    num = num//2
if(count % 2 ==0):
    print('Evil number')
else:
    print('Not a evil number')