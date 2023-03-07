import boto3


client = boto3.client('eks')
clusters = client.list_clusters()['clusters']

for cluster in clusters:
    response = client.describe_cluster(
        name=cluster
    )
    cluster_info = response['cluster']
    cluster_status = cluster_info['status']
    cluster_endpoint = cluster_info['endpoint']
    cluster_version = cluster_info['version']
    cluster_arn = cluster_info['arn']

    print(f"Sky-hop's cluster {cluster} {cluster_arn} status is currently {cluster_status}\n")
    print(f"{clusters} endpoint {cluster_endpoint}\n")
    print(f"{clusters} version {cluster_version}\n")
