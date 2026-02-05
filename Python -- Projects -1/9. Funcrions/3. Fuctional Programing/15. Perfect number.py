def per(num):
    add=0
    for i in range(1, num):
        if (num % i == 0):
            add += i
    return (add==num)
num=27
print(per(num))
