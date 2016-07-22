from django.conf.urls import url
from . import views as login_register_views
urlpatterns = [
	url(r'^$', login_register_views.index, name="index"),
    url(r'^register$', login_register_views.register, name="register"),
    url(r'^login$', login_register_views.login, name="login"),
    url(r'^logout$', login_register_views.logout, name="logout"),
]
