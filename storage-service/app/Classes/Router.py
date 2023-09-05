from fastapi import APIRouter, Body
from app.Classes.Service import Service
from pydantic import BaseModel as SchemaBaseModel


class Router:
    def __init__(self, service: Service, schema: SchemaBaseModel, prefix) -> None:
        self.service = service
        self.schema = schema
        self.router = APIRouter(prefix=prefix)
        self.router.add_api_route("/get/{id}", self.get, methods=["GET"])
        self.router.add_api_route("/get_all", self.get_all, methods=["GET"])
        self.router.add_api_route("/create", self.create, methods=["POST"])
        self.router.add_api_route("/update/{id}", self.update, methods=["PATCH"])
        self.router.add_api_route("/delete/{id}", self.delete, methods=["DELETE"])

    def get(self, id: int):
        return self.service.get_by_id(id)

    def get_all(self):
        return self.service.get_all()

    def create(self, item: object = Body(...)):
        item = self.schema(**item)
        return self.service.create(item)

    def update(self, id: int, item: object = Body(...)):
        item = self.schema(**item)
        return self.service.update(id, item)

    def delete(self, id: int):
        return self.service.delete(id)
