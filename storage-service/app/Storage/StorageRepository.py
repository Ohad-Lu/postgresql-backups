from app.Classes.Repository import Repository
from app.Storage.StorageModel import Storage


class StorageRepository(Repository):
    def __init__(self, session) -> None:
        super().__init__(session, Storage)
