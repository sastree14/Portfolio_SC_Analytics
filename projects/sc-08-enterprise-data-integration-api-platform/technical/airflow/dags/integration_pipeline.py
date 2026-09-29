from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def extract(): print("extract source records")
def validate(): print("validate schema and row counts")
def load(): print("load curated analytical tables")

with DAG("sc08_integration_pipeline", start_date=datetime(2026,1,1), schedule="@daily", catchup=False) as dag:
    a=PythonOperator(task_id="extract", python_callable=extract)
    b=PythonOperator(task_id="validate", python_callable=validate)
    c=PythonOperator(task_id="load", python_callable=load)
    a >> b >> c
