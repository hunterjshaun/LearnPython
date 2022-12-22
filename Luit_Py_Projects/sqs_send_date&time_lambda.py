import boto3
import datetime
import json

sqs = boto3.client('sqs')
queue_url = 'https://sqs.us-east-1.amazonaws.com/637919856173/my-queue'

def lambda_handler(event, context):
    # Get the current time
    current_time = str(datetime.datetime.now())

    # Send the message to the SQS queue
    response = sqs.send_message(
        QueueUrl=queue_url,
        MessageBody=current_time
    )
    # Return the current date and time in the message body when invoked
    return { 
        'statusCode': 200,
        'body': json.dumps(current_time)
    }
