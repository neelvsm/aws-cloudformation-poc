import boto3
import sys

def fetch_resources(stack_name):
    cf = boto3.client('cloudformation')
    try:
        resources = cf.describe_stack_resources(StackName=stack_name)['StackResources']
    except Exception as e:
        print(f"Error fetching resources from stack: {e}")
        return

    ec2_ids = []
    s3_buckets = []

    for res in resources:
        if res['ResourceType'] == 'AWS::EC2::Instance':
            ec2_ids.append(res['PhysicalResourceId'])
        elif res['ResourceType'] == 'AWS::S3::Bucket':
            s3_buckets.append(res['PhysicalResourceId'])

    print("== EC2 Instances ==")
    if ec2_ids:
        ec2 = boto3.client('ec2')
        response = ec2.describe_instances(InstanceIds=ec2_ids)
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                print(f"ID: {instance['InstanceId']}, Type: {instance['InstanceType']}, State: {instance['State']['Name']}")
    else:
        print("No EC2 Instances found.")

    print("\n== S3 Buckets ==")
    s3 = boto3.client('s3')
    for bucket in s3_buckets:
        try:
            location = s3.get_bucket_location(Bucket=bucket)
            print(f"Bucket: {bucket}, Region: {location['LocationConstraint']}")
        except Exception as e:
            print(f"Error accessing bucket {bucket}: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python fetch_inventory.py <stack-name>")
        sys.exit(1)
    fetch_resources(sys.argv[1])
