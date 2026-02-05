try:
    l=[4,3,'a',9,2,1]
    for i in l:
        print(l[i])
except TypeError as msg:
    print(msg)

print('-'*20)  #----------------------------------------

try:
    l=[4,3,5,9,2,1]
    for i in l:
        print(l[i])
except IndexError as msg:
    print(msg)

print('-'*20)  #----------------------------------------

try:
    l=[4,3,5,9,2,1]
    print(l.index(40))
except ValueError as msg:
    print(msg)


print('-'*20)  #----------------------------------------

try:
    l=[4,3,5,9,2,1]
    for i in l:
        print(l[i])
except IndexError as msg:
    print(msg)

except TypeError as msg:
    print(msg)

except:
    print('unknown error')



print('-'*20)  #----------------------------------------


try:
    l=[4,3,'a',9,2,1]
    for i in l:
        print(l[i])
except (ValueError,IndexError,TypeError) as msg:
    print(msg)