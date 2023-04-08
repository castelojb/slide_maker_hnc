from dataclasses import dataclass, asdict
from typing import Optional


@dataclass
class Hymn:
	identifier: str

	title: str

	verses: list[str]

	chorus: Optional[str]

	id: int = 0

	def dict(self):
		return dict(
			id=self.id,
			title=self.title,
			verses=self.verses,
			chorus=self.chorus,
			identifier=self.identifier
		)
