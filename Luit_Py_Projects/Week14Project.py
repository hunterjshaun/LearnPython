import boto3


region = 'us-east-1'
ec2 = boto3.client('ec2',region_name=region)

dev_instances = ec2.describe_tags(Filters=[{'Name': 'tag:Enviroment', 'Values': ['Dev']}])
running_instances = ec2.describe_instance_status()
for instances in dev_instances:
    if instances in running_instances:
        id='i-00b1994deb4a25354'
        ec2.start_instances(InstanceIds=[id])
#$response = client.start_instances(InstanceIds=[id],)
#print(response)