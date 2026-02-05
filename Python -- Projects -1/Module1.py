"""prime number program using recrusion """

def prime(num,i):
    if(num%i == 0):
        return False
    if(i == num//2+1):
        return True
    return print(num,i+1)

""" Factorial program using recrusion """

def fact (num):
    if(num == 0):
        return 1
    return num*fact(num-1)


if '__name__' =='__main__' :
    print(fact)


