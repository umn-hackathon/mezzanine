from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns =[
    url(r'^step1/$', views.step1, {'template_name': 'tata_kelola/step1.html'}, 'step1'),
    url(r'^step2/$', views.step2, {'template_name': 'tata_kelola/step2.html'}, 'step2'),
    url(r'^step3/$', views.step3, {'template_name': 'tata_kelola/step3.html'}, 'step3'),
    url(r'^step4/$', views.step4, {'template_name': 'tata_kelola/step4.html'}, 'step4'),
    url(r'^step5/$', views.step5, {'template_name': 'tata_kelola/step5.html'}, 'step5'),
    url(r'^home/$', TemplateView.as_view(template_name="tata_kelola/home.html"), {}, 'home'),
    url(r'^proyek_dashboard/$', TemplateView.as_view(template_name="tata_kelola/proyek_dashboard.html"), {}, 'proyek_dashboard'),
]