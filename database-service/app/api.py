from fastapi import FastAPI
from app.Database.DatabaseModel import Base
from app.Database.DatabaseConnection import DatabaseConnection
from app.Database.DatabaseRepository import DatabaseRepository
from app.Database.DatabaseService import DatabaseService
from app.Database.DatabaseRouter import DatabaseRouter
from app.Config import config

app = FastAPI()
database_connection = DatabaseConnection(config.database_connection_string, Base)
database_repository = DatabaseRepository(database_connection.session)
database_service = DatabaseService(database_repository)
database_router = DatabaseRouter(database_service)

app.include_router(database_router.router)
