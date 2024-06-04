from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = "manager"

urlpatterns = [
    path('', views.index, name='home'),
    path('users_list', views.users_list, name='users_list'),
    path('group_list', views.group_list, name='group_list'),
    path('feedback_list', views.feedback_list, name='feedback_list'),
    path('report_list', views.report_list, name='report_list'),
    path('group_show/<int:id>', views.group_show, name='group_show'),
    path('report_list/report_delete/<int:id>', views.report_delete, name='report_delete'),

]


urlpatterns += staticfiles_urlpatterns()