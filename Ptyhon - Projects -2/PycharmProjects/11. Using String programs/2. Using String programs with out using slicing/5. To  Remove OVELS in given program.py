s='ENGINEERING'
rem=''
for i in s:
    if i not in 'AEIOaeio':
        rem+=i
print(rem)