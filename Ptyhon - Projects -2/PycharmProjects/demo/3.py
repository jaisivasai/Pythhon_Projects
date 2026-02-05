"""
1. print prime factors for the given number in list.
n=350
i=2
L=[]
while i<=n:
    if n%i==0:
        L.append(i)
        n//=i
    else:
        i+=1
print(L)
"""

"""l=[2,5,0,1,6,4]
for i in l:
    for j in range(i,i1):
        print(i *'* ',end=' ')
    print()"""


'''l=[2,5,0,1,6,4]
for i in range(0,max(l)):
    for j in range(0,len(l)):
        if(l[j]>=1):
            print('*',end='')
        else:
            print('',end='')'''


"""l=[2,5,0,1,6,4]
for i in range (max(l)):
    for j in range(len(l)):
        if l[j]>=1:
            print('*',end=' ')
            l[j]-=1
        else:
            print(' ',end=' ')

    print()"""

"""for i in range(5):
    for j in range(4):
        if j ==0 or j==2 or j== 4:
            print('*'* i,end='')
        else:
            print('',end='')
    print()"""

"""for i in range(2):
    for j in range(3):
        print('-',end='')
    print('')"""

for x in range(4):
    for y in range(10):
        if y==0 or y==4 or (x==1 and y==1) or (x==2 and y==2) or (x==3 and y==3) \
                or y==6 or y==9 or (x==0 and y==7) or (x==0 and y==8) or (x==3 and y==7) or (x==3 and y==8) :
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

