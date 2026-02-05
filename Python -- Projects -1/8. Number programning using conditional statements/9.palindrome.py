num =101
copy=num
rev=0
while(num!=0):
    rev=(rev*10)+(num%10)
    num//=10
if(copy==rev):
    print('palindrome  number')
else:
    print('not palindrome  prime')

