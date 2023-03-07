import boto3

ec2_client = boto3.client('ec2')
ec2_resource = boto3.resource('ec2')


instance_id = []

reservations = ec2_client.describe_instances()['Reservations']
for res in reservations:
    instances = res['Instances']
    for ins in instances:
        instance_id.append(ins['Instance_id'])

response = ec2_resource.create_tags(
    Resources=instance_id,
    Tags=[
        {
            'Key': 'environment',
            'Value': 'us-east-1'
        },
    ]
)
