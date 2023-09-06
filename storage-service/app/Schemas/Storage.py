from pydantic import BaseModel, ConfigDict


class StorageSchema(BaseModel):
    id: int
    name: str
    type: str

    aws_bucket_name: str
    aws_access_key_id: str
    aws_secret_access_id: str

    model_config = ConfigDict(
        from_attributes=True, populate_by_name=True, arbitrary_types_allowed=True
    )
