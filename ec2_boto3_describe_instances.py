import boto3

ec2 = boto3.client('ec2')


# Use the describe_instances() method to get information about EC2 instances.

response = ec2.describe_instances()

for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        for tag in instance['Tags']:

            if instance['State']['Name'] == 'running':
                if tag['Key'] == 'Name':
                    print(tag['Value'], '** [ID]:', instance['InstanceId'], 
                    '** [IP Address]:', instance['PublicIpAddress'], 
                    '** is running')

# If the instance(s) is not in a 'running' state, then print the tag, instance ID, and state name for the instances.          
            else:
                if tag['Key'] == 'Name':
                    print(tag['Value'], '** [ID]:', instance['InstanceId'], 
                    '** is', instance['State']['Name'])    