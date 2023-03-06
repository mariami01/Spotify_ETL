from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago

from spotify_etl import run_spotify_etl

default_args = {
    "owner": "airflow",
    "depends_on_path": False,
    "start_date": days_ago(2023, 3, 6),
    "email": ["zenaishvilimariam@gmail.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "delay_on_retry": timedelta(minutes=1)
}

dag = DAG(
    "spotify_dag",
    default_args=default_args,
    description="First DAG with ETL process!",
    schedule_interval=timedelta(days=1) # program should run daily
)

def just_a_function():
    print("I'm going to show you something :)")

run_etl = PythonOperator(
    task_id="whole_spotify_etl",
    python_callable=run_spotify_etl,
    dag=dag
)
# order of executions
run_etl