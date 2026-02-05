# Write a Program for Highest among 6 numbers using if,elif,else.
a,b,c,d,e,f = 100,200,300,400,500,600
if(a>b and a>c and a>d and a>e and a>f):
    print('a is high')
elif(b>c and b>d and b>e and b>f):
    print('b is high')
elif(c>d and c>e and c>f):
    print('c is high')
elif(d>e and d>f):
    print('d is high')
elif(e>f):
    print('e is high')
else:
    print('f is high')
