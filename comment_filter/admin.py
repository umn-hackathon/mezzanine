from django.contrib import admin

from comment_filter.models import CensoredWord

admin.site.register(CensoredWord)
