import boto3
from datetime import datetime
import json

cloud_watch_logs = boto3.client('logs')

log_groups = cloud_watch_logs.describe_log_groups()
log_group_name = log_groups['logGroups'][0]['logGroupName']
events = cloud_watch_logs.filter_log_events(logGroupName=log_group_name, limit=10)


for evt in events['events']:
    log_stream = evt['logStreamName']
    log_stream_message = evt['message']
    kobj = json.loads(evt['message'])
    #List all the keys in dict
    # keys = kobj.keys()
    # print(keys)
    containerName = kobj['kubernetes']['pod_name']
    timestamp = (datetime.utcfromtimestamp(evt['timestamp']/1000).strftime('%Y-%m-%d %H:%M:%S'))
    print(f" LOG STREAM TIMESTAMP {timestamp}\n LOG STREAM MESSAGE {kobj}\n LOG STREAM CONTAINER NAME {containerName}\n")
    if kobj['kubernetes']['container_name'] == "chat-api":
        print(containerName)
    # else:
        # print(f"THIS CONTAINER {containerName} DOESN'T HAVE THAT KEY")

