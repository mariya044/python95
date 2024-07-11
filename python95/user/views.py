from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Group
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from user.models import NewUser
from user.forms import UserRegisterForm
from announcement.models import Announcement
from post.models import Post


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            email = request.POST.get('email')
            user_group = Group.objects.get(name=form.cleaned_data['groups'])
            user.groups.add(user_group)
            send_mail(
                'Welcome',
                f'Nice to meet you {user}!',
                'EMAIL_HOST_USER',
                [email],
                fail_silently=False
            )
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {"form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"hellow{username}")
                return redirect('post:posts')
            else:
                messages.info(request, "Username or password is not  correct ")
        else:
            messages.info(request, "Username or password is not  correct ")
    form = AuthenticationForm()
    return render(request, 'login.html', {"form": form})


def custom_logout(request):
    logout(request)
    return redirect("login")


def account(request):
    context = {
        "announcements": Announcement.objects.filter(user=request.user),
        "posts": Post.objects.filter(user=request.user),
        "users": NewUser.objects.filter(email=request.user)
    }
    return render(request, 'account.html', context)
