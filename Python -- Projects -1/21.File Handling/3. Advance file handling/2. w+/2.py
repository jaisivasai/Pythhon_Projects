with open('write example1.txt','w+') as f:
    print(f.tell())
    f.write('hai jai')
    print(f.tell())
    print(f.read())
