#Import the 'boto3' library, which is a Python SDK for interacting with AWS services
import boto3

#Set the region vairiable, and create the 'ec2_client' object which allows the code to interacct with the EC2 service
region = 'us-east-1'
ec2_client = boto3.client('ec2',region_name=region)

#def lambda_handler(event, context):
dev_instances = ec2_client.describe_tags(Filters=[{'Name': 'tag:Environment', 'Values': ['Dev']}])

all_running_instances = ec2_client.describe_instance_status()
running_instances = all_running_instances['InstanceStatuses']
running_instance_id = []
for i in running_instances:
    running_instance_id.append(i['InstanceId'])
    
dev_instance_tags = dev_instances['Tags']
dev_instance_Id = []
for i in dev_instance_tags:
    dev_instance_Id.append(i['ResourceId'])
    
for i in dev_instance_Id:
    #if i not in running_instance_id:
    if i in running_instance_id: 
        running_dev_Id = i
        id=running_dev_Id
        #ec2_client.start_instances(InstanceIds=[id])
        ec2_client.stop_instances(InstanceIds=[id])
        print(running_dev_Id)
        



