import json
with open('dumpsfile.txt','w') as a:
    d={'1':1000,'a':2000}
    print(f'Python data: {d}')
    p = json.dumps(d)
    print(f'json data: {p}')
    print(f'json datatype: {type(p)}')
    a.write(p)