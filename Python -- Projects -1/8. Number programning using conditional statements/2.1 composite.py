# To check and print given number is composite number are not a composite number.
# if given number has more than 4 factors it's a composite number


num= 47
for p in range(2,num//2+1):
    if(num % p == 0):
        print('composite number')
        break
else:
    print('Not a composite number')
