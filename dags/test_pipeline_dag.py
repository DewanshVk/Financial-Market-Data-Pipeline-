from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator


# Sample function to print something
def sample_task():
    print("✅ DAG is running successfully!")


# Default DAG arguments
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}


# DAG Definition
with DAG(
    dag_id='test_pipeline_dag',
    default_args=default_args,
    description='A simple test DAG to check Airflow setup',
    schedule_interval=timedelta(days=1),  # Runs daily
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=['test'],
) as dag:

    task1 = PythonOperator(
        task_id='print_hello',
        python_callable=sample_task,
    )

    task1
