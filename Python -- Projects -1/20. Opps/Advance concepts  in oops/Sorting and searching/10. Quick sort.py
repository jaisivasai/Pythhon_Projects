def positon(l,first,last):
    pivot = l[first]
    leftindex = first+1
    rightindex = last
    while True:
        while leftindex <= rightindex and pivot >= l[leftindex]:
            leftindex+=1
        while leftindex <= rightindex and pivot <= l[rightindex]:
            rightindex-=1
        if (leftindex > rightindex):
            break
        else:
            l[leftindex],l[rightindex] = l[rightindex],l[leftindex]
    l[first],l[rightindex] = l[rightindex],l[first]
    return rightindex

def quicksort(l,first,last):
    if (first < last):
        p=positon(l, first, last)
        quicksort(l, first, p-1)
        quicksort(l, p + 1, last)
l=[4,1,9,6,0]
quicksort(l,0,len(l)-1)
print(l)

