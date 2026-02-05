import json
with open('dumpfile.txt','w') as a:
    d={'1':1000,'a':2000}
    print(f'Python data: {d}')
    json.dump(d,a)

