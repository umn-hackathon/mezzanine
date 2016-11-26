from django.conf.urls import url
from  comment_filter.views import censored_check


urlpatterns =[
              url(r'^censored_check/$', censored_check, {}, 'censored_check'),
              ]