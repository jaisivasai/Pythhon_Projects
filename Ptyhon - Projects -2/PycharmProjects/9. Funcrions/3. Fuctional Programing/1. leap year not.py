def year(y):
    if (y % 100==0 and y % 400==0) or (y % 4==0 and y % 400!=0):
        return True
    return False
y=2024
print(year(y))