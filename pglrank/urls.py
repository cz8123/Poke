from django.conf.urls import url
from django.urls import path
from .views import *
# from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'pglrank'


urlpatterns = [
	path('pgl/', pgl, name='pgl'),
    path('pgl/<str:s>', pgl, name='pgl'),
]
