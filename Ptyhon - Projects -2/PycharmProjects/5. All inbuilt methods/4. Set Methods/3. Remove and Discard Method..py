s = {0,44,55,1,2}
s.remove(2)
print(s)
print('') # just for spacing only.


print('----------- Discard data type ----------------')

discard = {0,4,5}
discard.discard(4)
print(discard)
print('') # just for spacing only.


print('----------- Discard data type error ----------------')

discard = {0,4,5}
discard.discard(10) # Given value is not in set ,so it returns 'Given set'.
print(discard)
print('') # just for spacing only.


print('----------- remove data type error ----------------')

remove = {0,4,5}
remove.remove(100) # Given value is not in set ,so it returns 'Keyerror'.
print(remove)
print('') # just for spacing only.

