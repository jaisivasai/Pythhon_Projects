a = 100
b = 200
c = 300
d = 400
e = 500

if(a>b):
    if(a>c):
        if(a>d):
            if (a > e):
                print('a is high')
            else:
                print('e is high')
        else:
            if(d>e):
                print('d is high')
            else:
                print('e is high')
    else:
        if(c>d):
            if(c>e):
                print('c is high')
            else:
                print('e is high')
        else:
            if(d>e):
                print('d is high')
            else:
                print('e is high')
else:
    if(b>c):
        if(b>d):
            if(b>e):
                print('b is high')
            else:
                print('e is high')
        else:
            if(d>e):
                print('d is high')
            else:
                print('e is high')
    else:
        if(c>d):
            if(c>e):
                print('c is high')
            else:
                print('e is high')
        else:
            if(d>e):
                print('d is high')
            else:
                print('e is high')



