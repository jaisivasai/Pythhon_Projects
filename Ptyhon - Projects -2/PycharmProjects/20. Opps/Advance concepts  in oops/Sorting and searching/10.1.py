def positon(l,first,last):
    pivot = l[last]
    leftindex = first
    rightindex = last - 1
    while True:
        while leftindex <= rightindex and pivot >= l[leftindex]:
            leftindex+=1
        while leftindex <= rightindex and pivot <= l[rightindex]:
            rightindex-=1
        if (leftindex > rightindex):
            break
        else:
            l[leftindex],l[rightindex] = l[rightindex],l[leftindex]
    l[last],l[leftindex] = l[leftindex],l[last]
    return leftindex

def quicksort(l,first,last):
    if (first < last):
        p=positon(l, first, last)
        quicksort(l, first, p-1)
        quicksort(l, p + 1, last)
l=[4,1,9,6,0]
quicksort(l,0,len(l)-1)
print(l)

