with open('write example1.txt','a+') as f:
    f.write('Hello')
    print(f.read())
    print(f.tell())
    f.write(' world')
    print(f.tell())


