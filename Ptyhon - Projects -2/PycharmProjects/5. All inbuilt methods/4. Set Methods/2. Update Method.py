S = {True,2,2,3}
S.update({10,1})
print(S)
print('') # just for spacing only.

print('----------- Only Sequence data types allowed ----------------')
print('----------- Str data type ----------------')
print('') # just for spacing only.

str = {1,3,4}
str.update('sivasai')
print(str)
print('') # just for spacing only.


print('----------- list data type ----------------')

list = {1,0,2,3}
list.update([4,5,10,True,0])
print(list)
print('') # just for spacing only.



print('----------- Tuple data type ----------------')

tuple = {55,0,20,3,1}
tuple.update((14,50,100,1,0))
print(tuple)
print('') # just for spacing only.

print('----------- set data type ----------------')

set = {7,8,9}
set.update({7,5,6,9})
print(set)
print('') # just for spacing only.


print('----------- dic data type ----------------')

dic = {4,5}
dic.update({2:10,3:300})
print(dic)
print('') # just for spacing only.
