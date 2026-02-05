with open('writeline-m2.txt') as f:
    print(f.tell())
    print(f.read())
    print(f.tell())
    f.seek(0)
    print(f.tell())