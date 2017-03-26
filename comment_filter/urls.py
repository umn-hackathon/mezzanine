from django.conf.urls import url
from comment_filter.views import censored_check, report_comment, notifications, notifications_mark_all_as_read


urlpatterns =[
    url(r'^censored_check/$', censored_check, {}, 'censored_check'),
    url(r'^report_comment/$', report_comment, {}, 'report_comment'),
    url(r'^notifications/$', notifications, {'template_name': 'notifications.html'}, 'notifications'),
    url(r'^notifications_mark_all_as_read/$', notifications_mark_all_as_read, {}, 'notifications_mark_all_as_read'),

]