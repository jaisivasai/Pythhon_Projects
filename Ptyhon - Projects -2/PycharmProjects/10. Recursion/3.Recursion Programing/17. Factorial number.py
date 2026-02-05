def Fact(num):
    if(num==0):
        return 1
    return (num*Fact(num-1))
num=4
print(Fact(num))