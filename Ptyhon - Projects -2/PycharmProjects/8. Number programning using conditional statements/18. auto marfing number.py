num = 77
square = num ** 2
while(num!= 0):
    reminder1 = num % 10
    reminder2 = square % 10
    if(reminder1!=reminder2):
        print('Not a Auto-marfing')
        break
    num=num//10
    square=square//10
else:
    print('Auto-marfing')

