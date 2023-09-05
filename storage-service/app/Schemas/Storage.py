from pydantic import BaseModel, ConfigDict


class StorageSchema(BaseModel):
    id: int
    name: str
    type: str

    bucket_name: str
    token: str

    model_config = ConfigDict(
        from_attributes=True, populate_by_name=True, arbitrary_types_allowed=True
    )
