#!/usr/bin/env python3

# Helpful URL
# https://www.velotio.com/engineering-blog/kubernetes-python-client

from kubernetes import client, config

# Imports local environment
config.load_kube_config()
#or
#cofnig.load_cluster_config()


v1 = client.CoreV1Api()

# # returns a JSON with all the info like spec, metadata etc, for each node
# #print(v1.list_node())

# # Lists all nodes
# v1.list_node()

nodes= [
    'aks-agentpool-20545868-vmss000000',
    'aks-agentpool-20545868-vmss000001',
    'aks-agentpool-20545868-vmss000002',
    'aks-agentpool-20545868-vmss000003',
    'aks-agentpool-20545868-vmss000004'
]

for node in nodes:
    print(
        v1.read_node_status(name=node).status.capacity['memory']
    )
    print(
        v1.read_node_status(name=node).status.allocatable['memory']
    )
    print(
        v1.read_node_status(name=node).status.capacity['pods']
    )
    print(
        v1.read_node_status(name=node).status.allocatable['pods']
    )
    # print(
    #     v1.read_node_status(name=node).status.images['names']
    # )

print(
    v1.read_namespaced_pod_log('rstudio-eda-0b2a6105-7ec9-4daf-879f-4acac9b16f11-569fff898v24f7', 'project-171')
)
# # Lists all namespaces
# v1.list_namespace()


# # List all pods in all namespaces
# v1.list_pod_for_all_namespaces()


# # List all persistent volume claims in all namespaces
# v1.list_persistent_volume_claim_for_all_namespaces()


# # List all pods within a given namespace
# v1.list_namespaced_pod(namespace='gitlab')


# # List all servcies within a given namespace
# v1.list_namespaced_service(namespace='gitlab')


# Creating a resource
# example from linux cli
#   kubectl create deployment my-nginx-depl --image=nginx
#   kubectl apply -f nginx_depl.yaml
# python method
# v1.create_namespaced_pod('<namespace>', <body>)
# v1.create_namespaced_persistent_volume_claim(<namespace>, <body>)


