import smtplib
import ssl

from app.core.settings import settings
from app.worker.main import celery


@celery.task(name="send_admin_email", queue="email.send")
def send_admin_email(order_id, admin_email):
    message = f"""Subject: Order successfully created\n\n
    The order {order_id} was created!"""

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(
        settings.smtp_server, settings.mail_port, context=context
    ) as server:
        server.login(settings.sender_email, settings.mail_password)
        return server.sendmail(settings.sender_email, admin_email, message)


@celery.task(name="send_user_email", queue="email.send")
def send_user_email(order_id, user_email):
    message = f"""Subject: Order successfully created\n\n
    We received your order {order_id}. Our operator will contact you soon.

    Thank you!"""

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(
        settings.smtp_server, settings.mail_port, context=context
    ) as server:
        server.login(settings.sender_email, settings.mail_password)
        return server.sendmail(settings.sender_email, user_email, message)
