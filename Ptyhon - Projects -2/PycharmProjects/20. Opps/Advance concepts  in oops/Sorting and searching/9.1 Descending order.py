# Sort the list without using in-built method in Descending order.
l=[25,17,20,28,10]
for i in range(len(l)-1):
    for j in range(len(l)-1-i):
        if l[j] < l[j + 1]:
            l[j],l[j+1] = l[j+1],l[j]
print(l)
