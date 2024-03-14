from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = "main"

urlpatterns = [
    path('', views.index, name='home'),
]


urlpatterns += staticfiles_urlpatterns()