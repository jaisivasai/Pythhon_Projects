import json
with open('dumpsfile.txt','r') as a:
    c=json.load(a)
    print(f'python data: {c}')
    print(f'python datatype: {type(c)}')

