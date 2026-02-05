s='ABCBCBD'
l=[]
h=0
for i in range(0,len(s)):
    for j in range(i+1,len(s)+1):
        ss=(s[i:j])
        if(ss==ss[::-1]) and (ss not in l):
            print(ss)
            l.append(ss)
            if(len(ss))>h:
                h=len(ss)
for i in l:
    if(len(i)==h):
        print(i)

