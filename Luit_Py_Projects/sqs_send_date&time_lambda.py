import boto3  # import the boto3 library to use the Amazon Web Services (AWS) Simple Queue Service (SQS)
import datetime # import the datetime module for getting the current time
import json # import the json library to convert the current time to a json object

sqs = boto3.client('sqs') # create a client object to interact with the SQS service
queue_url = 'https://sqs.us-east-1.amazonaws.com/637919856173/my-queue' # URL of the SQS queue

def lambda_handler(event, context):
    current_time = str(datetime.datetime.now()) # Get the current time

    response = sqs.send_message( # Send the message to the SQS queue
        QueueUrl=queue_url,
        MessageBody=current_time
    )

    return { # Return the current date and time in the message body when invoked
        'statusCode': 200,
        'body': json.dumps(current_time)
    }
