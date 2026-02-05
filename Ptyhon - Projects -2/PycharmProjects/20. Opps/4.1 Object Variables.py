class py_Spiders:
    branch='btm'
obj1=py_Spiders()
obj2=py_Spiders()

def details(addess,name,gender,batchcode,mobnumber):
    addess.name=name
    addess.gender=gender
    addess.batchcode=batchcode
    addess.mobnumber=mobnumber

details(obj1,'hari','M','Pyd-M1',12554557789)
details(obj2,'sonu','F','Pedd-f2',1457896542)

print(obj1.name,obj1.gender,obj1.batchcode,obj1.mobnumber)
print(obj2.name,obj2.gender,obj2.batchcode,obj2.mobnumber)

