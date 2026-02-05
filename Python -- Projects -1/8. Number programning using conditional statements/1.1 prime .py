#To check and print given number is prime number are not prime number.
# if given number has 2 factors it's a prime number

num =1
if (num>1):
    for p in range(2,num//2+1):
        if(num % p == 0):
            print('Not a prime number')
    else:
        print("prime number")
else:
    print('not a prime number')
