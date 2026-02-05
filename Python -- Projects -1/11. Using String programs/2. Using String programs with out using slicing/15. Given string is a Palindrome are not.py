s='ABCABCDEE'
rev=''
for i in range (-1,-5,-1):
    rev=rev+s[i]
if(rev==s):
    print('palindrome')
else:
    print('Not a Palindrome')