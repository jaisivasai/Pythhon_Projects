a = 310
b = 220
c = 130
d = 140

if(a>b):
    if(a>c):
        if(a>b):
            print('a is highest')
        else:
            print('b is highest')
    else:
        if(c>b):
            print('c is highest')
        else:
            print('b is highest')
else:
    if(b>c):
        if(b>d):
            print('b is highest')
        else:
            print('d is highest')
    else:
        if(c>d):
            print('c is highest')
        else:
            print('d is highest')