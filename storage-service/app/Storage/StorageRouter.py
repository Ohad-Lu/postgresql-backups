from app.Schemas.Storage import StorageSchema
from app.Storage.StorageService import StorageService
from app.Classes.Router import Router

filename = "file.gz"


class StorageRouter(Router):
    def __init__(self, storage_service: StorageService) -> None:
        super().__init__(storage_service, StorageSchema, "/storages")
        self.router.add_api_route(
            "/upload_backup/{dest_storage_id}/{backup_filename}/{dest_filename}",
            self.upload_backup,
            methods=["GET"],
        )

    def upload_backup(self, dest_storage_id: int, backup_filename, dest_filename):
        self.service.upload_backup(dest_storage_id, backup_filename, dest_filename)

        return "okay"
