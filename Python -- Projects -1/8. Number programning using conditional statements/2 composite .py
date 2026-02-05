#To check and print given number is composite number are not a composite number.
# if given number has more than 4 factors it's a composite number


num = 12
count = 0
for a in range(1,num+1):
    if (num % a == 0) :
        count+=1
if (count > 2):
    print('composite number')
else:
    print('Not a composite number')


