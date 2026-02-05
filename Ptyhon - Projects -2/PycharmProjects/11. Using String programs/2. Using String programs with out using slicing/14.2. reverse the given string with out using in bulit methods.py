s='we are in class'
ss=''    #----Empty string
rev=''   #----Empty string
for a in s:
    if(a != ' '):
        ss=ss+a
    else:
        rev=' '+ss+rev    #Empty space
        ss=''       #----Empty string
rev=ss+rev
print(rev)