from fastapi.testclient import TestClient
import tests.config as config


class TestLogicDatabase:
    client = TestClient(config.app)
    item_json = config.item_json
    prefix = config.prefix

    def test_upload(self):
        self.client.post(f"{self.prefix}/create", json=self.item_json)
        response = self.client.get(
            f"{self.prefix}/upload_backup/{self.item_json['id']}/file.gz/file.gz"
        )
        self.client.delete(f"{self.prefix}/delete/{self.item_json['id']}")

        assert response.status_code == 200
