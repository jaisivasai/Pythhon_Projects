s='ABCD'
for i in range(0,4):
    for j in range(i+1,5):
        print(s[i:j])


print('-'*20) # ------- 0r -- it will for all programs. ------

s='ABCD'
for i in range(0,len(s)):
    for j in range(i+1,len(s)+1):
        print(s[i:j])
