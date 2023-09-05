
# Storage service
## micro-service to manage the diffrent target storages
### [Documantation](http://localhost:5000/docs)
### Structure: api -> router -> service -> repository -> model
### How to run  
* Create python virtual environment 
```
venv venv # or python -m venv venv 
source venv/bin/activate
```

* Change directory
```
cd storage-service
```

* Create PostgreSQL
```bash
docker run --name some-postgres -p 5432:5432  -e POSTGRES_PASSWORD=postgres -d postgres
PGPASSWORD=postgres echo "create database storages;" | psql "host=127.0.0.1 user=postgres dbname=postgres"
```

* Create RabbitMQ
```bash
docker run -d -p 5672:5672 rabbitmq
```

* Install python requirements
```bash
pip install -r requirements.txt
```
* Set required environment vars (or use .env file) 
```bash
export CELERY_BROKER_URI="pyamqp://<username>@<hostname>//"
export DATABASE_CONNECTION_STRING="postgresql+psycopg2://<username>:<password>@<hostname>/<database>"
```
* Run worker 
```bash
celery -A app.Storage.storage_tasks worker
```
* Run tests 
```bash
pytest
```
* Run server
```bash
uvicorn app.api:app --host localhost --port 5000
```

