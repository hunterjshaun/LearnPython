import boto3


region = 'us-east-1'
ec2_client = boto3.client('ec2',region_name=region)
ec2 = boto3.resource('ec2', region_name=region)

dev_instances = ec2_client.describe_tags(Filters=[{'Name': 'tag:Enviroment', 'Values': ['Dev']}])
running_instances = ec2_client.describe_instance_status()
dev_instance_tags = dev_instances['Tags']
dev_instance_Id = []
for i in dev_instance_tags:
    dev_instance_Id.append(i['ResourceId'])

for i in dev_instances:
    if i in running_instances and dev_instances:
        for ids in dev_instance_Id:
            id=dev_instance_Id
            ec2_client.stop_instances(InstanceIds=[id])
    
#for instances in dev_instances:
    #if instances in running_instances and dev_instances:
        #id=dev_instances['Tags'][0]['ResourceId']
        #ec2_client.start_instances(InstanceIds=[id])
#$response = client.start_instances(InstanceIds=[id],)

#print(dev_inst.get['ResourceId'])
#dev = dev_instances['Tags']
#dev_instId = []
#for value in dev:
   #dev_instId.append(value['ResourceId'])
#print(dev)
#print(dev)
#print(dev_inst_tag)
#print(dev2)