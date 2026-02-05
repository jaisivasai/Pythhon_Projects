d={}
a='1234'  #only collection data types
b=True,2,3   # both collection ,  single data types
print(d.fromkeys(a,b))

D={}
a={1,2,3} #only collection data types
b=[45,5,8]  # both collection ,  single data types
print(d.fromkeys(a,b))


x={}
a={1:10,2:54,3:78} #only collection data types
b=(45,5,8)  # both collection ,  single data types
print(x.fromkeys(a,b))


Y={}
a={1:10,2:54,3:78} #only collection data types
print(x.fromkeys(a))

