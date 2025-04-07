import json
import boto3

def lambda_handler(event, context):
    client = boto3.client('ec2')
    response = client.run_instances(
    ImageId='ami-076c6dbba59aa92e6',
    InstanceType='t2.micro',
    KeyName='Cust-KeyPair',
    MaxCount=1,
    MinCount=1,
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'server_from_lambda_boto3_git'
                },
            ]
        },
    ]
)

