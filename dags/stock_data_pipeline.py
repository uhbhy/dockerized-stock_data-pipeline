from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from fetch_data import fetch_stock_data, save_stock_data


default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

def fetch_and_save(symbol, **kwargs):
    row = fetch_stock_data(symbol)
    if row:
        save_stock_data(*row)

with DAG(
    dag_id="stock_pipeline",
    default_args=default_args,
    description="Fetch stock data and save to Postgres",
    schedule_interval="@daily",  # runs every day
    start_date=datetime(2025, 8, 22),
    catchup=False,
) as dag:

    fetch_and_save_task = PythonOperator(
        task_id="fetch_and_save_stock",
        python_callable=fetch_and_save,
        op_kwargs={"symbol": "AAPL"},  # you can change this to another stock
        provide_context=True,
    )