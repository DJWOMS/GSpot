# Channesl service modules installation

Create virtual enviroment
```shell
python -m venv venv
```
Install poetry package
```shell
pip install poetry
```

Add fastapi framework (websockets, email-validator, jinja2, pydantic included)
```shell
poetry add fastapi[all]
```

Add pytest and pytest-asyncio modules
```shell
poetry add pytest
poetry add pytest-asyncio
```

Add motor (pymongo included)
```shell
poetry add motor
```

Add pika
```shell
poetry add pika
```

Add redis
```shell
poetry add redis
```

Add celery
```shell
poetry add celery
```

Add flower
```shell
poetry add flower
```
