a='we are what we are we'
l1=a.split()
l2=[]
count=0
for b in l1:
    if(l1.count(b)>count):
        count=l1.count(b)
for b in l1:
    if(l1.count(b)==count)and (b not in l2):
        print(b)
        l2.append(b)
