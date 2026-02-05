#Default value in ['0' Starting index] Only in slicing, and [Ending index is given len(sequence)].

S= "WE ARE GROOT"
print(S[0:2])
print(S[3:6])
print(S[7:12])

print('-'*20)

S= "EGNGINEERING"
print(S[:])
print(S[3:len(S)])
print(S[0:len(S)])
print(S[0:7])
print(S[2:])

print('-'*20)

s='I AM INEVITABLE'
print(s[::2])
print(s[::3])
print(s[::5])

print('-'*20)

s='WE WORK HARD'
print(s[::-1])
print(s[-1:-5:-1])
print(s[-6:-10:-1])
print(s[-11:-13:-1])
