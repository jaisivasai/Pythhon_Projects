s='PYTHON'
rev=''
for a in range(5,-1,-1):#for a in range(len(s),-1,-1)
    rev=rev+s[a]
print(rev)

print('-'*20)# ------or-----------
for a in range(-1,7,-1):#for a in range(-1,len(s),-1)
    rev=rev+s[a]
print(rev)

print('-'*5,'Using recursion','-'*5)# Using recursion

def fun(s,i):
    if(i==-7):
        return ''
    return s[i]+fun(s,i-1)
s='PYTHON'
print(fun(s,-1))



