from app.worker.main import celery


@celery.task(name="send_request", queue="hello1")
def send_request(x):
    celery.send_task("get_request", args=[x], queue="hello2")
    return


@celery.task(name="show_result", queue="hello1")
def show_result(args):
    res = sum(args) * 5
    return res
