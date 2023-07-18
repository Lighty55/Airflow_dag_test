from airflow import DAG

from airflow_notebook.pipeline import NotebookOp
from airflow.utils.dates import days_ago

# Setup default args with older date to automatically trigger when uploaded
args = {
    "project_id": "test-0718054713",
}

dag = DAG(
    "test-0718054713",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="Created with Elyra 2.2.4 pipeline editor using test.pipeline.",
    is_paused_upon_creation=False,
)


notebook_op_9138ece0_a7f5_437e_8487_90b40e991d1b = NotebookOp(
    name="build_push_image",
    namespace="ml-workshop",
    task_id="build_push_image",
    notebook="Machine-Learning-on-Kubernetes/Chapter07/model_deploy_pipeline/model_build_push/build_push_image.py",
    cos_endpoint="http://minio-ml-workshop:9000",
    cos_bucket="airflow",
    cos_directory="test-0718054713",
    cos_dependencies_archive="build_push_image-9138ece0-a7f5-437e-8487-90b40e991d1b.tar.gz",
    pipeline_outputs=[],
    pipeline_inputs=[],
    image="quay.io/ml-on-k8s/kaniko-container-builder:1.0.0",
    in_cluster=True,
    env_vars={
        "AWS_ACCESS_KEY_ID": "minio",
        "AWS_SECRET_ACCESS_KEY": "minio123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "MODEL_NAME": "mlflowdemo",
        "MODEL_VERSION": "1",
        "CONTAINER_REGISTRY": "https://index.docker.io/v1/",
        "CONTAINER_REGISTRY_USER": "lighty55",
        "CONTAINER_REGISTRY_PASSWORD": "spoody51299",
        "CONTAINER_DETAILS": "lighty55/mlflowdemo:1.1.1",
    },
    config_file="None",
    dag=dag,
)

notebook_op_9138ece0_a7f5_437e_8487_90b40e991d1b.image_pull_policy = "IfNotPresent"


notebook_op_676c51bd_4fd6_427a_a604_c41715bf69d3 = NotebookOp(
    name="deploy_model",
    namespace="ml-workshop",
    task_id="deploy_model",
    notebook="Machine-Learning-on-Kubernetes/Chapter07/model_deploy_pipeline/model_deploy/deploy_model.py",
    cos_endpoint="http://minio-ml-workshop:9000",
    cos_bucket="airflow",
    cos_directory="test-0718054713",
    cos_dependencies_archive="deploy_model-676c51bd-4fd6-427a-a604-c41715bf69d3.tar.gz",
    pipeline_outputs=[],
    pipeline_inputs=[],
    image="quay.io/ml-on-k8s/airflow-python-runner:0.0.11",
    in_cluster=True,
    env_vars={
        "AWS_ACCESS_KEY_ID": "minio",
        "AWS_SECRET_ACCESS_KEY": "minio123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "MODEL_NAME": "mlflowdemo",
        "MODEL_VERSION": "1",
        "CONTAINER_DETAILS": "lighty55/mlflowdemo:1.1.1",
    },
    config_file="None",
    dag=dag,
)

notebook_op_676c51bd_4fd6_427a_a604_c41715bf69d3.image_pull_policy = "IfNotPresent"

(
    notebook_op_676c51bd_4fd6_427a_a604_c41715bf69d3
    << notebook_op_9138ece0_a7f5_437e_8487_90b40e991d1b
)
