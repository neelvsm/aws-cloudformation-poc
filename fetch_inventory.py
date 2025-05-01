import boto3
import sys

def fetch_inventory(stack_name):
    print(f"Fetching resources for stack: {stack_name}")
    
    cf = boto3.client('cloudformation')
    ec2 = boto3.client('ec2')
    s3 = boto3.client('s3')

    # Get resources from CloudFormation stack
    response = cf.describe_stack_resources(StackName=stack_name)
    resources = response['StackResources']

    ec2_ids = []
    print("\nResources in stack:")
    for res in resources:
        print(f"- {res['ResourceType']}: {res['PhysicalResourceId']}")
        if res['ResourceType'] == 'AWS::EC2::Instance':
            ec2_ids.append(res['PhysicalResourceId'])

    # List EC2 instance details
    if ec2_ids:
        print("\nEC2 Instance Info:")
        instances = ec2.describe_instances(InstanceIds=ec2_ids)
        for resv in instances['Reservations']:
            for inst in resv['Instances']:
                print(f"Instance ID: {inst['InstanceId']}, State: {inst['State']['Name']}, Type: {inst['InstanceType']}")
    else:
        print("No EC2 Instances found.")

    # List all S3 buckets
    print("\nS3 Buckets:")
    buckets = s3.list_buckets()
    for bucket in buckets['Buckets']:
        print(f"- {bucket['Name']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python fetch_inventory.py <stack-name>")
        sys.exit(1)
    fetch_inventory(sys.argv[1])
