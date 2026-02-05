def fasci(num):
    s=str(num*1)+str(num*2)+str(num*3)
    for b in range(1,10):
        if(str(b)not in s):
            return False
    return True
num=327
print(fasci(num))