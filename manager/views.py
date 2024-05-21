from django.shortcuts import render, redirect, get_object_or_404
from user.models import Profile_user
from django.contrib.auth.models import User
from group.models import *
from main.models import Feedback, Report

# Create your views here.
def index(request):
    return render(request, 'manager/home.html')

def users_list(request):
    users_list = User.objects.order_by('-id')
    return render(request, 'manager/users_list.html', {'instance_list':users_list})

def group_list(request):
    groups_list = Group.objects.order_by('-id')
    return render(request, 'manager/group_list.html', {'instance_list':groups_list})

def feedback_list(request):
    feedbacks_list = Feedback.objects.order_by('-id')
    return render(request, 'manager/feedback_list.html', {'instance_list':feedbacks_list})
def report_list(request):
    reports_list = Report.objects.order_by('-id')
    return render(request, 'manager/report_list.html', {'instance_list':reports_list})


def report_delete(request, id):
    print(f"=== report, action: report_delete === ")
    print(f"id: ", id)

    try:
        obj = None
        obj = Report.objects.get(id=id)
        print(f"obj: {obj}")
        obj.delete()
    except (Exception) as e:
        keeper_service.push("error", str(e))
        print(f"Error: {e}")


    return redirect('manager:report_list')



def group_show(request, id):
    print(f"=== group, action: show === ")
    print("request = ", request.GET)

    action= "show"
    group = get_object_or_404(Group, id=id)
    user = request.user
    comment_text = ''
    comment_creater = ''
    parent_comment = request.GET.dict().get("parent_comment")
    print('parent_comment: ', parent_comment)
    if parent_comment != None:
        comment = Comment.objects.get(id=parent_comment)
        comment_text = comment.comment
        comment_creater = comment.user_id





    comments_list = Comment.objects.filter(group_id=id).order_by('-id')

    context = {
        'group': group, 'users_list': users_list,
        'comments_list': comments_list,
        'parent_comment': parent_comment, 'comment_text': comment_text,
        'comment_creater': comment_creater
    }

    return render(request, 'manager/group_show.html',context)
