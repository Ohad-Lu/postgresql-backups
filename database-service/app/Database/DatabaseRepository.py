from app.Classes.Repository import Repository
from app.Database.DatabaseModel import Database


class DatabaseRepository(Repository):
    def __init__(self, session) -> None:
        super().__init__(session, Database)
