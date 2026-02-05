def niven(num,copy):
    add=0
    while(num!=0):
        rem=num%10
        add=add+rem
        num//=10
    return (copy%add==0)
num=126
print(niven(num,num))

print('-'*20)

def niven(num,copy):
    add=0
    while(num!=0):
        rem=num%10
        add=add+rem
        num//=10
    return (copy%add==0)
num=126
print("Niven number" if niven(num,num)else'not a Niven number')
