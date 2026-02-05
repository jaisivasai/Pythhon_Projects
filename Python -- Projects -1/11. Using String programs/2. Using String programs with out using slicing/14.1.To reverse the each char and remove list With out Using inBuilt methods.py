s='we are in class'
ss=''    #----Empty string
rev=''   #----Empty string
for a in s:
    if(a != ' '):
        ss=a+ss
    else:
        rev+=ss+' '    #Empty space
        ss=''       #----Empty string
rev=rev+ss
print(rev)