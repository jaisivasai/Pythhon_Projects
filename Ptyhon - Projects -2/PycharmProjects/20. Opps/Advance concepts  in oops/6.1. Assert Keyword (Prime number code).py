try:
    num=7
    assert num>1,'Not prime'
    for i in range(2,num//2+1):
        if(num%i == 0):
            raise AssertionError('Not prime')
except AssertionError as msg:
    print(msg)
else:
    print('prime')