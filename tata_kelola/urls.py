from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns =[
    url(r'^step1/$', views.step1, {'template_name': 'tata_kelola/step1.html'}, 'step1'),
    url(r'^home/$', TemplateView.as_view(template_name="tata_kelola/home.html"), {}, 'home'),
    url(r'^proyek_dashboard/$', TemplateView.as_view(template_name="tata_kelola/proyek_dashboard.html"), {}, 'proyek_dashboard'),
]