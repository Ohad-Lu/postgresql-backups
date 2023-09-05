from app.Schemas.Storage import StorageSchema
from app.Storage.StorageService import StorageService
from app.Classes.Router import Router


class StorageRouter(Router):
    def __init__(self, storage_service: StorageService) -> None:
        super().__init__(storage_service, StorageSchema, "/storages")
