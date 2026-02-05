l=[9,10,5,3,7]
for i in range(1,len(l)):
    h =i
    val = l[h]
    while h>0 and val<l[h-1]:
        l[h] = l[h-1]
        h-=1
    l[h] = val
    print(l)
print('-'* 20)
print(l)
