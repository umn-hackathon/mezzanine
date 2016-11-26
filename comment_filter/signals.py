import requests

from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.db.models.signals import post_save, pre_save

from notifications.signals import notify
from mezzanine.generic.models import ThreadedComment


def notif_comment(sender, instance, created, **kwargs):

    send_mail(
        'Subject here',
        'Here is the message.',
        'from@example.com',
        ['to@example.com'],
        fail_silently=False,
    )

    requests.post(settings.DOMAIN_URL + '/comment_filter/censored_check/',
                  data={'comment_id': instance.comment_ptr_id,})

    user = User.objects.get(id=instance.by_author)
    if instance.replied_to_id:
        notify.send(instance, recipient=user, verb='you reached level 10')


def filter_comment(sender, instance, created, **kwargs):
    requests.post(settings.DOMAIN_URL + '/comment_filter/censored_check/',
                  data={'comment_id': instance.comment_ptr_id,})

post_save.connect(notif_comment, sender=ThreadedComment)
post_save.connect(notif_comment, sender=ThreadedComment)
