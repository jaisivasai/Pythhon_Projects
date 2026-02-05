l=[2,4,5,1,7,1,8]
target=9
for i in range(0,7):
    for j in range(i+1,8):
        sum=0
        for x in l[i:j]:
            sum+=x
        if (sum == target):
            print(l[i:j])

print('-'*20)
"""
l=[2,4,5,1,7,1,8]
target=9
for i in range(0,7):
    for j in range(i+1,8):
        if(sum(l[i:j])==target):
            print(l[i:j])"""
