s='AbcD123'
res=''
for a in s:
    if('a'<=a<='z'):
        res=res+chr(ord(a)-32)
    else:
        res=res+a
print(res)