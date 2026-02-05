Name = 'sivasai'
Age = 28
Salary = 50000
print('{} is {} years old and he is earning {} per month'.format(Name,Age,Salary)) # Method -- 1
print('{} is {} years old and he is earning {} per month'.format(Age,Salary,Name)) # This format is not correct.
print('{2} is {0} years old and he is earning {1} per month'.format(Age,Salary,Name))  # Method -- 2
print('{N} is {A} years old and he is earning {S} per month'.format(A = Age,S = Salary,N = Name))  # Method -- 3
print(f'{Name} is {Age} years old and he is earning {Salary} per month')  # Method -- 4