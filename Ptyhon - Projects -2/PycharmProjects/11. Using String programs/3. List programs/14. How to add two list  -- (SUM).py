l1=[11,20,30]
l2=[9,5,4,7]
if len(l1)>len(l2):
    for i in range(len(l2)):
        l1[i]+=l2[i]
    print(l1)
else:
    for j in range(len(l1)):
        l2[j]+=l1[j]
    print(l2)

"""print('-'*20)

l1=[11,20,30]
l2=[9,5,4,7,5,5,5,5]
if len(l1)>len(l2):
    l1+=[0]*(len(l1)-len(l2))
else:
    l2 += [0] * (len(l2) - len(l1))
for i in range(len(l1)):
    l1[i]+=l1[i]
print(l1)
print(l2)
"""

