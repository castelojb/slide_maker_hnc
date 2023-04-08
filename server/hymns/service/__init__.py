from server.hymns.repository.impl.HymnsRepositoryImpl import HymnsRepositoryImpl
from server.hymns.service.HymnService import HymnService

hymn_service = HymnService(HymnsRepositoryImpl())
