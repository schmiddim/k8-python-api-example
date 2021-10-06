from kubernetes import client


def read_config_map(namespace: str, config_name: str, v1: client.CoreV1Api):
    """

    :param namespace: str
    :param config_name: str
    :param v1: v1.client.CoreV1Api
    :return: dict || None
    """
    try:
        result: client.models.v1_config_map.V1ConfigMap
        result = v1.read_namespaced_config_map(name=config_name, namespace=namespace)
        print(type(result))
        return result.data
    except client.ApiException as e:
        if e.status == 404:
            return None
        else:
            raise Exception(e)


def create_or_update_config_map(namespace: str, config_name: str, data: dict, v1: client.CoreV1Api):
    """

    :param namespace: str
    :param config_name: str
    :param data: dict
    :param v1: kubernetes.client.CoreV1Api
    :return: dict
    """
    # kubernetes api only accepts strings
    for k in data:
        if type(data.get(k)) is not str:
            raise Exception("{} value is not a string".format(k))

    metadata = client.V1ObjectMeta(
        name=config_name,
        namespace=namespace,
    )

    configmap = client.V1ConfigMap(
        api_version="v1",
        kind="ConfigMap",
        data=data,
        metadata=metadata
    )
    try:
        _ = v1.read_namespaced_config_map(name=config_name, namespace=namespace)

    except client.ApiException as e:

        if e.status == 404:
            print('create config map')
            return v1.create_namespaced_config_map(namespace=namespace, body=configmap)
        else:
            raise Exception(e)
    print('update config map')
    return v1.replace_namespaced_config_map(name=config_name, namespace=namespace, body=configmap)
