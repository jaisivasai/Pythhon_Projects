d=[10,20,30,40]
d.extend({10:'py',50:'sai'})  # it will allow only keys only
print(d)  # dic

s=['siva sai']
s.extend('jai') # it will saperate each chracter
print(s) #string

l=[100,200,'sai']
l.extend([400,500,'siva'])  #string will not saperate
print(l)  #list

t=[700,80,'raju']
t.extend((500,'sai')) #string will not saperate
print(t)  # tuple

s1=[0,2,1,'jai']
s1.extend({14,23,0,True,False,0,1,'ok'}) # duplicates wil not print in set it will remove.
print(s1)  # set is under data type
