# We will design a script to allow us to generate EC2 instance names for authorized departments.
# The authorized departments are 'Accounting', 'Marketing', 'FinOps'

# The string module will give us access to string constants.
import string
# The random module will allow us to generate random strings.
import random
# Here we are going to define the variable 'department' using the users input. 
# We can use the '.lower()' function to make all of the users inputs lowercase. This way we can account for the various ways
# a user may enter the department name.
department = input("Good day, which department are you with? \n Accouting \n Marketing \n FinOps \n \n ").lower()
unique_string = string.ascii_letters + string.digits
# We can use an 'if' statement to verify an authorized department is requesting names.
if department in ['accounting', 'finops', 'marketing']:
    instance_quantity = int(input("\n Please enter the number of instances you require: "))
else:
    print('\nPleaes choose an authorized department')
    exit()
# We can use this 'for loop' to generate a unique instance name by combining a random string with the department name.
for _ in range(instance_quantity):
    ec2_name = department + '_' + ''.join(random.choice(unique_string) for _ in range(7))
    print(f"\n Instance: {ec2_name}")
