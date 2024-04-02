from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = "group"

urlpatterns = [
    path('', views.group_list, name='list'),
    path('group_create', views.group_create, name='group_create'),
    path('show/<int:id>', views.show, name='show'),
    path('show/add_user', views.add_user, name='add_user'),
    path('show/comment_create', views.comment_create, name='comment_create'),
    path('show/comment_delete/<int:id>', views.comment_delete, name='comment_delete'),
    path('show/delete_user', views.delete_user, name='delete_user'),
    path('group_delete/<int:id>', views.group_delete, name='group_delete'),
    path('edit/<int:id>', views.edit, name='edit'),
]


urlpatterns += staticfiles_urlpatterns()