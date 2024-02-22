from airflow import DAG
from airflow.operators.dummy import EmptyOperator
from airflow.utils.task_group import TaskGroup
from datetime import datetime, timedelta
import logging
import pendulum
import yaml

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

with DAG(dag_id="PL_USAGE_CLONE_A205384_PL_USAGE_PP01", 
         start_date=datetime(2021,1,1,tzinfo=g_local_tz),
         default_args=default_args, catchup=False, 
         doc_md='docs/clone.md'
) as dag:
    

    # def _build_tasks():

    #     def is_task(f):
    #         return f[-4:-3] == '.'

    #     with dag:
    #         with TaskGroup(group_id=f'EXECUTE') as task_tree:
    #             with open('/usr/local/airflow/dags/A205384_DEP_EAW_DEV3.yml') as f:
    #                 config = yaml.safe_load(f)
    #                 for LEVEL1 in config: # MDM
    #                     with TaskGroup(group_id=LEVEL1) as LEVEL1_tree:
    #                         LEVEL1_TASK_LIST = []
    #                         GROUP1_START_TASK_LIST  = []
    #                         GROUP1_END_TASK_LIST    = []
    #                         for i, LEVEL2 in enumerate(config[LEVEL1]):
    #                             if is_task(LEVEL2):
    #                                 # the dml file is at the LEVEL2 level - create the task
    #                                 LEVEL1_TASK_LIST.append(EmptyOperator(task_id=LEVEL2, dag=dag)) 
    #                                 if i == 0:
    #                                     LEVEL1_TASK_LIST[i]
    #                                 else:
    #                                     LEVEL1_TASK_LIST[i-1] >> LEVEL1_TASK_LIST[i]
 
    #                             else:

    #                                 GROUP1_START_TASK_LIST .append(EmptyOperator(task_id=f'GROUP_{LEVEL2}_START', dag=dag))
    #                                 GROUP1_END_TASK_LIST .append(EmptyOperator(task_id=f'GROUP_{LEVEL2}_END', dag=dag))

    #                                 if i != 0:
    #                                     GROUP1_END_TASK_LIST [i-1] >> GROUP1_START_TASK_LIST [i]

    #                                 LEVEL2_TASK_LIST = []

    #                                 with TaskGroup(group_id=LEVEL2, parent_group=LEVEL1_tree):
    #                                     for j, LEVEL3 in enumerate(config[LEVEL1][LEVEL2]):

    #                                         LEVEL2_TASK_LIST.append(EmptyOperator(task_id=LEVEL3, dag=dag))

    #                                         if j == 0:
    #                                             GROUP1_START_TASK_LIST [i] >> LEVEL2_TASK_LIST[j]
    #                                         else:
    #                                             LEVEL2_TASK_LIST[j-1] >> LEVEL2_TASK_LIST[j]

    #                                     LEVEL2_TASK_LIST[j] >> GROUP1_END_TASK_LIST [i]

        
    #     return task_tree


    def _build_tasks():

        def is_task(f):
            return f[-4:-3] == '.'

        with dag:
            with TaskGroup(group_id=f'EXECUTE') as task_tree:
                with open('/usr/local/airflow/dags/A205384_DEP_EAW_DEV3.yml') as f:
                    config = yaml.safe_load(f)
                    for LEVEL1 in config: # MDM
                        with TaskGroup(group_id=LEVEL1) as LEVEL1_TREE:
                            LEVEL1_TASK_LIST = []
                            GROUP1_START_TASK_LIST  = []
                            GROUP1_END_TASK_LIST    = []
                            GROUP2_START_TASK_LIST  = []
                            GROUP2_END_TASK_LIST    = []
                            for i, LEVEL2 in enumerate(config[LEVEL1]):
                                if is_task(LEVEL2):
                                    # the dml file is at the LEVEL2 level - create the task
                                    LEVEL1_TASK_LIST.append(EmptyOperator(task_id=LEVEL2, dag=dag))
                                    if i == 0:
                                        LEVEL1_TASK_LIST[i]
                                    else:
                                        LEVEL1_TASK_LIST[i-1] >> LEVEL1_TASK_LIST[i]
 
                                else:

                                    GROUP1_START_TASK_LIST.append(EmptyOperator(task_id=f'{LEVEL2}_START', dag=dag))
                                    GROUP1_END_TASK_LIST.append(EmptyOperator(task_id=f'{LEVEL2}_END', dag=dag))

                                    if i != 0:
                                        GROUP1_END_TASK_LIST[i-1] >> GROUP1_START_TASK_LIST[i]

                                    LEVEL2_TASK_LIST = []

                                    with TaskGroup(group_id=LEVEL2, parent_group=LEVEL1_TREE):
                                        max_i = i
                                        for j, LEVEL3 in enumerate(config[LEVEL1][LEVEL2]):

                                            LEVEL2_TASK_LIST.append(EmptyOperator(task_id=LEVEL3, dag=dag))

                                            if j == 0:
                                                LEVEL2_TASK_LIST[j]
                                            else:
                                                LEVEL2_TASK_LIST[j-1] >> LEVEL2_TASK_LIST[j]
                                            
                                        LEVEL2_TASK_LIST[j] >> GROUP1_END_TASK_LIST[max_i] # this joins the group end of the last section to the first

                                            
        
        return task_tree

    # def _read_config():
    #     with open(g_config) as f:
    #         # config = str(yaml.safe_load(f))
    #         config = yaml.safe_load(f)
    #         # config = config.replace("\'", "\"")
    #         # config_json = json.loads(config)
    #         task_logger.info(f'config: {config}')
    #         task_logger.info(f'config type: {type(config)}')
    #         for LEVEL1 in config:
    #             task_logger.info(f'LEVEL1: {LEVEL1}')
    #             task_logger.info(f'branch type: {type(LEVEL1)}')
    #             for LEVEL2 in config[LEVEL1]:
    #                 task_logger.info(f'LEVEL2: {LEVEL2}')
    #                 task_logger.info(f'branch type: {type(LEVEL2)}')
    #                 for LEVEL3 in config[LEVEL1][LEVEL2]:
    #                     if 'Group' in group:
    #                         task_logger.info(f'{group} IS a GROUP')
    #                         for file in config[LEVEL1][LEVEL2][group]:
    #                             task_logger.info(f'CREATE A TASK FOR: {file}')
    #                     else:
    #                         task_logger.info(f'CREATE A TASK FOR: {group}')


# read_config = PythonOperator(task_id='read_config', python_callable=_read_config, dag=dag, provide_context=True)

# read_config
end_dml_execution = EmptyOperator(task_id='end_dml_execution', dag=dag)
start_dml_execution = EmptyOperator(task_id='start_dml_execution', dag=dag)

dml_tasks = _build_tasks()

start_dml_execution >> dml_tasks >> end_dml_execution