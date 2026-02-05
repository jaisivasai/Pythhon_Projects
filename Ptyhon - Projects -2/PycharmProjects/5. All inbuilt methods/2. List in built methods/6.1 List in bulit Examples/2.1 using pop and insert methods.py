p = [10,20,30,'a b c',1,2,3,-1,0]
p.insert(p.pop(p.pop(-3)),p.pop(1)) #error
print(p) # it takes right to left
