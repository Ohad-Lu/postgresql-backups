from sqlalchemy import create_engine
from sqlalchemy.orm import Session, DeclarativeBase


class DatabaseConnection:
    def __init__(self, connection_string, base: DeclarativeBase) -> None:
        engine = create_engine(connection_string)
        base.metadata.create_all(engine)
        self.session = Session(engine)
