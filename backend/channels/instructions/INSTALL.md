## Installation

1. Change directory
```shell
cd backend/channels
```
2. Rename .env.dev-example to .env.dev, and update enviroment values.
3. To install project - enter command:
```shell
docker-compose -f docker-compose.yml up --build
```
4. To run docker build connection tests - enter command:
```shell
docker exec -it fastapi_channels poetry run pytest -v tests
```

Links on the local machine:
1. FastApi swagger docs: http://127.0.0.1:8000/docs
2. RabbitMq: http://127.0.0.1:15672
3. Flower: http://127.0.0.1:5555
4. MongoDB (MongoDBCompass): mongodb://127.0.0.1:27017

*Mark channels directory as Source Root in the Pycharm IDE.
