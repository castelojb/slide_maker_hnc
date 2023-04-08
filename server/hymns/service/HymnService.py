from server.hymns.exceptions.HymnsNotFoundException import HymnsNotFoundException
from server.hymns.models.Hymn import Hymn
from server.hymns.repository.api.HymnsRepository import HymnsRepository


class HymnService:

	def __init__(self, hymns_repository: HymnsRepository):
		self.hymns_repository = hymns_repository

	def get_by_id(self, id_: int) -> Hymn:
		hym = self.hymns_repository.get_by_id(id_)

		if hym is None:
			raise HymnsNotFoundException(str(id_))

		return hym

	def get_by_identifier(self, identifier: str) -> Hymn:
		hym = self.hymns_repository.get_by_identifier(identifier)

		if hym is None:
			raise HymnsNotFoundException(identifier)

		return hym

	def list_identifiers(self) -> list[str]:
		return self.hymns_repository.list_identifiers()

	def get_all(self) -> list[Hymn]:
		return self.hymns_repository.get_all()
