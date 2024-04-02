from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from main.keeper_service import keeper_service
from django.utils import timezone


# Create your views here.
def group_list(request):
    groups_list = Group.objects.order_by('-id')
    return render(request, 'group/list.html', {'instance_list':groups_list})

# show groups
def show(request, id):
    print(f"=== group, action: show === ")
    print("request = ", request.GET)

    action= "show"
    group = get_object_or_404(Group, id=id)
    user = request.user
    is_group_member = False
    comment_text = ''
    comment_creater = ''
    parent_comment = request.GET.dict().get("parent_comment")
    print('parent_comment: ', parent_comment)
    if parent_comment != None:
        comment = Comment.objects.get(id=parent_comment)
        comment_text = comment.comment
        comment_creater = comment.user_id


    form = CreateComment()
    sql = f"""select u.id , u.username, gu.id as rel_id
              from group_relgroupuser gu
                  join auth_user u on u.id = gu.user_id
              where gu.group_id = {id}"""
    users_list = RelGroupUser.objects.raw(sql)
    print('list: ', users_list)
    for el in users_list:
        if user.id == el.id:
            is_group_member = True


    comments_list = Comment.objects.filter(group_id=id).order_by('-id')

    context = {
        'group': group, 'form': form, 'users_list': users_list,
        'comments_list': comments_list, 'is_group_member': is_group_member,
        'parent_comment': parent_comment, 'comment_text': comment_text,
        'comment_creater': comment_creater
    }

    return render(request, 'group/show.html',context)

# add new forum
def group_create(request):
    form = CreateGroup()
    creator = request.user
    error = ''
    if request.method == 'POST':
        form = CreateGroup(request.POST)
        if form.is_valid():
            group = form.save(commit=False)
            group.creator = request.user
            group.save()
            return redirect('group:show', id=group.id)
        else:
            error = 'Помилки при заповненні форми'
    context = {
        'form':form,
        'error': error,
        'creator': creator,
    }
    return render(request, 'group/group_create.html', context)


# delete forum
def group_delete(request, id):
    print(f"=== group, action: group_delete === ")
    print(f"id: ", id)

    try:
        obj = None
        obj = Group.objects.get(id=id)
        print(f"obj: {obj}")
        obj.delete()
    except (Exception) as e:
        keeper_service.push("error", str(e))
        print(f"Error: {e}")

    return redirect('group:list')


# edit forum
def edit(request, id):
    print(f"=== group, action: edit === ")
    print(f"id: ", id)
    print(f"method: ", request.method)
    error = ''
    cur_action = "edit"

    group = get_object_or_404(Group, id=id)

    if request.method == 'POST':
        params = request.POST.dict()
        print(f"params: {params}")
        form = CreateGroup(request.POST, request.FILES, instance=group)
        if form.is_valid():
            form.save()
            return redirect('group:show', id=group.id)  # Redirect to forum detail view
        else:
            error = 'Помилки при заповненні форми'
            print('Помилки при заповненні форми')

    ### open form for updating
    else:
        form = CreateGroup(instance=group)

    return render(request, 'group/edit.html',
                  {'form': form, 'error':error, 'id':id})


def add_user(request):
    print(f"=== main, action: add-user === ")
    #print(f"request: {request.POST.dict() } ")
    group_id = request.POST.dict()['group_id']
    user_id = request.POST.dict()['user_id']
    print(f"group_id: {group_id}, user_id: {user_id} ")
    error = ''

    try:
        instance = RelGroupUser()
        instance.group = Group.objects.get(id=group_id)
        instance.user = User.objects.get(id=user_id)
        instance.save(force_insert=True)
    except (Exception) as e:
        keeper_service.push("error", str(e))
        print(f"Error: {e}")
    return redirect('group:show', id=group_id)

def delete_user(request):
    print(f"=== main, action: delete_user === ")

    group_id = request.POST.dict()['group_id']
    user_id = request.POST.dict()['user_id']
    rel_id = None

    sql = f"""select gu.id, gu.group_id as rel_id
                         from group_relgroupuser gu
                              where gu.group_id = {group_id} 
                                and gu.user_id = {user_id}"""

    rel = RelGroupUser.objects.raw(sql)

    rel_id = rel[0].id
    print('rel_id: ', rel_id)


    try:
        obj = None
        obj = RelGroupUser.objects.get(id=rel_id)
        print(f"obj: {obj}")
        obj.delete()

    except (Exception) as e:
        keeper_service.push("error", str(e))
        print(f"Error: {e}")
    return redirect('group:show', id=group_id)

def comment_create(request):
    print("request = ", request.POST)
    name = request.user
    date_created = timezone.now().date
    error = ''

    if request.method == 'POST':
        form = CreateComment(request.POST)
        if form.is_valid():
            group_id = int(request.POST['group_id'])
            parent_comment = request.POST.dict().get("parent_comment")

            comment = form.save(commit=False)
            comment.user_id = request.user
            comment.group_id = Group.objects.get(id=group_id)

            print('parent_comment: ', parent_comment)
            if parent_comment != 'None':
                comment.parent_comment = Comment.objects.get(id=parent_comment)

            comment.save()
            return redirect('group:show', id=group_id)
        else:
            error = 'Помилки при заповненні форми'
    context = {
        'form': form,
        'error': error,
        'name': name,
        'date_created': date_created
    }
    return render(request, 'group/show.html', context)


def comment_delete(request, id):
    print(f"=== forum, action: discussion_delete === ")
    print(f"id: ", id)

    try:
        obj = None
        obj = Comment.objects.get(id=id)
        group_id = obj.group_id.id
        print(f"group: {group_id}")
        obj.delete()
    except (Exception) as e:
        keeper_service.push("error", str(e))
        print(f"Error: {e}")

    return redirect('group:show',id=group_id)



