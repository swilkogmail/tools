from airflow import DAG
from airflow.models import Variable
from airflow.models.param import Param
from airflow.operators.empty import EmptyOperator
from airflow.operators.python_operator import PythonOperator, BranchPythonOperator
from airflow.operators.trigger_dagrun import TriggerDagRunOperator
from airflow.sensors.sql_sensor import SqlSensor
from airflow.decorators import dag, task
from datetime import datetime, timedelta, date
import logging
import pendulum

blue = '#6FA8DC'
green = '#93C47D'
purple = '#B4A7D6'
yellow = '#FFD966'
BranchPythonOperator.ui_color = green
EmptyOperator.ui_color = purple
PythonOperator.ui_color = yellow
SqlSensor.ui_color = blue

task_logger = logging.getLogger("airflow.task")
task_logger.setLevel(logging.INFO)
g_local_tz = pendulum.timezone('Europe/London')

default_args = {
    "owner" : "airflow",
    "email_on_failure" : False,
    "email_on_retry" : False,
    "email" : "stephen.wilkins@thomsonreuters.com",
    "retries": 1,
    "retry_delay": timedelta(minutes=1)
}

# ________                           ______ __________                           
# ___  __ )____________ ________________  /____  ____/___  ______________________
# __  __  |_  ___/  __ `/_  __ \  ___/_  __ \_  /_   _  / / /_  __ \  ___/_  ___/
# _  /_/ /_  /   / /_/ /_  / / / /__ _  / / /  __/   / /_/ /_  / / / /__ _(__  ) 
# /_____/ /_/    \__,_/ /_/ /_/\___/ /_/ /_//_/      \__,_/ /_/ /_/\___/ /____/  
                                                                              

with DAG(dag_id=f"multirun", 
         start_date=datetime(2021,1,1,tzinfo=g_local_tz), 
         schedule_interval=None, 
         default_args=default_args,
         catchup=False,
         max_active_runs=1,
         default_view='graph',
         tags='pl_usage eaw dataload'.split(),
         params={"start_date": Param(
                    f"{date.today()}",  
                    type="string",
                    format="date",
                    title="Start Date",
                    description="The date of the first DAG Run."),
                "end_date": Param(
                    f"{date.today()}",  
                    type="string",
                    format="date",
                    title="End Date",
                    description="The Date of the last DAG run.")
                }
) as dag:


    def _build_dag_list(context):
        from datetime import datetime
        param_dict = context["task_instance"].xcom_pull(task_ids='set_dag_params', key="param_dict")
        start_date = param_dict['start_date']
        end_date = param_dict['end_date']

        date_format = '%Y-%m-%d'
        delta = timedelta(days=1)
        start_py_date = datetime.strptime(start_date, date_format)
        end_py_date = datetime.strptime(end_date, date_format)

        task_list = []

        while (start_py_date < end_py_date):
            start_py_date += delta
            task_date = start_py_date.strftime(date_format).upper()

            # task_logger.info(f"Task Date is {task_date}")

            # task_list.append(EmptyOperator(task_id=f'end_dynamic_tasks_{start_date}'))

            task_list.append(TriggerDagRunOperator(task_id=f'launch_dag_{task_date}', 
                                            trigger_dag_id='example_dag_basic',
                                                    execution_date=task_date, 
                                                    reset_dag_run=False, 
                                                    wait_for_completion=False, 
                                                    poke_interval=60))

        return task_list

    def _dag_params(**context) -> None:
        from airflow.exceptions import AirflowSkipException
        from airflow.models.dagrun import DagRun
        from airflow.models.taskinstance import TaskInstance
        import json

        ti: TaskInstance = context["ti"]
        dag_run: DagRun = ti.dag_run
        if not dag_run.conf:
            task_logger.info("No parameters supplied as DagRun.conf, was the trigger w/o form?")
            raise AirflowSkipException("No DagRun.conf parameters supplied.")
        task_logger.info(f"This DAG was triggered with the following parameters:\n{json.dumps(dag_run.conf, indent=4)}")
        param_dict = dag_run.conf
        context["ti"].xcom_push(key='param_dict', value=param_dict)

        dag_list = _build_dag_list(context)

        task_logger.info(f"{dag_list}")

        dag_list

    
    set_dag_params = PythonOperator(task_id='set_dag_params', python_callable=_dag_params, provide_context=True)
    
    # build_dag_list = PythonOperator(task_id='build_dag_list', python_callable=_build_dag_list, provide_context=True)

    set_dag_params
# ________             ______         
# ___  __/_____ __________  /_________
# __  /  _  __ `/_  ___/_  //_/_  ___/
# _  /   / /_/ /_(__  )_  ,<  _(__  ) 
# /_/    \__,_/ /____/ /_/|_| /____/  



# ________             ______ _______________                
# ___  __/_____ __________  /____  ____/__  /________      __
# __  /  _  __ `/_  ___/_  //_/_  /_   __  /_  __ \_ | /| / /
# _  /   / /_/ /_(__  )_  ,<  _  __/   _  / / /_/ /_ |/ |/ / 
# /_/    \__,_/ /____/ /_/|_| /_/      /_/  \____/____/|__/  