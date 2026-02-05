def neo(num,seq):
    add=0
    while(seq!=0):
        rem=seq%10
        add=add+rem
        seq//=10
    return (add==num)
num=9
print(neo(num,num**2))