from django.conf.urls import url
from . import views

app_name = 'grievances'

urlpatterns = [
    url(r'^$', views.complains_list, name="list"),
    url(r'^register/$', views.complain_new, name="register"),
    url(r'^respond/$', views.respond, name="respond"),
    url(r'^respond/(?P<id>[\w-]+)/$', views.display, name="disp"),
    url(r'^update/$', views.update, name="update"),
]