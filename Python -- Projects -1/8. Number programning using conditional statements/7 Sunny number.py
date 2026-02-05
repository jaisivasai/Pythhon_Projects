num = 23
i = 1
while(i ** 2<= (num+1)):
    if(i ** 2 == num+1):
        print('Sunny number')
        break
    i=i+1
else:
    print('Not a Sunny number')