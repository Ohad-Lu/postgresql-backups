from app.api import app

item_json = {
    "id": 3,
    "name": "postgres",
    "type": "string",
    "hostname": "localhost",
    "username": "postgres",
    "password": "postgres",
    "database_name": "postgres",
}
prefix = "/databases"
backup_filename = "file.gz"
app = app
