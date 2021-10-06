import requests as r
import os,json 
from kubernetes import client, config
from modules.kubernetes_wrapper import create_or_update_config_map

is_in_cluster = os.getenv("IN_CLUSTER", "0")
print(is_in_cluster)
if is_in_cluster == "1":
    config.load_incluster_config()
    current_namespace = open("/var/run/secrets/kubernetes.io/serviceaccount/namespace").read()
else:
    config.load_kube_config()
    current_namespace = 'python'
coreApi = client.CoreV1Api()

time = r.get("http://worldtimeapi.org/api/timezone/America/Argentina/Salta").text


payload = {'data':time}
print(payload)
(create_or_update_config_map(current_namespace, "worldtime", payload, coreApi))
