from time import sleep
from os import path, remove
from app.api import app
from fastapi.testclient import TestClient

client = TestClient(app)
db_json = {
    "id": 3,
    "name": "postgres",
    "type": "string",
    "hostname": "localhost",
    "username": "postgres",
    "password": "postgres",
    "database_name": "postgres",
}


def test_create_db():
    response = client.post(
        "/databases/create",
        json=db_json,
    )

    assert response.status_code == 200
    assert response.json() == db_json


def test_get_db():
    response = client.get(f"/databases/get/{db_json['id']}")

    assert response.status_code == 200
    assert response.json() == db_json


def test_get_all_dbs():
    response = client.get("/databases/get_all")

    assert response.status_code == 200
    assert response.json() == [db_json]


def test_update_db():
    db_json["name"] = "changed_name"
    patch_response = client.patch(f"/databases/update/{db_json['id']}", json=db_json)

    assert patch_response.status_code == 200


def test_backup_db():
    response = client.get(f"/databases/backup/{db_json['id']}")
    sleep(11)

    assert response.status_code == 200
    assert path.exists("file.gz") == True

    remove("file.gz")


def test_delete_db():
    response = client.delete(f"/databases/delete/{db_json['id']}")

    assert response.status_code == 200
