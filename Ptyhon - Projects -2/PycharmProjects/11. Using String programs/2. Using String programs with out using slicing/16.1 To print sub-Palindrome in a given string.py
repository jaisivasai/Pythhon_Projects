s='ABCBCBD'
for i in range(0,len(s)):
    for j in range(i+1,len(s)+1):
        ss=(s[i:j])
        if(ss==ss[::-1]):
            print(ss)

