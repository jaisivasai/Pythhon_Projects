# synatax  def ['Keyword']sample()   [function]:
def sample():
    print('Hai')
print(sample())

print("-"*20) #-----------------------------------

def sample():
    print('Hai')
    return 100
print(sample())

print("-"*20) #------------------------------------

def sample():
    print('Hai')
    return 100
    print('jai')
print(sample())

print("-"*20) #---------------------------------

def sample():
    print('Hai')
    return 100
print(sample(),sample(),sample())


print("-"*20) #---------------------------------

def sample():
    print('Hai')
    return 100
print(sample())
print(sample())


print("-"*20) #---------------------------------

def sample():
    print('Hai')
    return 100,2,-1,87
print(sample())

print("-"*20) #---------------------------------

def sample(x,y):
    print(x)
    print(y)
    return x ** y
print(sample(1,200))

print("-"*20) #---------------------------------

def sample(x,y):
    print(x)
    print(y)
    return y ** x
print(sample(1,400))
