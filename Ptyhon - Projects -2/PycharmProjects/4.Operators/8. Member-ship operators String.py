print("--------- string example ----------------" " " "just for under standing------ This line -------")
S='python'
print('z' not in S)
print('p' not in S)
print('z' in S)
print('n' in S)
print('p' in S)
# only string to string compaire



print("------------- List ---------" " " "just for under standing------ This line -------")
L=['java',100,45.5,11,12,1.0]
print('j' in L) #in list it will check full list on string
print('java' in L)
print(1 in L)
print('True' in L)
print('[11,12]' in L) # in side list another list in is false
print('v' not in L)
print('a' in L) #in list it will check full list on string


print("------------- Dic ---------" " " "just for under standing------ This line -------")
D={(11,12):45,'a':10,15:45}
print('a' in D)
print('45' in D)
print(15 not in D)
# In "Dic" we decalir with keywords.


print("------------- tuple ---------" " " "just for under standing------ This line -------")
T=('siva',14,45,78,[1,2])
print('s' in T)
print('siva' in T)
print([1,2] not in T)
print(45 in T)


print("------------- set ---------" " " "just for under standing------ This line -------")
s={1,4,7,8,5,'saisai'}
print('saisai' in s)
print(1 not in s)
print(True in s)