with open('writeline-m1.txt') as f:
    print(f.tell())
    print(f.readline(3))
    print(f.tell())
    print(f.readline(5))
    f.seek(0)
    print(f.readline(5))
