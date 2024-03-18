from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import send_mail
from django.conf import  settings
from django.contrib.auth.decorators import login_required


@login_required
def welcome_email(request):
    username = request.user
    print("username = ", username)
    email = request.user.email
    print("email = ", email)
    subject = 'Welcome to our Book Club!'
    message = f'Hi {username}, thank you for choosing our book club. Now you can be the part of a reading family! '
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list, fail_silently=False)
    return redirect("main:home")


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        print("registration form is here")
        if form.is_valid():
            print("registration form is valid")
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("main:home")
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
            return render(request, "registry/register.html", {"register_form": form})
         #messages.error(request, "Unsuccessful registration. Invalid information.")
    else:
        form = NewUserForm()
    return render(request=request, template_name="registry/register.html", context={"register_form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("main:home")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="registry/login.html", context={"login_form": form})


def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.")
	return redirect("main:home")


