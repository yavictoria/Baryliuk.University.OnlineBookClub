from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = "manager"

urlpatterns = [
    path('', views.index, name='home'),
    path('users_list', views.users_list, name='users_list'),
    path('group_list', views.group_list, name='group_list'),
    path('group_show/<int:id>', views.group_show, name='group_show'),

]


urlpatterns += staticfiles_urlpatterns()