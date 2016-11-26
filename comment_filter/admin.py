from django.contrib import admin

from comment_filter.models import CensoredWord, ReportedComment


admin.site.register(CensoredWord)
admin.site.register(ReportedComment)
