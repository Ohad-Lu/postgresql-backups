from time import sleep
from os import path, remove
from fastapi.testclient import TestClient
import tests.config as config


class TestLogicDatabase:
    client = TestClient(config.app)
    item_json = config.item_json
    prefix = config.prefix
    backup_filename = config.backup_filename

    def test_backup_db(self):
        self.client.post(f"{self.prefix}/create", json=self.item_json)
        response = self.client.get(f"{self.prefix}/backup/{self.item_json['id']}")

        sleep(11)

        self.client.delete(f"{self.prefix}/delete/{self.item_json['id']}")

        assert response.status_code == 200
        assert path.exists(self.backup_filename) == True

        remove(self.backup_filename)
