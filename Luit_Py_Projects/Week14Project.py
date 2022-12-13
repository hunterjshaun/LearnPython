import boto3


region = 'us-east-1'
ec2_client = boto3.client('ec2',region_name=region)

dev_instances = ec2_client.describe_tags(Filters=[{'Name': 'tag:Enviroment', 'Values': ['Dev']}])
running_instances = ec2_client.describe_instance_status()
#for instances in dev_instances:
    #if instances in running_instances and dev_instances:
        #id=
        #ec2_client.start_instances(InstanceIds=[id])
#$response = client.start_instances(InstanceIds=[id],)
#print(response)
print(dev_instances)