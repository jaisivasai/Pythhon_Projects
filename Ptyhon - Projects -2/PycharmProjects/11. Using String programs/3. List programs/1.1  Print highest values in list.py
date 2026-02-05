l=[-16,-14,-13,-12,-19,-15,]
count=l[0]
for i in range(1,len(l)):
    if(l[i]>count):
        count=l[i]
print(count)

