num =101
copy=num
rev=0
while(num!=0):
    rev=(rev*10)+(num%10)
    num//=10
if(copy==rev) and (copy > 1):
    # ---------check prime are not , its prime means its poly-prine---------
    for p in range(2, copy // 2 + 1):
        if (copy % p == 0):
                print('Not a ployprime number')

    else:
        print('PolyPrime number')
else:
    print('Not a poly number')
