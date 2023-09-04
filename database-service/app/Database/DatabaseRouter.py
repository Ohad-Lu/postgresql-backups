from fastapi import APIRouter
from app.Schemas.Database import DatabaseSchema
from app.Database.DatabaseService import DatabaseService
from app.Classes.Router import Router


class DatabaseRouter(Router):
    def __init__(self, database_service: DatabaseService) -> None:
        super().__init__(database_service, DatabaseSchema, "/databases")
        self.router.add_api_route("/backup/{id}", self.backup, methods=["GET"])

    def backup(self, id: int):
        self.service.backup_db(id, "file.gz")
        return "okay"
