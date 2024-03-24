from django.shortcuts import render, redirect,  get_object_or_404
from .forms import *
from .models import *
from django.utils import timezone
from main.keeper_service import keeper_service

# list of forums
def forum_list(request):
    forums_list = Forum.objects.order_by('-id')
    return render(request, 'forum/list.html', {'instance_list':forums_list})

# show forum
def show(request, id):
    print(f"=== forum, action: show === ")
    print(f"id: ", id)
    action= "show"



    forum = get_object_or_404(Forum, id=id)
    discussions_list = Discussion.objects.filter(forum=id).order_by('-id')

    form = CreateInDiscussion()


    return render(request, 'forum/show.html',
                  {'forum':forum,'form':form, 'discussions_list':discussions_list})

# add new forum
def forum_create(request):
    form = CreateInForum()
    name = request.user
    date_created = timezone.now().date
    error = ''
    if request.method == 'POST':
        form = CreateInForum(request.POST)
        if form.is_valid():
            forum = form.save(commit=False)
            forum.name = request.user
            forum.save()
            return redirect('forum:show', id=forum.id)
        else:
            error = 'Помилки при заповненні форми'
    context = {
        'form':form,
        'error': error,
        'name': name,
        'date_created': date_created
    }
    return render(request, 'forum/forum_create.html', context)


# delete forum
def forum_delete(request, id):
    print(f"=== forum, action: forum_delete === ")
    print(f"id: ", id)

    try:
        obj = None
        obj = Forum.objects.get(id=id)
        print(f"obj: {obj}")
        obj.delete()
    except (Exception) as e:
        keeper_service.push("error", str(e))
        print(f"Error: {e}")

    return redirect('forum:list')


# edit forum
def edit(request, id):
    print(f"=== forum, action: edit === ")
    print(f"id: ", id)
    print(f"method: ", request.method)
    error = ''
    cur_action = "edit"

    forum = get_object_or_404(Forum, id=id)

    if request.method == 'POST':
        params = request.POST.dict()
        print(f"params: {params}")
        form = CreateInForum(request.POST, request.FILES, instance=forum)
        if form.is_valid():
            form.save()
            return redirect('forum:show', id=forum.id)  # Redirect to forum detail view
        else:
            error = 'Помилки при заповненні форми'
            print('Помилки при заповненні форми')

    ### open form for updating
    else:
        form = CreateInForum(instance=forum)

    return render(request, 'forum/edit.html',
                  {'form': form, 'error':error,'name':forum.name,
                   'date_created':forum.date_created, 'id':id})


# add comments to forum
def discussion_create(request):
    print("request = ", request.POST)
    name = request.user
    date_created = timezone.now().date
    error = ''

    if request.method == 'POST':
        form = CreateInDiscussion(request.POST)
        if form.is_valid():
            forum_id = int(request.POST['forum_id'])
            discussion = form.save(commit=False)
            discussion.name = request.user
            discussion.forum = Forum.objects.get(id=forum_id)
            discussion.save()
            return redirect('forum:show', id=forum_id)
        else:
            error = 'Помилки при заповненні форми'
    context = {
        'form': form,
        'error': error,
        'name': name,
        'date_created': date_created
    }
    return render(request, 'forum/show.html', context)


# delete discussion
def discussion_delete(request, id):
    print(f"=== forum, action: discussion_delete === ")
    print(f"id: ", id)

    try:
        obj = None
        obj = Discussion.objects.get(id=id)
        forum_id = obj.forum.id
        print(f"forum: {forum_id}")
        obj.delete()
    except (Exception) as e:
        keeper_service.push("error", str(e))
        print(f"Error: {e}")

    return redirect('forum:show',id=forum_id)


