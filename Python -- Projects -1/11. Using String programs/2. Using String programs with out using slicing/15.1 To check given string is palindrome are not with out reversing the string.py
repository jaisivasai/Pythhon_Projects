s="malayalam"
a=-1
for i in range (0,4):
    if(s[i]!=s[a]):
        print('not a palindrome')
        break
    a=a-1
print('Palindrome')

print('-'*20) # ------- 0r -- it will for all programs. ------

s="malayalam"
a=-1
for i in range (0,len(s)//2):
    if(s[i]!=s[a]):
        print('not a palindrome')
        break
    a=a-1
print('Palindrome')