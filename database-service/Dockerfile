FROM python:3.9-alpine

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

RUN apk update

RUN apk add postgresql15-client

COPY ./app /code/app

CMD ["uvicorn", "app.api:app", "--host", "0.0.0.0", "--port", "80"]
