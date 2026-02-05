l=[12,1,15,7,11,18,13,2]
for num in l:
    i=[]
    add=0
    while(num!=0):
        rem=num%10
        add+=rem
        num//10
    i.append(num)
print(i)