from django.contrib.auth.models import User
from django.db import models

from django_comments.models import Comment

class CensoredWord(models.Model):
    word = models.CharField(max_length = 225)

    def __str__(self):
        return self.word


class ReportedComment(models.Model):
    comment = models.ForeignKey(Comment, related_name='reported_comments')
    reporter = models.ForeignKey(User, related_name='reported_comments')

    def __str__(self):
        return "{} - reported by {}".format(self.comment.comment, self.reporter)
