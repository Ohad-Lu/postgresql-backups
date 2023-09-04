from app.Database.DatabaseModel import Database
from app.Abstract.AbstractRepository import AbstractRepository


class DatabaseRepository(AbstractRepository):
    def __init__(self, session) -> None:
        self.session = session

    def get_by_id(self, id):
        return self.session.get(Database, id)

    def get_all(self):
        return self.session.query(Database).all()

    def create(self, database_json):
        db = Database(**database_json)
        self.session.add(db)
        self.session.commit()
        self.session.refresh(db)

        return db

    def update(self, id, database_json):
        db = (
            self.session.query(Database)
            .filter(Database.id == id)
            .update(database_json, synchronize_session=False)
        )
        self.session.commit()

        return db

    def delete(self, id):
        self.session.delete(self.get_by_id(id))
        self.session.commit()

        return id
