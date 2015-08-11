from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
  url(r'^api-browsable/', include('rest_framework.urls', namespace='rest_framework'))
)
