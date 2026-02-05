import json
with open('dumpsfile.txt','r') as a:
    x = a.read()
    print(f'json data: {x}')
    print(f'json datatype: {type(x)}')
    c=json.loads(x)
    print(f'python data: {c}')
    print(f'python datatype: {type(c)}')

