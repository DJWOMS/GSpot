from config.celery import app


@app.task
def get_item_for_self_user():
    pass


@app.task
def gift_item_to_other_user():
    pass
