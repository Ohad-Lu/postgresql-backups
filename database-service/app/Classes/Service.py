from app.Classes.Repository import Repository
from pydantic import BaseModel


class Service:
    def __init__(self, repository: Repository) -> None:
        self.repository = repository

    def get_by_id(self, id: int):
        return self.repository.get_by_id(id)

    def get_all(self):
        return self.repository.get_all()

    def create(self, item: BaseModel):
        return self.repository.create(item.model_dump())

    def update(self, id: int, item: BaseModel):
        return self.repository.update(id, item.model_dump())

    def delete(self, id: int):
        return self.repository.delete(id)
