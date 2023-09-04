from pydantic import BaseModel, ConfigDict


class DatabaseSchema(BaseModel):
    id: int
    name: str
    type: str
    hostname: str
    username: str
    password: str
    database_name: str

    model_config = ConfigDict(
        from_attributes=True, populate_by_name=True, arbitrary_types_allowed=True
    )
