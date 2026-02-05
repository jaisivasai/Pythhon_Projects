with open('write example1.txt','w+') as f:
    print(f.tell())
    print(f.read())  # old data will br removed.
