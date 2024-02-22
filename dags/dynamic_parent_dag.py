import airflow
import logging
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
PythonOperator.ui_color = '#0000FF'
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.trigger_dagrun import TriggerDagRunOperator
from airflow.models import Variable

task_logger = logging.getLogger("airflow.task")
task_logger.setLevel(logging.INFO)

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    "start_date": airflow.utils.dates.days_ago(1),
    'email': ['swilko@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

dag = DAG(
    dag_id='dynamic_parent_dag', 
    default_args=default_args, 
    description='Main Load DAG',
    schedule_interval=None,
    catchup=False,
    max_active_runs=1,
    params={"start_date": "","end_date": ""}
)

def _set_dates_for_backfill(in_start_date, in_end_date, **context):
    in_format = '%d-%b-%y'
    out_format = '%Y-%m-%d'
    # Validate the dates are in the correct format
    task_logger.info(f"In From Date: {in_start_date}")
    task_logger.info(f"In To Date: {in_end_date}")

    from_date = datetime.strptime(in_start_date, in_format)
    to_date = datetime.strptime(in_end_date, in_format)

    # Set the correct date for the backfill
    out_start_date = from_date.strftime(out_format)
    out_end_date = to_date.strftime(out_format)
    task_logger.info(f"Out From Date: {out_start_date}")
    task_logger.info(f"Out To Date: {out_end_date}")

    # Push to xcom
    context["task_instance"].xcom_push(key="start_date_in", value=in_start_date)
    context["task_instance"].xcom_push(key="end_date_in", value=in_end_date)
    context["task_instance"].xcom_push(key="start_date", value=out_start_date)
    context["task_instance"].xcom_push(key="end_date", value=out_end_date)
    Variable.set('start_date', in_start_date)
    Variable.set('end_date', in_end_date)

    return out_start_date, out_end_date

# def _run_dag_for_dates(**context):
#     start_date = context["task_instance"].xcom_pull(task_ids='set_dates_for_backfill',key="start_date_in")
#     end_date = context["task_instance"].xcom_pull(task_ids='set_dates_for_backfill',key="end_date_in")
#     date_format = '%d-%b-%y'
#     start_py_date = datetime.strptime(start_date, date_format)
#     end_py_date = datetime.strptime(end_date, date_format)
#     delta = timedelta(days=1)
#     task_logger.info(f"Py Start Date: {start_py_date}")
#     task_logger.info(f"Py End Date: {end_py_date}")

#     task_list = []

#     while (start_py_date < end_py_date):
#         start_py_date += delta
#         task_date = start_py_date.strftime(date_format).upper()

#         task_logger.info(f"Running DAG for: {start_py_date}")
#         task_logger.info(f"Task Date: {task_date}")
#         task_list.append(TriggerDagRunOperator(task_id=f'child_task_{task_date}', trigger_dag_id='child_dag',
#                                                conf={"start_date":"{{ task_instance.xcom_pull(task_ids='set_dates_for_backfill', key='start_date') }}", "end_date":"{{ task_instance.xcom_pull(task_ids='set_dates_for_backfill', key='end_date') }}"},
#                                                execution_date='{{ ds }}', reset_dag_run=True, wait_for_completion=True, poke_interval=60, dag=dag))

#     return task_list

def _run_dag_for_dates():
    start_date = Variable.get('start_date', default_var="30-DEC-74")
    end_date = Variable.get('end_date', default_var="31-DEC-74")
    date_format = '%d-%b-%y'
    start_py_date = datetime.strptime(start_date, date_format)
    end_py_date = datetime.strptime(end_date, date_format)
    delta = timedelta(days=1)
    task_logger.info(f"Py Start Date: {start_py_date}")
    task_logger.info(f"Py End Date: {end_py_date}")

    task_list = []

    start_dynamic_tasks = DummyOperator(task_id='start_dynamic_tasks', dag=dag)
    task_list.append(start_dynamic_tasks)

    while (start_py_date < end_py_date):
        start_py_date += delta
        task_date = start_py_date.strftime(date_format).upper()

        task_logger.info(f"Running DAG for: {start_py_date}")
        task_logger.info(f"Task Date: {task_date}")
        task_list.append(TriggerDagRunOperator(task_id=f'child_task_{task_date}', trigger_dag_id='child_dag',
                                               conf={"start_date": f'"{start_date}"', "end_date":f'"{end_date}"'},
                                               execution_date='{{ ds }}', reset_dag_run=False, wait_for_completion=False, poke_interval=60, dag=dag))

    end_dynamic_tasks = DummyOperator(task_id='end_dynamic_tasks', dag=dag)
    task_list.append(end_dynamic_tasks)

    return task_list

set_dates_for_backfill = PythonOperator(task_id='set_dates_for_backfill', python_callable=_set_dates_for_backfill, dag=dag, op_kwargs={'in_start_date':"{{ dag_run.conf['start_date'] if dag_run.conf.get('start_date') else '' }}",
                                                                                                'in_end_date':"{{ dag_run.conf['end_date'] if dag_run.conf.get('end_date') else '' }}"}, provide_context=True)

# run_dag_for_dates = PythonOperator(task_id='run_dag_for_dates', python_callable=_run_dag_for_dates, dag=dag, op_kwargs={'in_start_date':"{{ dag_run.conf['start_date'] if dag_run.conf.get('start_date') else '' }}",
#                                                                                                 'in_end_date':"{{ dag_run.conf['end_date'] if dag_run.conf.get('end_date') else '' }}"}, provide_context=True)

child_task_list = _run_dag_for_dates()

set_dates_for_backfill >> child_task_list