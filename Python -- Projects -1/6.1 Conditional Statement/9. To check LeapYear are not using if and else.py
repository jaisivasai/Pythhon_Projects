# If it's a 'century year divisible  with 400'
# If it's a 'non-century year divisible  with 4'
# using if and else.

y=2025
if(y%100==0):
    if(y%400==0):
        print('leap year')
    else:
        print('non-leap year')
else:
    if(y%4==0):
        print('leap year')
    else:
        print('non-leap year')
