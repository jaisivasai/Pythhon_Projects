# Write a program to print  5th  fibinocci number
f,s=0,1
for i in range(0,7):
    temp = f
    f,s=s,f+s
print(temp)
