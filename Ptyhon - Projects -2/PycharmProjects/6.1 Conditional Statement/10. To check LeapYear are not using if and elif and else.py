# If it's a 'century year divisible  with 400'
# If it's a 'non-century year divisible  with 4'
# using if and elif and else.

y=1880
if(y%4==0 and y%100!=0):
    print('leap year')
elif(y%400==0):
    print('leap year')
else:
    print('non-leap year')
