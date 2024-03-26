from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = "group"

urlpatterns = [
    path('', views.group_list, name='list'),
    path('group_create', views.group_create, name='group_create'),
    path('show/<int:id>', views.show, name='show'),
    path('group_delete/<int:id>', views.group_delete, name='group_delete'),
    path('edit/<int:id>', views.edit, name='edit'),
]


urlpatterns += staticfiles_urlpatterns()