from django.urls import re_path
from . import views

app_name='pages'
urlpatterns = [
    re_path(r'^$', views.index, name = 'index'),
    re_path(r'login/$', views.userLoginView, name = 'login'),
]
