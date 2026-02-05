num=2
h=0
while h!=5:
    count=0
    for i in range(1,num+1):
        if(num%i==0):
            count+=1
    if(count==2):
        h+=1
        print(num)
    num+=1
