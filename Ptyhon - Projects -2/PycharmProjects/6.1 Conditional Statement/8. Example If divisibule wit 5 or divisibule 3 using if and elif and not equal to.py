# Divisible  with 5 print 'fizz'
# Divisible  with 3 print 'buzz'
# Divisible  with 5 and 3 print 'fizzbuzz'  Using if and elif condition and !=,==

number = 5
if(number%5 ==0 and number%3!=0):
    print('fizz')
elif(number%3 ==0 and number%5!=0):
    print('buzz')
elif(number%5 ==0 and number%3 ==0):
    print('fizzbuzz')
