class details:
    student_name='jai'
    Branch_name='btm'
    Subject_code='m1'
hari=details()
sri=details()
print(hari.student_name)
print(sri.Branch_name)

""" Modifing the class variabules details """
print('_'*20)

details.student_name='karjal'
details.Branch_name='Tirupathi'

print(hari.student_name)
print(sri.Branch_name)