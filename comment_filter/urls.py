from django.conf.urls import url
from  comment_filter.views import censored_check, report_comment


urlpatterns =[
    url(r'^censored_check/$', censored_check, {}, 'censored_check'),
    url(r'^report_comment/$', report_comment, {}, 'report_comment'),
]