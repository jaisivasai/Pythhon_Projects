#To check and print given number is prime number are not prime number.
# if given number has 2 factors it's a prime number

num = 3
count = 0
for a in range(1,num+1):
    if (num % a == 0) :
        count+=1
if (count == 2):
    print('Prime number')
else:
    print('Not a Prime number')


