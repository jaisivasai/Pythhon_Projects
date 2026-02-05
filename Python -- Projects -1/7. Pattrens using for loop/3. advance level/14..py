l=[2,5,0,1,6,4]
for i in range (max(l)):
    for j in range(len(l)):
        if l[j]>=1:
            print('*',end=' ')
            l[j]-=1
        else:
            print(' ',end=' ')

    print()