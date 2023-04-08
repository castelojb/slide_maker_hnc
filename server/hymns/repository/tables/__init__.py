from sqlalchemy import Table, Column, Integer, String, JSON

from setup import app_metadata, default_schema_name

hymns_table_name = 'hymns'

hymns_table = Table(
	hymns_table_name,
	app_metadata,
	Column("id", Integer, primary_key=True, autoincrement=True),
	Column("identifier", String),
	Column("title", String),
	Column("verses", JSON),
	Column("chorus", String),
	schema=default_schema_name
)
