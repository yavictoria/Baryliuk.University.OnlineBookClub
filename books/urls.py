from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = "books"

urlpatterns = [
    path('', views.book_list, name='list'),
    path('a_book/<int:id>', views.a_book, name='a_book'),
    path('add_like/<int:id>/', views.add_like, name='add_like'),
]


urlpatterns += staticfiles_urlpatterns()