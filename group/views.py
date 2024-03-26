from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from main.keeper_service import keeper_service


# Create your views here.
def group_list(request):
    groups_list = Group.objects.order_by('-id')
    return render(request, 'group/list.html', {'instance_list':groups_list})

# show groups
def show(request, id):
    print(f"=== group, action: show === ")
    print(f"id: ", id)
    action= "show"



    group = get_object_or_404(Group, id=id)


    form = CreateComment()


    return render(request, 'group/show.html',
                  {'group':group,'form':form})

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
