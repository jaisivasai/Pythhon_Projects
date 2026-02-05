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

print('-'*20)
s='PYthoH@123'
res=''
for a in s:
    if('a'<=a<='z') and ('A'<=a<='Z'):
        res = res + chr(ord(a) + 32 or res + chr(ord(a) -32))
    res = res + a

print(res)

