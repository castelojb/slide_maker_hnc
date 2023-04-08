import os

from fastapi import FastAPI
from sqlalchemy import create_engine, MetaData

# For API Usage
app = FastAPI()


def create_conn_str():
	# postgresql://[user[:password]@][netloc][:port][/dbname][?param1=value1&...]
	return f"postgresql://{os.environ.get('DB_USERNAME')}:{os.environ.get('DB_PASSWORD')}@{os.environ.get('DB_HOST')}:{os.environ.get('DB_PORT')}/{os.environ.get('DB_NAME')}"


app_sql_engine = create_engine(create_conn_str(), echo=True)

app_metadata = MetaData()

default_schema_name = os.environ.get('DB_SCHEMAS')
