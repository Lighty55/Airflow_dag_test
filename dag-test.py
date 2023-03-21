from textwrap import dedent
import pendulum
from airflow import DAG
from airflow.operators.python import PythonOperator


with DAG(
    'dag-test',
    default_args={'retries': 0},
    description="test",
    schedule_interval=None,
    start_date=pendulum.datetime(2022, 1, 1, tz="UTC"),
    catchup=False,
    tags=["test"],
) as dag:
    dag.doc_md = __doc__

    def hdfs_example(**kwargs):
        print("Hello World")
        print("Testing Airflow flow")
        print("Dag Test")

    test = PythonOperator(
        task_id='test',
        python_callable=hdfs_example,
    )
    test.doc_md = dedent(
        """ extract task
            extract data
        """
    )
