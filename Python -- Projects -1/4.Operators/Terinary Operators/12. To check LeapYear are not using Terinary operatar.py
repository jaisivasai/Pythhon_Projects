# If it's a 'century year divisible  with 400'
# If it's a 'non-century year divisible  with 4'
# using Terninary operatar(if and else).

y = 1880
print('leap year' if (y%4==0 and y%100!=0) or (y%400==0) else 'non-leap year')
