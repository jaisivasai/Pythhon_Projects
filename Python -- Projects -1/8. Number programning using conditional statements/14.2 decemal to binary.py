num =27
bin = 0
t =1
while(num!=0):
    rem=num%2
    bin=bin+(rem*t)
    num=num//2
    t*=10
print(bin)