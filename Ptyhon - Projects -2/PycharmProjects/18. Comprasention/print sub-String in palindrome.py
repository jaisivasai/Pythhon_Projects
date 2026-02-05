""" Using normal method """
s='abacaca'
for i in range(0,len(s)):
    for j in range(i+1,len(s)+1):
        if(s[i:j]==s[i:j][::-1]):
            print(s[i:j])

print('-'*20)
""" using Comprasention """
s='abacaca'
n=[s[i:j] for i in range(0,len(s)) for j in range(i+1,len(s)+1) if(s[i:j]==s[i:j][::-1])]
print(n)