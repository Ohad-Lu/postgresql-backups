from pydantic import BaseModel, ConfigDict


class StorageSchema(BaseModel):
    id: int or None
    name: str
    type: str

    s3_endpoint_url: str
    s3_bucket_name: str
    s3_access_key_id: str
    s3_secret_access_key: str

    model_config = ConfigDict(
        from_attributes=True, populate_by_name=True, arbitrary_types_allowed=True
    )
