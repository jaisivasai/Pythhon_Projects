# Check given given number is fibinocci are not
num =int(input('Enter the number:-'))
f,s= 0,1
while (f <= num):
    if (f == num):
        print('Fibinocci number')
        break
    f,s=s,f+s
else:
    print('not Fibinocci number')
