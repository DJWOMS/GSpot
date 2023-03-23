import pytest
from app_celery.celery import ping


@pytest.mark.usefixtures("celery_config")
def test_celery_tasks(celery_app, celery_worker):
    assert ping.delay().get() == "pong"
