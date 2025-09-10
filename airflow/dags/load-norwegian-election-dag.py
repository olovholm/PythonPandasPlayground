import sys
sys.path.append('/opt/airflow/src')

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime


from norwegian_election import load_election_data


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'retries': 1,
}

with DAG(
        dag_id='load-norwegian-election-dag',
        default_args=default_args,
        description='Setting up a DAG for Norwegian Election data processing',
        schedule_interval='@yearly',
        start_date=datetime(2025, 9, 8),
        catchup=False,
) as dag:
    task_1 = PythonOperator(
        task_id='load_election_data',
        python_callable=load_election_data
    )
