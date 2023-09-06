from app.Schemas.Storage import StorageSchema
from app.Storage.StorageService import StorageService
from app.Classes.Router import Router

filename = "file.gz"


class StorageRouter(Router):
    def __init__(self, storage_service: StorageService) -> None:
        super().__init__(storage_service, StorageSchema, "/storages")
        self.router.add_api_route("/upload/{storage_id}", self.upload, methods=["GET"])

    def upload(self, storage_id: int):
        self.service.upload(storage_id, filename)

        return "okay"
