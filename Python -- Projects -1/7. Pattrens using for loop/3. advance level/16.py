"""
*       *   * * * *
* *     *   *     *
*   *   *   *     *
*     * *   * * * *

"""


for x in range(4):
    for y in range(10):
        if y==0 or y==4 or (x==1 and y==1) or (x==2 and y==2) or (x==3 and y==3) \
                or y==6 or y==9 or (x==0 and y==7) or (x==0 and y==8) or (x==3 and y==7) or (x==3 and y==8) :
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

