import boto3
import schedule

ec2_client = boto3.client('ec2')
ec2_resource = boto3.resource('ec2')


reservations = ec2_client.describe_instances()
for reservation in reservations["Reservations"]:
    instances = reservation["Instances"]
    for instance in instances:
        print(f"Instance {instance['InstanceId']} is \
              {instance['State']['Name']}")


def check_instance_status():
    statuses = ec2_client.describe_instance_status(
        IncludeAllInstances=True
    )
    for status in statuses['InstanceStatuses']:
        in_status = status['InstanceStatus']['Status']
        sys_status = status['SystemStatus']['Status']
        print(f"Instance {status['InstanceId']} status is {in_status} and system status is {sys_status}")
        print('########################\n')
        if sys_status == "ok":
            print(f"now we can run anisble")


schedule.every(10).seconds.do(check_instance_status)

while True:
    schedule.run_pending()


all_available_vpcs = ec2_client.describe_vpcs()
vpcs = all_available_vpcs["Vpcs"]


for vpc in vpcs:
    print(vpc["VpcId"])
    print(vpc["OwnerId"])
    cidr_block_assoc_sets = vpc["CidrBlockAssociationSet"]
    for assoc_sets in cidr_block_assoc_sets:
        print(assoc_sets["CidrBlockState"])
