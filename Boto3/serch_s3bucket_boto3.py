import boto3

resource = boto3.resource("s3")
for bucket in resource.buckets.all():
    print(bucket)
#It will print: s3.Bucket(name='luitbotobucket')

# HOW TO GET CREATION DATE FOR S3 Bucket
s3_resource=boto3.client("s3")

print(s3_resource.list_buckets()['Buckets'])
# it will print: [{'Name': 'luitbotobucket', 'CreationDate': datetime.datetime(2022, 12, 12, 16, 37, 43, tzinfo=tzlocal())}]