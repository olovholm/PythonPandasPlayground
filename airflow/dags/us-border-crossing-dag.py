import sys
sys.path.append('/opt/airflow/src')

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

from us_border_crossings.load_data import load_data
from us_border_crossings.unload_data import unload_data


# Define the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'retries': 1,
}

with DAG(
        dag_id='us-border-crossing-dag',
        default_args=default_args,
        description='Setting up a DAG for US Border Crossing data processing',
        schedule_interval='@daily',
        start_date=datetime(2023, 1, 1),
        catchup=False,
) as dag:
    task_1 = PythonOperator(
        task_id='load_raw_data',
        python_callable=load_data
    )

    task_2 = PythonOperator(
        task_id='unload_data',
        python_callable=unload_data,
    )

    task_1 >> task_2  # Define task dependencies
