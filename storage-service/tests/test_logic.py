from fastapi.testclient import TestClient
import tests.config as config


class TestLogicDatabase:
    client = TestClient(config.app)
    item_json = config.item_json
    prefix = config.prefix
