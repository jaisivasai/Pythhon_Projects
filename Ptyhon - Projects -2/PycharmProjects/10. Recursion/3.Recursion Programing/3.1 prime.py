def Prime(num,i):
    if(i==num//2+1):
        return True
    if(num%i==0):
        return False
    return (Prime(num,i+1))
num=5
print(Prime(num,2))