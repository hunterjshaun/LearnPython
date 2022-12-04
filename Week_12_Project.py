 #AWS Service Inventory

# Create a list of services using Python. IE: S3, Lambda, EC2, etc

# 1. The list should be empty initially.
# 2. Populate the list using append or insert.
# 3. Print the list and the length of the list.
# 4. Remove two specific services from the list by name or by index.
# 5. Print the new list and the new length of the list.

# Create an empty list
services = []

# Populate the list using append or insert.
services.append('EC2')
services.append('Lambda')
services.append('ECS')
services.append('DynamoDB')
services.append('IAM')
services.append('CodeCommit')

# print the list and length of the list
print(services)
print(len(services))
# Will rerutn ['EC2', 'Lambda', 'ECS', 'DynamoDB', 'IAM', 'CodeCommit']
# Will return 6

# Remove 2 specific services from the list by name or by index
# Print the new list and teh new length of the list
del services[2:4]
print(services)
# will return ['EC2', 'Lambda', 'IAM', 'CodeCommit'] and remove delete ['ECS', 'DynamoDB']
print(len(services))
# will return 4