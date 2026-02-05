"""
10 9 8 7
6 5 4
3 2
1
"""

m=10
for i in range(5,1,-1):
    for j in range(1,i):
        print(m,end=' ')
        m-=1
    print()
