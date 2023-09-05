from app.Storage.storage_tasks import task
from app.Storage.StorageRepository import StorageRepository
from app.Classes.Service import Service


class StorageService(Service):
    def __init__(self, repository: StorageRepository) -> None:
        super().__init__(repository)
