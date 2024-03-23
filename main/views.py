from django.shortcuts import render, redirect

# Create your views here.

### index site ###
def index(request):
    return render(request, 'main/home.html')


