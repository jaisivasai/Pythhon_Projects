def Auto(num,seq):
    while(num!=0):
        rem1=num%10
        rem2=seq%10
        return (rem1==rem2)
        num//=10
        seq//=10
num=76
print(Auto(num,num**2))