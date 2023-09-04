from sqlalchemy.orm import DeclarativeBase


class Repository:
    def __init__(self, session, base: DeclarativeBase) -> None:
        self.session = session
        self.base = base

    def get_by_id(self, id):
        return self.session.get(self.base, id)

    def get_all(self):
        return self.session.query(self.base).all()

    def create(self, item_json):
        db = self.base(**item_json)
        self.session.add(db)
        self.session.commit()
        self.session.refresh(db)

        return db

    def update(self, id, item_json):
        db = (
            self.session.query(self.base)
            .filter(self.base.id == id)
            .update(item_json, synchronize_session=False)
        )
        self.session.commit()

        return db

    def delete(self, id):
        self.session.delete(self.get_by_id(id))
        self.session.commit()

        return id
