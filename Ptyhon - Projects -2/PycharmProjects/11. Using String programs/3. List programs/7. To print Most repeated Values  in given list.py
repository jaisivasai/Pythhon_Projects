l=[10,12,12,18,19,18,12,10]
count=0
h=[]
for num in l:
    if(l.count(num)>count):
        count=l.count(num)
for num in l:
    if(l.count(num)==count) and (num not in h):
        print(num)
        l.append(num)
