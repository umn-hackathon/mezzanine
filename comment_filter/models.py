from django.db import models


class CensoredWord(models.Model):
    word = models.CharField(max_length = 225)

    def __str__(self):
        return self.word
