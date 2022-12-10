#Here we will need to input the 
import string
import random


department = input("Good day, which department are you with? \n Accouting \n Marketing \n FinOps \n \n ")
unique_string = string.ascii_letters + string.digits
instance_name = department + '_' + ''.join(random.choice(unique_string) for _ in range(7))

if department == "Accounting" or department == "Marketing" or department == "FinOps":
    instance_quantity = int(input("\n Please enter the number of instances you require: "))
    
elif department.lower() == "accounting" or department.lower() == "marketing" or department.lower() == "finops":
    instance_quantity = int(input("\n Please enter the number of instances you require: "))
    
else:
    print('\nPleaes choose an authorized department')
    exit()

for _ in range(instance_quantity):
    ec2_name = department + '_' + ''.join(random.choice(unique_string) for _ in range(7))
    print(f"\n Instance: {ec2_name}")