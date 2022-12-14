import boto3


region = 'us-east-1'
ec2_client = boto3.client('ec2',region_name=region)

dev_instances = ec2_client.describe_tags(Filters=[{'Name': 'tag:Environment', 'Values': ['Dev']}])

all_running_instances = ec2_client.describe_instance_status()
running_instances = all_running_instances['InstanceStatuses']
running_instance_id = []
for i in running_instances:
    running_instance_id.append(i['InstanceId'])
#print(running_instance_id)

dev_instance_tags = dev_instances['Tags']
dev_instance_Id = []
for i in dev_instance_tags:
    dev_instance_Id.append(i['ResourceId'])
#print(dev_instance_Id)

for _ in dev_instance_Id:
    if _ in running_instance_id and dev_instance_Id:
        for ids in range(len(dev_instance_Id)):
            id=dev_instance_Id[ids]
            ec2_client.stop_instances(InstanceIds=[id])
            


#for _ in dev_instances:
    #if _ in all_running_instances and dev_instances:
        #for ids in range(len(dev_instance_Id)):
            #id=dev_instance_Id[ids]
            #ec2_client.stop_instances(InstanceIds=[id])