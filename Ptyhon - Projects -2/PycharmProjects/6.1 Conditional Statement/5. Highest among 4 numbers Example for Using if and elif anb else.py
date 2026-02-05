# Write a Program for Highest among 4 numbers using if,elif,else.
a,b,c,d = 10,11,12,13
if(a>b and a>c and a>d):
    print('a is high')
elif(b>c and b>d):
    print('b is high')
elif(c>d):
    print('c is high')
else:
    print('d is high')