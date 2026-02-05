l=[12,1,15,7,18,11,23]
res=[]
for num in l:
    count = 0
    for j in range(1,num+1):
        if num % j == 0:
            count+=1
    if count == 2:
        res.append(num)
print(res)