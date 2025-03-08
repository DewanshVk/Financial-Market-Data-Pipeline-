from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import subprocess

default_args = {
    "owner": "hydra",
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 3,
    "retry_delay": timedelta(minutes=5),
}

def run_producer():
    subprocess.run(["python", "C:/Users/Hydra/Desktop/DE Projects/FinancialMarketPipelineV2/src/producer/producer.py"], check=True)

def check_asa_status():
    # Simple check—can be enhanced with Azure SDK
    print("Checking ASA job status...")

with DAG(
    "finance_pipeline",
    default_args=default_args,
    description="Run financial market pipeline",
    schedule_interval="*/1 * * * *",  # Har minute
    start_date=datetime(2025, 3, 4),
    catchup=False,
) as dag:
    producer_task = PythonOperator(task_id="run_producer", python_callable=run_producer)
    asa_check = PythonOperator(task_id="check_asa_status", python_callable=check_asa_status)
    producer_task >> asa_check