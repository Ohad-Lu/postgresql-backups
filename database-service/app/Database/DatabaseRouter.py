from fastapi import APIRouter
from app.Schemas.Database import DatabaseSchema
from app.Database.DatabaseService import DatabaseService


class DatabaseRouter:
    def __init__(self, database_service: DatabaseService) -> None:
        self.database_service = database_service
        self.router = APIRouter(prefix="/databases")
        self.router.add_api_route("/get/{id}", self.get_database, methods=["GET"])
        self.router.add_api_route("/get_all", self.get_all_databases, methods=["GET"])
        self.router.add_api_route("/create", self.create_database, methods=["POST"])
        self.router.add_api_route(
            "/update/{id}", self.update_database, methods=["PATCH"]
        )
        self.router.add_api_route(
            "/delete/{id}", self.delete_database, methods=["DELETE"]
        )
        self.router.add_api_route("/backup/{id}", self.backup, methods=["GET"])

    def get_database(self, id: int):
        return self.database_service.get_by_id(id)

    def get_all_databases(self):
        return self.database_service.get_all()

    def create_database(self, database: DatabaseSchema):
        return self.database_service.create(database)

    def update_database(self, id: int, database: DatabaseSchema):
        return self.database_service.update(id, database)

    def delete_database(self, id: int):
        return self.database_service.delete(id)

    def backup(self, id: int):
        self.database_service.backup_db(id, "file.gz")
        return "okay"
