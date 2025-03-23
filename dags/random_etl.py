from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.dummy import DummyOperator
from datetime import datetime, timedelta
from data_ingestion import data_ingestion
from data_transform import data_transform
from data_load import data_load

# Default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Initialize the DAG
dag = DAG(
    'random_user_data',
    default_args=default_args,
    description='ETL pipeline for random names API to PostgreSQL',
    schedule_interval=timedelta(minutes=1),
    start_date=datetime(2025, 3, 23),
    catchup=False
)

# Define tasks
start = DummyOperator(
    task_id='start',
    dag=dag,
)

extract_task = PythonOperator(
    task_id='extract_from_api',
    python_callable=data_ingestion,
    provide_context=True,
    dag=dag,
)

transform_task = PythonOperator(
    task_id='transform_data',
    python_callable=data_transform,
    provide_context=True,
    dag=dag,
)

load_task = PythonOperator(
    task_id='load_to_postgres',
    python_callable=data_load,
    provide_context=True,
    dag=dag,
)

end = DummyOperator(
    task_id='end',
    dag=dag,
)

# Set task dependencies
start >> extract_task >> transform_task >> load_task >> end