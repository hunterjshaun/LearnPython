import boto3


region = 'us-east-1'
client = boto3.client('ec2',region_name=region)

dev_instances = client.describe_tags(Filters=[{'Name': 'tag:Enviroment', 'Values': ['Dev']}])
for instances in dev_instances:
    response = client.describe_instances(Filters=InstanceIds=[])
    #id=ResourceId
    #client.start_instances(InstanceIds=[id])
#$response = client.start_instances(InstanceIds=['i-00b1994deb4a25354'],)
print(response)