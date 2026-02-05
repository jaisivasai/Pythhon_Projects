"""    *
  * * *
* * sai * *
  * * *
    * """

space=2
for a in range(1,4,2):
    print("{}{}".format('  '*space,'* ' * a))
    space-=1
star=2
for s in range(1,2):
    print("{}{}{}".format('* ' * star,'sai ','* '* star))
sp=1
for b in range(3,0,-2):
    print("{}{}".format('  '*sp,'* ' * b))
    sp+=1
