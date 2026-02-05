a='brain is in coma and brain frezz'
l1=a.split()
l2=[]
count=0
for b in l1:
    if(len(b)>count):
        count=len(b)
for b in l1:
    if(len(b)==count) and (b not in l2):
        print(b)
        l2.append(b)
