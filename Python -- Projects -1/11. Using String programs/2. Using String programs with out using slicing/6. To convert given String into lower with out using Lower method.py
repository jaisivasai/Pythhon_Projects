s='AbcD123'
res=''
for a in s:
    if('A'<=a<='Z'):
        res=res+chr(ord(a)+32)
    else:
        res=res+a
print(res)