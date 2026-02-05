s='aaabbaaaccddd'
#4
count=1
h=0
for i in range(0,12):
    if s[i] == s[i+1]:
        count=count+1
    else:
        if(count>h):
            h = count
            count=1
if(count>h):
    h=count
print(h)