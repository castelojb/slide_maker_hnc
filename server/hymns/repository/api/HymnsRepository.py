from abc import ABC, abstractmethod
from typing import Optional

from server.hymns.models.Hymn import Hymn


class HymnsRepository(ABC):

	@staticmethod
	@abstractmethod
	def get_by_id(id_: int) -> Optional[Hymn]:
		pass

	@staticmethod
	@abstractmethod
	def get_by_identifier(identifier: str) -> Optional[Hymn]:
		pass

	@staticmethod
	@abstractmethod
	def list_identifiers() -> list[str]:
		pass

	@staticmethod
	@abstractmethod
	def get_all() -> list[Hymn]:
		pass
