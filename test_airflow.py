from datetime import datetime as dtime
from airflow import DAG
from airflow.operators.python import PythonOperator
import time
import pendulum
from textwrap import dedent
# from pyspark.sql import SparkSession

def extract_task(**kwargs):
    # context = get_current_context()
    # print (f"context value: {context}")
    # spark =
    custom_param = kwargs['dag_run'].conf.get('custom_parameter')

    if custom_param is not None:
        print(f"Custom Parameter Value is:{custom_param}")
    time.sleep(15)

with DAG(
    "test_config",
    default_args={'retries': 0},
    description="testconfig1",
    schedule_interval=None,
    start_date=pendulum.datetime(2022, 1, 1, tz="UTC"),
    catchup=False,
    tags=["test"],
) as dag:
    dag.doc_md = __doc__

    extract_task = PythonOperator(
        task_id='extract_task',
        python_callable=extract_task,
    )
    extract_task.doc_md = dedent(
        """ extract task
            extract data
        """
    )

    extract_task