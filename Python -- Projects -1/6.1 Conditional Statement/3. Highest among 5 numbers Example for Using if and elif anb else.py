# Write a Program for Highest among 5 numbers using if,elif,else.
a,b,c,d,e = 10,11,12,13,14
if(a>b and a>c and a>d and a>e):
    print('a is high')
elif(b>c and b>d and b>e):
    print('b is high')
elif(c>d and c>e):
    print('c is high')
elif(d>e):
    print('d is high')
else:
    print('e is high')