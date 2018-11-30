from airflow import DAG
from datetime import datetime, timedelta

from operators.KubernetesPodOperator import XKubernetesPodOperator

current_date = datetime.utcnow()

default_args = {
    'owner': 'root',
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

with  DAG(
        dag_id='Test_Kubernetes_Operator',
        default_args=default_args,
        start_date=current_date,
        concurrency=1,
        schedule_interval=None
) as d:
    XKubernetesPodOperator(namespace='default',
                           image="hello-world",
                           name="test",
                           task_id="task",
                           startup_timeout_seconds=600,
                           in_cluster=True,
                           is_delete_operator_pod=True
                           )
