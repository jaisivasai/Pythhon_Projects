with open('example1.txt','r+') as f:
    print(f.read())
    f.write(' yes')
    print(f.read())
