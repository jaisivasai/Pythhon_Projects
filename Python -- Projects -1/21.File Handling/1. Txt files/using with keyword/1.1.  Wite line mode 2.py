with open('writeline-m2.txt', 'w') as f:
    l=['Developers\t''rules\t''world']
    print(f.tell())
    f.writelines(l)
    print(f.tell())
