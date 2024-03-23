from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = "forum"

urlpatterns = [
    path('', views.forum_list, name='list'),
    path('forum_create', views.forum_create, name='forum_create'),
    path('show/<int:id>', views.show, name='show'),
    path('show/discussion_create', views.discussion_create, name='discussion_create'),
    path('forum_delete/<int:id>', views.forum_delete, name='forum_delete'),
    path('edit/<int:id>', views.edit, name='edit'),
]


urlpatterns += staticfiles_urlpatterns()