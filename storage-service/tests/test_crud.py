from app.Classes.T_TestCrud import T_TestCrud
from fastapi.testclient import TestClient
import tests.config as config


class TestCrudDatabase(T_TestCrud):
    client = TestClient(config.app)
    item_json = config.item_json
    prefix = config.prefix
