from django.shortcuts import render

# Create your views here.

### index site ###
def index(request):
    return render(request, 'main/home.html')