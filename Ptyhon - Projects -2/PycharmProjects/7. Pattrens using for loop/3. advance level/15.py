for i in range(5):
    for j in  range(6):
        if(j==0 or i==2 or j==5):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()