import requests

AIRFLOW_URL = "192.168.99.100:30212"
DAG_ID = "Test_Kubernetes_Operator"
docker_image_name = "saivarunr/testpython:test-1"


def initiate_pod(container_name):
    r = requests.get(
        'http://{AIRFLOW_URL}/admin/rest_api/api/trigger_dag?dag_id={DAG_ID}&run_id=vers7&conf={"docker_image_name": "{CONTAINER_NAME}"}'.format(
            AIRFLOW_URL=AIRFLOW_URL,
            CONTAINER_NAME=container_name,
            DAG_ID=DAG_ID
        )
    )


initiate_pod(docker_image_name)
