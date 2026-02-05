s='aaabbaaaccddd'
# 3a2b3a2c3d
res=''
count=1
for i in  range(0,12):
    if s[i] == s[i+1]:
        count+=1
    else:
        res+=str(count)+s[i]
        count=1
res+= str(count)+s[-1]
print(res)