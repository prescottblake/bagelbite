from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^travel$', views.travel, name='travel'),
    url(r'^add_plan$', views.add_plan, name='add_plan'),
    url(r'^add_plan_process$', views.add_plan_process, name='add_plan_process'),
    url(r'^destination/(?P<id>[0-9]+)$', views.destination, name='destination'),
    url(r'^join$', views.join, name='join')
]
