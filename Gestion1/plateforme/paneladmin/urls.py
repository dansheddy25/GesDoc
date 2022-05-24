from django.urls import re_path
from .import views

app_name = 'paneladmin'

urlpatterns = [
    re_path('wel', views.wel, name = 'wel'),

]
