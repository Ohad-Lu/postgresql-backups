from __future__ import annotations
from typing import Any
from sqlalchemy import String, orm
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
import boto3
import logging
from sqlalchemy.ext.hybrid import hybrid_property


class Base(DeclarativeBase):
    pass


class Storage(Base):
    __tablename__ = "storages"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    type: Mapped[str] = mapped_column(String(30))

    s3_endpoint_url: Mapped[str] = mapped_column(String(50))
    s3_bucket_name: Mapped[str] = mapped_column(String(30))
    s3_access_key_id: Mapped[str] = mapped_column(String(50))
    s3_secret_access_key: Mapped[str] = mapped_column(String(50))

    # def __init__(
    #     self,
    #     name,
    #     type,
    #     s3_endpoint_url,
    #     s3_bucket_name,
    #     s3_access_key_id,
    #     s3_secret_access_key,
    #     id=None,
    # ):
    #     if id:
    #         self.id = id
    #     self.name = name
    #     self.type = type
    #     self.s3_endpoint_url = s3_endpoint_url
    #     self.s3_bucket_name = s3_bucket_name
    #     self.s3_access_key_id = s3_access_key_id
    #     self.s3_secret_access_key = s3_secret_access_key

    @hybrid_property
    def client(self):
        return boto3.client(
            "s3",
            endpoint_url=self.s3_endpoint_url,
            aws_access_key_id=self.s3_access_key_id,
            aws_secret_access_key=self.s3_secret_access_key,
            verify=False,
        )

    @classmethod
    def download(self, src_file, dst_file):
        logging.error(f"{type(self.s3_bucket_name(self))}")
        # self.client.download_file(self.s3_bucket_name.value, src_file, dst_file)
        return dst_file

    @classmethod
    def upload(self, src_file, dst_file):
        # self.client.upload_file(src_file, self.s3_bucket_name, dst_file)
        return f"{self.s3_bucket_name}/{dst_file}"

    @classmethod
    def copy(self, src_file, dst_bucket: Storage, dst_file):
        logging.error(print(f"=========={self.s3_endpoint_url}========"))
        return dst_bucket.upload(self.download(src_file, src_file), dst_file)
