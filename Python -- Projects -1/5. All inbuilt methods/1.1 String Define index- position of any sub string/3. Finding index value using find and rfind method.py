A= 'ENGINEERING'
print('Here we are using Finding the given sub string -------- find method using')
print(A.find('E',1,7))
print(A.find('NG',1,7))
print(A.find('z')) # -1 is error in find method

print('Here we are using Finding the given sub string -------- rfind method using')
print(A.rfind('E',1,7))
print(A.rfind('NG',1,7))
print(A.rfind('x'))  # -1 is error in find method
