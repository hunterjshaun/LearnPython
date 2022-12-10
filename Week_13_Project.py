#Here we will need to input the 
import string
import random



department = input("Good day, which department are you with? ")
instance_quantity = int(input("Please enter the number of instances you require: "))

unique_string = string.ascii_letters + string.digits
instance_name = department + '_' + ''.join(random.choice(unique_string) for _ in range(7))

for _ in range(instance_quantity):
    ec2_name = department + '_' + ''.join(random.choice(unique_string) for _ in range(7))
    print(ec2_name)