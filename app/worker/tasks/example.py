from app.core.settings import settings
from app.worker.main import celery

@celery.task(name='send_request', queue='hello1')
def send_request(x):
    celery.send_task('get_request', args=[x], queue='hello2')
    return


@celery.task(name='show_result',queue='hello1')
def show_result(args):
    res=sum(args) * 5
    return res

@celery.task(name='send_request_email_admin', queue='email.send')
def send_request_admin(order_id):
    return celery.send_task(
        "send_email_admin",
        args=[],
        kwargs={
            "address":settings.email_admin,
            "message_text": f'Order #{order_id} was created'
        },
        queue="email.manage",
        serializer="json"
    )

@celery.task(name='send_request_email_user', queue='email.send')
def send_request_user(order_id, email):
    return celery.send_task(
        "send_email_user",
        args=[],
        kwargs={
            "address":email,
            "message_text": f'The #{order_id} was successfully created. Thank you!'
        },
        queue="email.manage",
        serializer="json"
    )
