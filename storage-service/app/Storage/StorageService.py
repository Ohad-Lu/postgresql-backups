from app.Storage.storage_tasks import upload_to_aws
from app.Storage.StorageRepository import StorageRepository
from app.Classes.Service import Service
from app.Config import config


class StorageService(Service):
    def __init__(self, repository: StorageRepository) -> None:
        super().__init__(repository)

    def upload_backup(self, dest_storage_id, backup_filename, dest_filename):
        dest_storage = self.repository.get_by_id(dest_storage_id)
        config.backups_bucket.copy(backup_filename, dest_storage, dest_filename)

        return "okay"
