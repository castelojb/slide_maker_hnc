from fastapi import HTTPException


class HymnsNotFoundException(HTTPException):

	def __init__(self, hym_requested: str):
		super().__init__(status_code=404, detail=f'The hym {hym_requested} not exists')
