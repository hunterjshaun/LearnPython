import boto3


region = 'us-east-1'
ec2_client = boto3.client('ec2',region_name=region)
ec2 = boto3.resource('ec2', region_name=region)

running_instance = ec2.instances.filter(Filters=[{'Name': 'instance-state-name','Values': ['running']}])
print(running_instance.id)