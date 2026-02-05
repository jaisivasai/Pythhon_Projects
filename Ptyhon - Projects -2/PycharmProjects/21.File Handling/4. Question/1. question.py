with open('write example1.txt','w') as f:
    f.write('I \nneed \na \njob jai')

# To count how many lines present in given file
with open('write example1.txt','r') as f:
    countlines = 0
    for a in f:
        a = a.strip('\n')
        countlines +=1
    print(f'number of lines = {countlines}')

# To count how many words present in given file
with open('write example1.txt','r') as f:
    countwords = 0
    for a in f:
        for b in a.split():
            countwords +=1
    print(f'number of words = {countwords}')

# To count how count each-charter present in given file
with open('write example1.txt','r') as f:
    countchar= 0
    for a in f:
        for b in a.split():
            countchar += len(b)
    print(f'number of char = {countchar}')
