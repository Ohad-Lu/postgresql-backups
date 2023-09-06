from app.Storage.storage_tasks import upload_to_aws
from app.Storage.StorageRepository import StorageRepository
from app.Classes.Service import Service


class StorageService(Service):
    def __init__(self, repository: StorageRepository) -> None:
        super().__init__(repository)

    def upload(self, storage_id, filename):
        storage = self.repository.get_by_id(storage_id)
        upload_to_aws(
            aws_bucket_name=storage.aws_bucket_name,
            aws_access_key_id=storage.aws_access_key_id,
            aws_secret_access_id=storage.aws_secret_access_id,
            filename=filename,
        )

        return "okay"
