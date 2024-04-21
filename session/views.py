from django.shortcuts import render, redirect,  get_object_or_404
from .forms import *
from .models import *
from django.utils import timezone
from main.keeper_service import keeper_service
from user.models import  Profile_user

# list of sessions
def session_list(request):
    sessions_list = Session.objects.order_by('-id')
    author = False

    user = request.user
    user_profile = Profile_user.objects.filter(user_id=user.id)
    if user_profile.exists():
        profile_u = Profile_user.objects.get(user_id=user.id)
        print('profile_u: ', profile_u.is_author)
        if profile_u.is_author == True:
            author = True

    print('author: ', author)
    return render(request, 'session/list.html', {'instance_list':sessions_list,
                                                                    'author': author})


