from fastapi import FastAPI
from app.Storage.StorageModel import Base
from app.Classes.DatabaseConnection import DatabaseConnection
from app.Storage.StorageRepository import StorageRepository
from app.Storage.StorageService import StorageService
from app.Storage.StorageRouter import StorageRouter
from app.Config import config

app = FastAPI()
database_connection = DatabaseConnection(config.database_connection_string, Base)
storage_repository = StorageRepository(database_connection.session)
storage_service = StorageService(storage_repository)
storage_router = StorageRouter(storage_service)

app.include_router(storage_router.router)
