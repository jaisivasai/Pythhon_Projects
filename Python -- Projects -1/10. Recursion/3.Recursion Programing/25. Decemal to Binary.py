def Di_to_Bi(num,i):
    if(num==0):
        return 0
    return (num%2*i+Di_to_Bi(num//2,i*10))
num=22
print(Di_to_Bi(num,1))