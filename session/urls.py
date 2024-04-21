from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = "session"

urlpatterns = [
    path('', views.session_list, name='list'),

]


urlpatterns += staticfiles_urlpatterns()