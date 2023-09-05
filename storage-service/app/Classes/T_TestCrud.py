from fastapi.testclient import TestClient
from fastapi import FastAPI

app = FastAPI()
item_json = {}
prefix = ""
backup_filename = ""


class T_TestCrud:
    client = TestClient(app)
    item_json = item_json
    prefix = prefix

    def test_create(self):
        response = self.client.post(
            f"{self.prefix}/create",
            json=self.item_json,
        )

        assert response.status_code == 200
        assert response.json() == self.item_json

    def test_get(self):
        response = self.client.get(f"{self.prefix}/get/{self.item_json['id']}")

        assert response.status_code == 200
        assert response.json() == self.item_json

    def test_get_all(self):
        response = self.client.get(f"{self.prefix}/get_all")

        assert response.status_code == 200
        assert response.json() == [self.item_json]

    def test_update(self):
        self.item_json["name"] = "changed_name"
        patch_response = self.client.patch(
            f"{self.prefix}/update/{self.item_json['id']}", json=self.item_json
        )

        assert patch_response.status_code == 200

    def test_delete(self):
        response = self.client.delete(f"{self.prefix}/delete/{self.item_json['id']}")

        assert response.status_code == 200
