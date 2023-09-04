from app.Database.database_tasks import backup_db_task
from app.Database.DatabaseRepository import DatabaseRepository
from app.Schemas.Database import DatabaseSchema

class DatabaseService:
    def __init__(self, database_repository: DatabaseRepository) -> None:
        self.database_repository = database_repository

    def backup_db(self, db_id: int, dest_filename):
        db = self.database_repository.get_by_id(db_id)
        return backup_db_task.apply_async(args=(db.hostname, db.username, db.database_name, db.password, dest_filename,), countdown=10)

    def get_by_id(self, id: int):
        return self.database_repository.get_by_id(id)

    def get_all(self):
        return self.database_repository.get_all()

    def create(self, database: DatabaseSchema):
        return self.database_repository.create(database.model_dump())

    def update(self, id: int, database: DatabaseSchema):
        return self.database_repository.update(id, database.model_dump())

    def delete(self, id: int):
        return self.database_repository.delete(id)
