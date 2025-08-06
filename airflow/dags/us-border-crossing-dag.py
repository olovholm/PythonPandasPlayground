from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

# Define Python functions for tasks
def task_one():
    print("Task one executed")

def task_two():
    print("Task two executed")

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
        task_id='task_one',
        python_callable=task_one,
    )

    task_2 = PythonOperator(
        task_id='task_two',
        python_callable=task_two,
    )

    task_1 >> task_2  # Define task dependencies
