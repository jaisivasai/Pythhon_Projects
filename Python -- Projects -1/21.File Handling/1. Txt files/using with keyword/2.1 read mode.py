with open('writeline-m2.txt') as f:
    print(f.tell())
    print(f.read(5))
    print(f.tell())
    f.seek(6)
    print(f.tell())
    print(f.read(2))