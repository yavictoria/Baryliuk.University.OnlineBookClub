from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Group)
admin.site.register(Interest)
admin.site.register(Comment)
admin.site.register(RelGroupUser)
