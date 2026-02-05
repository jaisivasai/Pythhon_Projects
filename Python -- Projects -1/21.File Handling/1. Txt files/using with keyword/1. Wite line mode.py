with open('writeline-m1.txt', 'w') as f:
    l=['Developers\n''rules\n''world']
    print(f.tell())
    f.writelines(l)
    print(f.tell())
