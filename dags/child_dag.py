import airflow
import logging
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

task_logger = logging.getLogger("airflow.task")
task_logger.setLevel(logging.INFO)

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    "start_date": airflow.utils.dates.days_ago(100),
    'email': ['swilko@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

dag = DAG(
    dag_id='child_dag', 
    default_args=default_args, 
    description='Main Load DAG',
    schedule_interval=None,
    catchup=False,
    max_active_runs=1,
    params={"start_date": "","end_date": ""}
)

def _set_dates_for_backfill(in_start_date, in_end_date, **context):
    # Validate the dates are in the correct format
    task_logger.info(f"In From Date: {in_start_date}")
    task_logger.info(f"In To Date: {in_end_date}")


set_dates_for_backfill = PythonOperator(task_id='set_dates_for_backfill', python_callable=_set_dates_for_backfill, dag=dag, op_kwargs={'in_start_date':"{{ dag_run.conf['start_date'] if dag_run.conf.get('start_date') else '' }}",
                                                                                                'in_end_date':"{{ dag_run.conf['end_date'] if dag_run.conf.get('end_date') else '' }}"}, provide_context=True)

set_dates_for_backfill