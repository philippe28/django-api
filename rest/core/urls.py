from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter

from . import views

app_name = 'core'
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),


]


router = DefaultRouter()

