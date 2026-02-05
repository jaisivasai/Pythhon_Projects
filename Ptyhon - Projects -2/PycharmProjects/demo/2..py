l=[[40,20,'cat'],[[[[3]]],'dog'],[(40,30,),50]]
x=str(l)
m=[]
for i in x:
    res=''
    if i not in "[]()'":
        res+=i
