num =0
bin =10110
t =1
while(bin!=0):
    rem=bin % 10
    num=num+(rem*t)
    bin=bin//10
    t*=2
print(num)