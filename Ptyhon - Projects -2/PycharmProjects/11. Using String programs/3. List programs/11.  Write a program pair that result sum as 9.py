l=[2,4,3,7,8,5]
target=9
for i in range(0,5):
    for j in range(i+1,6):
        if(l[i]+l[j] == target):
            print(l[i],l[j])