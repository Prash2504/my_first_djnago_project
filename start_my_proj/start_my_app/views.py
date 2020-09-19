from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from .models import UserPosts, my_choices
from .forms import SignUpForm
from django.views import View
from datetime import datetime

def signup_form(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        print("Valid", form.is_valid())
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            request.session["username"] = username
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


class UserLogin(View):

    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        print("Recevied post request")
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                print("User is active")
                request.session["username"] = username
                login(request, user)
                return redirect('/')
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username, password))
            return HttpResponse("Invalid login details given")

def index(request):
    if request.method == 'POST':
        UserLogin().post(request)

    if "username" in request.session:
        print("Getting into the view file")
        my_blog_data = UserPosts.objects.all()
        my_name = "Prashanth"
        return render(request,"home.html", locals())
    else:
        return render(request, 'login.html')

def myposts(request):
    print("Myposts")
    print(request.POST)
    if "username" in request.session:
        category = my_choices
        return render(request, "myposts.html", locals())
    else:
        return render(request, 'login.html')

def about(request):
    print("Adding data about me")
    if "username" in request.session:
        return render(request, "about.html")
    else:
        return render(request, 'login.html')

def logout(request):
    request.session.flush()
    return  render(request, "logout.html")
