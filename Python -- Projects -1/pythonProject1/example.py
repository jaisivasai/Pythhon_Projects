
    s= input('Enter:')
for i in s:
    if i not in "AEIOaeio":
        print(i)


s='PYthoH@123'
res=''
for a in s:
    if('a'<=a<='z'):
        res=res+chr(ord(a)-32)
    elif('A'<=a<='Z'):
        res=res+chr(ord(a)+32)
    else:
        res=res+a
print(res)
