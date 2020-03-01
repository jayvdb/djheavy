from __future__ import absolute_import, unicode_literals

from celery import shared_task

# from time import sleep
import binascii
import os

# Django
from django.core.cache import cache

# from django.core.mail import send_mail
# from django.conf import settings

from apps.mail.models import Mail

# local Django
from apps.utils.basetaskcelery import VerifyTaskBase
from djheavy.celery import app


@app.task(base=VerifyTaskBase)
def example_add(x: int, y: int):
    """
    ...
    """

    return x + y


@shared_task
def simulate_send_emails(text: str):
    """
    ...
    """

    Mail.objects.create(name=text)
    # print("task db", Mail.objects.count())

    # subject = 'Thank you for registering to our site'
    # message = ' it  means a world to us '
    # email_from = settings.EMAIL_HOST_USER
    # recipient_list = ['receiver@gmail.com']
    # send_mail(
    #     subject,
    #     message,
    #     email_from,
    #     recipient_list
    # )

    dict_task = {
        "sended_to": text,
    }
    return dict_task


@shared_task
def send_email_activation(username: str, email: str):
    """
    ...
    """

    token: str = binascii.hexlify(os.urandom(20)).decode()

    # subject = 'Thank you for registering to our site'
    # message = render_to_string('activate_account.html', {
    #     'username': request.data["username"],
    #     'domain': current_site.domain,
    #     'token': token,
    # })

    # email_from = settings.EMAIL_HOST_USER
    # recipient_list = [email]
    # send_mail(
    #     subject,
    #     message,
    #     email_from,
    #     recipient_list
    # )

    cache.set(token, f"{username}_{email}_{token}", 60)

    return token
