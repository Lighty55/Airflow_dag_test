from airflow import DAG

from airflow_notebook.pipeline import NotebookOp
from airflow.utils.dates import days_ago

# Setup default args with older date to automatically trigger when uploaded
args = {
    "project_id": "build_push_image-0509064153",
}

dag = DAG(
    "build_push_image-0509064153",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="Created with Elyra 2.2.4 pipeline editor using build_push_image.pipeline.",
    is_paused_upon_creation=False,
)


notebook_op_94602623_af1a_4129_b313_22e1d5035907 = NotebookOp(
    name="Machine_Learning_on_Kubernetes_Chapter07_model_deploy_pipeline_model_build_push_build_push_image.py",
    namespace="ml-workshop",
    task_id="Machine_Learning_on_Kubernetes_Chapter07_model_deploy_pipeline_model_build_push_build_push_image.py",
    notebook="Machine-Learning-on-Kubernetes/Chapter07/model_deploy_pipeline/model_build_push/build_push_image.py",
    cos_endpoint="http://minio-ml-workshop:9000",
    cos_bucket="airflow",
    cos_directory="build_push_image-0509064153",
    cos_dependencies_archive="build_push_image-94602623-af1a-4129-b313-22e1d5035907.tar.gz",
    pipeline_outputs=[],
    pipeline_inputs=[],
    image="quay.io/ml-on-k8s/kaniko-container-builder:1.0.0",
    in_cluster=True,
    env_vars={
        "AWS_ACCESS_KEY_ID": "minio",
        "AWS_SECRET_ACCESS_KEY": "minio123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
    },
    config_file="None",
    dag=dag,
)

notebook_op_94602623_af1a_4129_b313_22e1d5035907.image_pull_policy = "IfNotPresent"
