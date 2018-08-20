from django.conf.urls import url
from . import views

app_name = 'accounts'

urlpatterns = [
   url(r'^signup/$', views.Csignup_view, name="signup"),
   url(r'^login/$', views.Clogin_view, name="login"),
   url(r'^logout/$', views.Clogout_view, name="logout"),
]