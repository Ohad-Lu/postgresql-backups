from app.Database.database_tasks import backup_db_task, upload_to_aws_task
from app.Database.DatabaseRepository import DatabaseRepository
from app.Classes.Service import Service
from app.Config import config


class DatabaseService(Service):
    def __init__(self, repository: DatabaseRepository) -> None:
        super().__init__(repository)

    def backup_db(self, db_id: int, dest_filename):
        db = self.repository.get_by_id(db_id)
        backup_db_task.apply_async(
            args=(
                db.hostname,
                db.username,
                db.database_name,
                db.password,
                dest_filename,
            ),
            countdown=10,
        )
