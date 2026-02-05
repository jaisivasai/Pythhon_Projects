def Bi_to_Di(Bin,i):
    if(Bin==0):
        return 0
    return (Bin%10*i+Bi_to_Di(Bin//10,i*2))
Bin=10110
print(Bi_to_Di(Bin,1))