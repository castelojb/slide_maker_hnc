from fastapi import APIRouter
from fastapi_pagination import Page, paginate

from server.hymns.models.Hymn import Hymn
from server.hymns.service import hymn_service

base_service = hymn_service

hymn_router = APIRouter(
	prefix='/hymn'
)


@hymn_router.get(
	'/{id_}'
)
async def get_by_id(id_: int) -> Hymn:
	return base_service.get_by_id(id_)


@hymn_router.get(
	'/identifier/{identifier}'
)
async def get_by_identifier(identifier: str) -> Hymn:
	return base_service.get_by_identifier(identifier)


@hymn_router.get(
	'list-identifiers'
)
async def list_identifiers() -> list[str]:
	return base_service.list_identifiers()


@hymn_router.get(
	'list-all'
)
async def get_all() -> list[Hymn]:
	response = base_service.get_all()
	return response
