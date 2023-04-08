from typing import Optional

from sqlalchemy import select
from sqlalchemy.orm import Session

from server.hymns.models.Hymn import Hymn
from server.hymns.repository.api.HymnsRepository import HymnsRepository
from server.hymns.repository.tables import hymns_table
from setup import app_sql_engine


class HymnsRepositoryImpl(HymnsRepository):
	@staticmethod
	def get_by_id(id_: int) -> Optional[Hymn]:
		query = select(hymns_table).where(
			hymns_table.c.id == id_
		)

		with Session(app_sql_engine) as session:
			db_row = session.execute(query).one_or_none()

		if db_row is None:
			return None

		out = Hymn(**db_row)

		return out

	@staticmethod
	def get_by_identifier(identifier: str) -> Hymn:

		query = select(hymns_table).where(
			hymns_table.c.identifier == identifier
		)

		with Session(app_sql_engine) as session:
			db_row = session.execute(query).one_or_none()

		if db_row is None:
			return None

		out = Hymn(**db_row)

		return out

	@staticmethod
	def list_identifiers() -> list[str]:
		query = select([hymns_table.c.identifier.label('identifier')])

		with Session(app_sql_engine) as session:
			db_rows = session.execute(query).all()

		identifier_list = [
			row.identifier for row in db_rows
		]

		return identifier_list

	@staticmethod
	def get_all() -> list[Hymn]:
		query = select(hymns_table)

		with Session(app_sql_engine) as session:
			db_rows = session.execute(query).all()

		hymns = [
			Hymn(**row) for row in db_rows
		]

		return hymns
