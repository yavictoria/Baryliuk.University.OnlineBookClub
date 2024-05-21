from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from main.keeper_service import keeper_service
from django.utils import timezone

# Create your views here.

### index site ###
def index(request):
    form = CreateFeedback()
    return render(request, 'main/home.html', {'form':form })


def feedback_create(request):
    print("request = ", request.POST)
    name = request.user
    date_created = timezone.now().date
    error = ''
    form = CreateFeedback(request.POST)

    if request.method == 'POST':
        form = CreateFeedback(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.user_id = name
            feedback.save()
            return redirect('main:home')
        else:
            error = 'Помилки при заповненні форми'
    context = {
        'form': form,
        'error': error,
        'name': name,
        'date_created': date_created
    }
    return render(request, 'main/feedback.html', context)

def report_create(request):
    print("request = ", request.POST)
    name = request.user
    date_created = timezone.now().date
    error = ''
    form = CreateReport(request.POST)

    if request.method == 'POST':
        form = CreateReport(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            report.user_id = name
            report.save()
            return redirect('main:home')
        else:
            error = 'Помилки при заповненні форми'
    context = {
        'form': form,
        'error': error,
        'name': name,
        'date_created': date_created
    }
    return render(request, 'main/report.html', context)





